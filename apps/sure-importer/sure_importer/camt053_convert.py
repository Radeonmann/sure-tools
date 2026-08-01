import logging
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, Literal
from urllib.parse import quote_plus
from uuid import UUID

from camt_parser import TransactionInfo
from sure_api_client.models.post_api_v1_transactions_body import PostApiV1TransactionsBody
from sure_api_client.models.post_api_v1_transactions_body_transaction import PostApiV1TransactionsBodyTransaction
from sure_api_client.types import UNSET

# Logger setup
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Camt053ConverterSettings:
    """Holds settings for the CAMT.053 converter."""

    sure_transaction_source: str = "camt053"
    """ID which identifies the source of the transaction in sure.am. This is used to track where the transaction came from (e.g. API, importer, etc.)"""
    counterparty_name_fallback: str = "<Unknown Counterparty>"
    """Fallback name to use if no other name can be determined from the CAMT.053 transaction."""
    date_source: Literal["BookingDate", "ValueDate"] = "BookingDate"
    """Sure only supports a single date field for transactions. This setting determines which date from the CAMT.053 transaction is used for the sure.am transaction date."""
    id_use_batch_index_fallback: bool = True
    """
    Determines whether to use the batch index as a fallback identifier for transactions when TransactionAccountServicerReference is missing.
    If True, the batch index will be appended to the EntryAccountServicerReference to create a unique identifier for the transaction.
    If False, an error will be raised if TransactionAccountServicerReference is missing for a batch transaction.
    """


@dataclass(frozen=True)
class Camt053ConverterLookups:
    """Holds lookup dictionaries for accounts, categories, and tags."""

    accounts_by_iban: dict[str, UUID] = field(default_factory=dict)
    """Mapping of IBAN strings to sure.am account UUIDs. Used to look up the correct account for a transaction based on its IBAN."""
    categories_by_name: dict[str, UUID] = field(default_factory=dict)
    """Mapping of category names to sure.am category UUIDs. Used to look up the correct category for a transaction based on its name."""
    tags_by_name: dict[str, UUID] = field(default_factory=dict)
    """Mapping of tag names to sure.am tag UUIDs. Used to look up the correct tag for a transaction based on its name."""


@dataclass(frozen=True)
class Camt053ConverterContext:
    """Holds the context for the CAMT.053 converter, including settings and lookups."""

    settings: Camt053ConverterSettings
    """Settings for the CAMT.053 converter."""
    lookups: Camt053ConverterLookups
    """Lookup dictionaries for the CAMT.053 converter."""


def _tx_log_prefix(camt_tx: TransactionInfo) -> str:
    """
    Generates a log prefix for a CAMT.053 transaction, to quickly identify it in logs.
    Uses various IDs in a fallback in order to maximize the chance of having a unique identifier for the transaction in logs.
    """
    # Handle entries with at least one AccountServicerReference at first
    if camt_tx.TransactionAccountServicerReference:
        return f"Transaction {camt_tx.TransactionAccountServicerReference}"
    if camt_tx.EntryAccountServicerReference and not camt_tx.IsBatch:
        return f"Entry {camt_tx.EntryAccountServicerReference}"
    if camt_tx.EntryAccountServicerReference:
        return f"Entry {camt_tx.EntryAccountServicerReference} Transaction #{camt_tx.BatchIndex}"
    # Use other IDs as fallback
    fallback_id = (
        camt_tx.EndToEndId
        or camt_tx.InstructionId
        or camt_tx.PaymentInformationId
        or camt_tx.ClearingSystemReference
        or camt_tx.EntryReference
    )
    if fallback_id:
        return f"Transaction {fallback_id}"
    # Use amount and date as last resort
    return f"Transaction (Amt: {camt_tx.Amount}{camt_tx.Currency}, BookgDt: {camt_tx.BookingDate}, ValDt: {camt_tx.ValueDate})"


def _lookup_account_id_by_iban(iban: str, context: Camt053ConverterContext) -> UUID:
    """Looks up the sure.am account UUID from ACCOUNTS_BY_IBAN using the IBAN string."""
    clean_iban = iban.replace(" ", "").upper()
    account_uuid = context.lookups.accounts_by_iban.get(clean_iban)
    if not account_uuid:
        raise KeyError(f"IBAN '{iban}' not found in ACCOUNTS_BY_IBAN mapping dictionary.")
    return account_uuid


def _extract_sure_account_uuid(camt_tx: TransactionInfo, context: Camt053ConverterContext) -> UUID:
    """
    Extracts the account UUID from a CAMT.053 transaction using the IBAN.
    Raises ValueError if the IBAN is missing or empty.
    Raises KeyError if the IBAN is not found in the ACCOUNTS_BY_IBAN mapping.
    """
    iban = camt_tx.AccountIBAN
    if not iban:
        raise ValueError(f"Missing 'AccountIBAN' in transaction: {camt_tx}")
    return _lookup_account_id_by_iban(iban, context)


def _extract_sure_date(camt_tx: TransactionInfo, context: Camt053ConverterContext) -> date:
    """
    Extracts the date from a CAMT.053 transaction.
    - Uses BookingDate and raises an error if not present.
    - Returns the date as a datetime.date object
    """
    match context.settings.date_source:
        case "BookingDate":
            date_or_dt = camt_tx.BookingDate
        case "ValueDate":
            date_or_dt = camt_tx.ValueDate
        case _:
            raise ValueError(f"Unsupported date source: {context.settings.date_source}")
    if date_or_dt is None:
        raise ValueError(f"Missing '{context.settings.date_source}' in transaction: {camt_tx}")
    if isinstance(date_or_dt, datetime):
        return date_or_dt.date()
    elif isinstance(date_or_dt, date):
        return date_or_dt
    else:
        raise TypeError(f"Unexpected type for {context.settings.date_source}: {type(date_or_dt)}")


def _extract_sure_amount(camt_tx: TransactionInfo) -> float:
    """
    Extracts the amount from a CAMT.053 transaction and converts it to the correct sign for sure.am.
    - CRDT (Inflow/Credit)  -> Negative (-amount)
    - DBIT (Outflow/Debit)  -> Positive (+amount)
    """
    indicator = camt_tx.CreditDebitIndicator
    match indicator:
        case "CRDT":
            return float(-camt_tx.Amount)
        case "DBIT":
            return float(camt_tx.Amount)
        case _:
            raise ValueError(f"Unexpected CreditDebitIndicator '{indicator}' in transaction: {camt_tx}")


def _extract_counterparty_name_from_raw_text(text: str | None) -> str | None:
    """
    Attempts to extract a counterparty name from raw text fields in a CAMT.053 transaction.

    This function only handles cases, where the counterparty is not explicitly provided in the structured fields of the CAMT.053 transaction,
    but is instead embedded in the raw text fields (e.g., AdditionalTransactionInfo, AdditionalEntryInfo, UnstructuredRemittanceInfo).

    Following cases are currently handled:
    - TWINT: Extracts the name after "TWINT:" (case-insensitive) in the text, e.g., "Belastung TWINT: SHELL (SWITZERLAND) AG BAAR" -> "SHELL (SWITZERLAND) AG BAAR"

    Returns the extracted name if found, otherwise returns None.
    """
    # empty -> None
    if not text:
        return None
    # TWINT: Extract the name after "TWINT:" (case-insensitive)
    twint_marker = "TWINT:"
    twint_pos = text.upper().find(twint_marker)
    if twint_pos != -1:
        # Extract the substring after "TWINT:"
        name_start_pos = twint_pos + len(twint_marker)
        return text[name_start_pos:].strip()
    # unhandled cases -> None
    return None


def _extract_sure_tx_name_channel(camt_tx: TransactionInfo) -> str | None:
    """
    Extracts the payment channel/mechanism, which is appended to the transaction name in parentheses.
    Example: 'Starbucks (TWINT)' or 'Coop (Card)' or 'Wingo (eBill)'

    We do not want to use it for categorization, as it may overlap with categorization and other UI elements.
    We also do not want to indicate the direction (e.g. Card Purchase), as the direction is already indicated by the sign of the amount.

    Returns the channel name, e.g. 'TWINT', 'Card', 'eBill', or None if it cannot be determined.
    """
    # Fetch ISO codes from both Transaction and Entry levels
    family = (camt_tx.TransactionFamilyCode or "").upper()
    sub_family = (camt_tx.TransactionSubFamilyCode or "").upper()
    ntry_family = (camt_tx.EntryTransactionFamilyCode or "").upper()
    ntry_sub_family = (camt_tx.EntryTransactionSubFamilyCode or "").upper()
    # Fetch Text fields and Indicator
    add_info = f"{camt_tx.AdditionalTransactionInfo or ''} {camt_tx.AdditionalEntryInfo or ''}"
    add_info_upper = add_info.upper()
    indicator = camt_tx.CreditDebitIndicator
    # Proprietary swiss specific channels -> must be parsed from the text fields, as they are not standardized in the ISO codes
    if "EBILL" in add_info_upper:
        return "eBill"
    if "TWINT" in add_info_upper:
        return "TWINT"
    # The Automatic transfer Channels
    if "STDO" in (sub_family, ntry_sub_family):
        return "Standing Order"
    if "IDDT" in (family, ntry_family) or "RDDT" in (family, ntry_family):
        return "Direct Debit"
    # The Card & Cash Channels
    if "CCRD" in (family, ntry_family):
        if "CDPT" in (sub_family, ntry_sub_family) or "CWDL" in (sub_family, ntry_sub_family):
            return "ATM"
        return "Card"  # Covers POSD (Purchase), RIMB (Refund), and fallbacks
    # Default (Standard wires, invoices, internal transfers)
    return None


def _extract_counterparty_name(camt_tx: TransactionInfo, context: Camt053ConverterContext) -> str:
    """
    Extracts the counterparty name from a CAMT.053 transaction.
    - Uses the creditor name for DBIT transactions and the debtor name for CRDT transactions.
    - Falls back to the card POI ID if available.
    - As fallback, try to extract the name from the additional transaction info, additional entry info, or unstructured remittance info.
    """
    # Use the creditor, debtor name or card POI ID if available
    indicator = camt_tx.CreditDebitIndicator
    creditor = camt_tx.UltimateCreditorName or camt_tx.CreditorName
    debtor = camt_tx.UltimateDebtorName or camt_tx.DebtorName
    if indicator == "DBIT" and creditor:
        return creditor
    elif indicator == "CRDT" and debtor:
        return debtor
    if camt_tx.CardPoiId:
        return camt_tx.CardPoiId
    # Try to extract the name from all raw text fields
    from_add_tx_info = _extract_counterparty_name_from_raw_text(camt_tx.AdditionalTransactionInfo)
    if from_add_tx_info:
        return from_add_tx_info
    from_add_entry_info = _extract_counterparty_name_from_raw_text(camt_tx.AdditionalEntryInfo)
    if from_add_entry_info:
        return from_add_entry_info
    from_unstructured_remittance = _extract_counterparty_name_from_raw_text(camt_tx.UnstructuredRemittanceInfo)
    if from_unstructured_remittance:
        return from_unstructured_remittance
    # nothing works, fallback to default name from settings:
    default = context.settings.counterparty_name_fallback
    logger.warning(f"{_tx_log_prefix(camt_tx)}: Could not determine a counterparty name, falling back to default name '{default}'")
    return default


def _extract_sure_name(camt_tx: TransactionInfo, context: Camt053ConverterContext) -> str:
    """
    Extracts the clean display name and appends the transaction channel.
    For display we use the name of the counterparty (creditor or debtor).
    We also append the transaction channel/type in parentheses if it exists.
    Details are in the description.
    Example: 'Starbucks (TWINT)' or 'ABB CAPITAL AG (Bank Transfer)'

    In case we cannot determine a name, we fallback to the unstructured remittance info, and if that is also missing, we fallback to "Bank Transaction".

    This data is intended to be used for display purposes in the sure.am UI and should be human-readable.
    Also it is used for manual rule creation
    """
    counterparty_name = _extract_counterparty_name(camt_tx, context)
    tx_channel = _extract_sure_tx_name_channel(camt_tx)
    if tx_channel:
        return f"{counterparty_name} ({tx_channel})"
    else:
        return counterparty_name


def _extract_sure_description(camt_tx: TransactionInfo, context: Camt053ConverterContext) -> str:
    """
    Extracts a structured description from a CAMT.053 transaction, including all relevant metadata, codes, and raw text fields.
    The description is intended to be used for display purposes in the sure.am details UI and should be human-readable.
    It is also used for AI-based categorization and rule creation, so it should contain all relevant information for that purpose.
    The description is a pipe-separated key / value string.

    E.g.:
    `To: Starbucks | FX: 100.00 USD (Rate: 0.85) | Fees: 2.50 USD | CardNr: 1234 | CardPOI: POI123 | CreditorRef: INV-12345 | DocRef: DOC-67890 | ... | Raw: ...additional info text...`
    """
    # Dict for parts which will be joined together to form the final description string
    # Key is the label, value is the content. None and empty string values will be filtered out.
    # We try to use a sorting which makes sense for humans to read, but also for AI-based categorization and rule creation.
    # So we try to put the most relevant information first, and the codes and references later, and the raw text fields last.
    desc_parts: dict[str, str | None] = {}
    # ---------------------------------------------------------
    # HUMAN READABLE / UX FIRST -> Quickly visible in the UI
    # ---------------------------------------------------------
    # Counterparty
    counterparty_name = _extract_counterparty_name(camt_tx, context=context)
    indicator = camt_tx.CreditDebitIndicator
    if indicator == "DBIT":
        desc_parts["To"] = counterparty_name
    elif indicator == "CRDT":
        desc_parts["From"] = counterparty_name
    else:
        raise ValueError(f"{_tx_log_prefix(camt_tx)}: Unexpected CreditDebitIndicator '{indicator}'")
    # Financial Meta (FX & Charges)
    if camt_tx.ForeignAmount is not None:
        desc_parts["FX"] = f"{camt_tx.ForeignAmount} {camt_tx.ForeignCurrency} (Rate: {camt_tx.ExchangeRate})"
    if camt_tx.ChargesAmount is not None:
        desc_parts["Fees"] = f"{camt_tx.ChargesAmount} {camt_tx.ChargesCurrency}"
    # Card Information
    desc_parts["CardNr"] = camt_tx.CardPan
    desc_parts["CardPOI"] = camt_tx.CardPoiId
    # User-Friendly References (Invoices, QR-Refs)
    desc_parts["CreditorRef"] = camt_tx.CreditorReference
    desc_parts["DocRef"] = camt_tx.DocumentReferenceNumber
    # ---------------------------------------------------------
    # EXPERT / AI METADATA & CODES (Pushed to the back)
    # ---------------------------------------------------------
    # Entry-Level Codes
    ntry_codes = [c for c in [camt_tx.EntryDomainCode, camt_tx.EntryTransactionFamilyCode, camt_tx.EntryTransactionSubFamilyCode] if c]
    if ntry_codes:
        desc_parts["NtryBkTxCd"] = "-".join(ntry_codes)
    desc_parts["NtryPrtryCd"] = camt_tx.EntryProprietaryTransactionCode
    desc_parts["NtryPurpCd"] = camt_tx.EntryPurposeCode
    desc_parts["NtryPurpPrtry"] = camt_tx.EntryPurposeProprietary
    desc_parts["NtryRtrRsn"] = camt_tx.EntryReturnReasonCode
    # Transaction-Level Codes
    tx_codes = [c for c in [camt_tx.DomainCode, camt_tx.TransactionFamilyCode, camt_tx.TransactionSubFamilyCode] if c]
    if tx_codes:
        desc_parts["TxDtlsBkTxCd"] = "-".join(tx_codes)
    desc_parts["TxDtlsPrtryCd"] = camt_tx.ProprietaryTransactionCode
    desc_parts["TxDtlsPurpCd"] = camt_tx.PurposeCode
    desc_parts["TxDtlsPurpPrtry"] = camt_tx.PurposeProprietary
    desc_parts["TxDtlsRtrRsn"] = camt_tx.ReturnReasonCode
    # Core System References
    desc_parts["TxAcctSvcrRef"] = camt_tx.TransactionAccountServicerReference
    desc_parts["EntryAcctSvcrRef"] = camt_tx.EntryAccountServicerReference
    desc_parts["EndToEndId"] = camt_tx.EndToEndId
    desc_parts["PmtInfId"] = camt_tx.PaymentInformationId
    desc_parts["ClrSysRef"] = camt_tx.ClearingSystemReference
    desc_parts["InstrId"] = camt_tx.InstructionId
    desc_parts["MandateId"] = camt_tx.MandateId
    # ---------------------------------------------------------
    # RAW TEXT
    # ---------------------------------------------------------
    raw_text_fields = [
        camt_tx.AdditionalEntryInfo,
        camt_tx.AdditionalTransactionInfo,
        camt_tx.UnstructuredRemittanceInfo,
        camt_tx.ReturnAdditionalInfo,
    ]
    raw_texts_deduplicated = []
    for text_block in raw_text_fields:
        if text_block and text_block not in raw_texts_deduplicated:
            if not any(text_block in existing for existing in raw_texts_deduplicated):
                raw_texts_deduplicated.append(text_block)

    if raw_texts_deduplicated:
        raw_string = " - ".join(raw_texts_deduplicated).replace("\n", " ")
        desc_parts["Raw"] = raw_string

    # Build the final description string
    filtered_desc_parts = {k: v for k, v in desc_parts.items() if v is not None and str(v).strip() != ""}
    prefixed_desc_parts = [f"{k}: {v}" for k, v in filtered_desc_parts.items()]
    return " | ".join(prefixed_desc_parts)


def _extract_sure_external_id(camt_tx: TransactionInfo, context: Camt053ConverterContext) -> str:
    """
    Extracts a collision-proof external_id from a CAMT.053 transaction, based on AccountServicerReference.
    - Single transaction: TransactionAccountServicerReference or EntryAccountServicerReference
    - Batch transaction: TransactionAccountServicerReference
    - Batch transaction fallback: EntryAccountServicerReference + BatchIndex (if enabled in settings)

    Raises ValueError if both references are missing, or if a batch transaction is missing the TransactionAccountServicerReference, as we cannot generate a unique external_id.
    """
    if camt_tx.TransactionAccountServicerReference:
        return camt_tx.TransactionAccountServicerReference
    if camt_tx.EntryAccountServicerReference:
        if not camt_tx.IsBatch:
            return camt_tx.EntryAccountServicerReference
        elif context.settings.id_use_batch_index_fallback:
            return f"{camt_tx.EntryAccountServicerReference}-batch-{camt_tx.BatchIndex}"
        else:
            raise ValueError(
                f"{_tx_log_prefix(camt_tx)}: Missing TransactionAccountServicerReference for batch transaction, cannot generate unique external_id."
            )
    # If we reach this point, it means we cannot generate a unique external_id for the transaction, so we raise an error.
    raise ValueError(
        f"{_tx_log_prefix(camt_tx)}: Missing both TransactionAccountServicerReference and EntryAccountServicerReference, cannot generate unique external_id."
    )


def camt_transaction_to_payload(camt_tx: TransactionInfo, context: Camt053ConverterContext) -> PostApiV1TransactionsBody:
    transaction = PostApiV1TransactionsBodyTransaction(
        account_id=_extract_sure_account_uuid(camt_tx, context),
        date=_extract_sure_date(camt_tx, context),
        amount=_extract_sure_amount(camt_tx),
        name=_extract_sure_name(camt_tx, context),
        description=_extract_sure_description(camt_tx, context),
        notes=UNSET,
        currency=UNSET,
        category_id=UNSET,
        merchant_id=UNSET,
        nature=UNSET,
        external_id=_extract_sure_external_id(camt_tx, context),
        source=context.settings.sure_transaction_source,
        tag_ids=UNSET,
    )
    return PostApiV1TransactionsBody(
        transaction=transaction,
    )
