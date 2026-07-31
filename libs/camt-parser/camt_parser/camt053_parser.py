import copy
import logging
import pathlib
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Literal

from lxml import etree as ET

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Camt053ParserSettings:
    exchange_rate_result_tolerance: Decimal = Decimal("0.006")
    """
    Absolute error tolerance of the exchange rate calculation to account for rounding errors in the amounts.

    The value is in the currency of the ledger amount. For example, if the ledger amount is in CHF, then this value is in CHF.
    e.g.
    calculated_ledger = foreign_amt * xchg_rate
    absolute_error = abs(calculated_ledger - stated_ledger_amt)
    is_valid = absolute_error <= EXCHANGE_RATE_RESULT_TOLERANCE

    Default is 0.006, which is slightly more than half a cent. This is usually sufficient to account for rounding errors in the amounts,
    which are usually rounded to 2 decimal places. If the bank provides low resolution rates or amounts, this may need to
    be increased to avoid false positives.
    """


@dataclass(frozen=True)
class XmlElementDict:
    text: str | None
    attrib: dict[str, str]
    children: dict[str, list["XmlElementDict"]]


@dataclass(frozen=True)
class StatementInfo:
    StatementId: str | None
    LegalSequenceNumber: str | None
    ElectronicSequenceNumber: str | None
    StatementCreationDate: date | datetime | None
    FromDateTime: date | datetime | None
    ToDateTime: date | datetime | None
    AccountIBAN: str | None
    AccountIdOther: str | None
    AccountCurrency: str
    AccountOwner: str | None
    OpeningBalance: Decimal | None
    ClosingBalance: Decimal | None
    # Advanced Raw XML Payload Includes whole tree, but stripped of all elements which are not descendants or ancestors
    Advanced: XmlElementDict


@dataclass(frozen=True)
class EntryInfo:
    # Identifiers & References
    EntryReference: str | None
    AccountServicerReference: str | None

    # Financial Details - Account / Ledger (always in Account Currency)
    Amount: Decimal
    Currency: str
    CreditDebitIndicator: Literal["CRDT", "DBIT"]
    BookingDate: date | datetime | None
    ValueDate: date | datetime | None

    # Secondary Foreign Financials (Only if a currency conversion happened)
    ForeignAmount: Decimal | None
    ForeignCurrency: str | None
    ExchangeRate: Decimal | None

    # Other Metadata
    Status: str | None
    ReversalIndicator: bool
    AdditionalEntryInfo: str | None
    DomainCode: str | None
    TransactionFamilyCode: str | None
    TransactionSubFamilyCode: str | None
    ProprietaryTransactionCode: str | None
    ReturnReasonCode: str | None
    PurposeCode: str | None
    PurposeProprietary: str | None
    CardPoiId: str | None
    CardPan: str | None
    ChargesAmount: Decimal | None
    ChargesCurrency: str | None
    # Advanced Raw XML Payload Includes whole tree, but stripped of all elements which are not descendants or ancestors
    Advanced: XmlElementDict


@dataclass(frozen=True)
class TransactionInfo:
    # Statement Context
    AccountIBAN: str | None
    """The IBAN of the ledger account."""
    StatementId: str | None
    """The ID of the parent statement."""

    # Identifiers & References
    EntryAccountServicerReference: str | None
    """The bank's internal reference for the Entry (Ntry)."""
    TransactionAccountServicerReference: str | None
    """The bank's internal reference for the specific transaction (TxDtls) (if provided, it is unique within a batch in this parser)."""
    EntryReference: str | None
    """The primary reference of the Entry."""
    PaymentInformationId: str | None
    """The ID of the payment batch/instruction provided by the initiating system."""
    ClearingSystemReference: str | None
    """The central bank or clearing system trace ID."""
    EndToEndId: str | None
    """The End-to-End tracking ID provided by the initiator."""
    InstructionId: str | None
    """Point-to-point reference assigned by the instructing party."""
    MandateId: str | None
    """Direct Debit mandate identifier."""

    # Financial Details - Account / Ledger (Always present, always in Account Currency)
    Amount: Decimal
    """The final settled amount applied to the ledger. Is always positive or zero."""
    Currency: str
    """The currency of the ledger account."""
    CreditDebitIndicator: Literal["CRDT", "DBIT"]
    """CRDT (Deposit) or DBIT (Withdrawal)."""
    BookingDate: date | datetime | None
    """The date the transaction was booked to the ledger."""
    ValueDate: date | datetime | None
    """The date the transaction becomes effective for interest purposes."""
    ChargesAmount: Decimal | None
    """Any fees explicitly deducted by the bank. Safely isolated per-transaction during batch processing."""
    ChargesCurrency: str | None
    """The currency of the deducted charges."""

    # Secondary Foreign Financials (Only if a currency conversion happened)
    ForeignAmount: Decimal | None
    """The original instructed invoice/wire amount before FX conversion. Is always positive or zero."""
    ForeignCurrency: str | None
    """The original currency before FX conversion."""
    ExchangeRate: Decimal | None
    """The applied conversion rate."""

    # Parties & Channels
    CreditorName: str | None
    """The primary creditor counterparty name."""
    CreditorAccountIBAN: str | None
    """The creditor counterparty's IBAN."""
    CreditorAccountIdOther: str | None
    """The creditor counterparty's non-IBAN account identifier."""
    UltimateCreditorName: str | None
    """The ultimate creditor in the transaction chain (if paying on behalf of someone else)."""
    DebtorName: str | None
    """The primary debtor counterparty name."""
    DebtorAccountIBAN: str | None
    """The debtor counterparty's IBAN."""
    DebtorAccountIdOther: str | None
    """The debtor counterparty's non-IBAN account identifier."""
    UltimateDebtorName: str | None
    """The ultimate debtor in the transaction chain (if paying on behalf of someone else)."""
    CardPoiId: str | None
    """Point of Interaction (e.g., the store name for a POS terminal)."""
    CardPan: str | None
    """The masked card number used for the transaction."""

    # ISO & Proprietary Codes
    EntryDomainCode: str | None
    """ISO standard classification domain code at the Entry level (e.g., PMNT)."""
    EntryTransactionFamilyCode: str | None
    """ISO standard classification family code at the Entry level (e.g., ICDT)."""
    EntryTransactionSubFamilyCode: str | None
    """ISO standard classification sub-family code at the Entry level (e.g., STDO)."""
    EntryProprietaryTransactionCode: str | None
    """Bank-specific internal transaction code at the Entry level."""
    EntryReturnReasonCode: str | None
    """The ISO reason code if the entry bounced/reversed (e.g., AC01) at the Entry level."""
    EntryPurposeCode: str | None
    """The ISO category for the payment (e.g., SALA for Salary) at the Entry level."""
    EntryPurposeProprietary: str | None
    """A proprietary category for the payment at the Entry level."""
    DomainCode: str | None
    """ISO standard classification domain code (e.g., PMNT) at the TxDetails level."""
    TransactionFamilyCode: str | None
    """ISO standard classification family code (e.g., ICDT) at the TxDetails level."""
    TransactionSubFamilyCode: str | None
    """ISO standard classification sub-family code (e.g., DMCT) at the TxDetails level."""
    ProprietaryTransactionCode: str | None
    """Bank-specific internal transaction code at the TxDetails level."""
    ReturnReasonCode: str | None
    """The ISO reason code if the transaction bounced/reversed (e.g., AC01) at the TxDetails level."""
    PurposeCode: str | None
    """The ISO category for the payment (e.g., SALA for Salary) at the TxDetails level."""
    PurposeProprietary: str | None
    """A proprietary category for the payment at the TxDetails level."""

    # Text & Remittance
    AdditionalEntryInfo: str | None
    """Bank-provided contextual text at the entry level."""
    AdditionalTransactionInfo: str | None
    """Bank-provided contextual text at the transaction level."""
    UnstructuredRemittanceInfo: str | None
    """Free-text invoice description or payment message."""
    ReturnAdditionalInfo: str | None
    """Human-readable explanation of why a payment was reversed."""
    CreditorReference: str | None
    """Structured payment references (e.g., Swiss QR-Bill reference)."""
    DocumentReferenceNumber: str | None
    """Commercial invoice numbers passed through the structured block."""

    # Batch Metadata
    IsBatch: bool
    """True if this transaction was part of a bundled batch payment."""
    BatchIndex: int
    """Tracking number to identify the transaction's position within the batch (1-indexed)."""
    BatchTotal: int
    """The total number of transactions in the parent entry batch."""

    # Advanced Raw XML Payload Includes whole tree, but stripped of all elements which are not descendants or ancestors
    Advanced: XmlElementDict
    """A namespace-stripped, whitespace-normalized JSON representation of the exact XML path for this specific transaction."""


@dataclass(frozen=True)
class _StatementData:
    xml_element: ET._Element
    info: StatementInfo


@dataclass(frozen=True)
class _EntryData:
    statement: _StatementData
    xml_element: ET._Element
    info: EntryInfo


@dataclass(frozen=True)
class _TransactionData:
    entry: _EntryData
    xml_element: ET._Element
    info: TransactionInfo


@dataclass(frozen=True)
class _AmountDetails:
    Amount: Decimal | None
    Currency: str | None
    ForeignAmount: Decimal | None
    ForeignCurrency: str | None
    ExchangeRate: Decimal | None


@dataclass(frozen=True)
class _CurrencyExchangeDetails:
    SourceCurrency: str
    """Source currency of the exchange rate, e.g. 'EUR'."""
    TargetCurrency: str
    """Target currency of the exchange rate, e.g. 'CHF'."""
    ExchangeRate: Decimal
    """Exchange rate from target to source currency, e.g. 0.92 means 1 EUR = 0.92 CHF (source * rate = target)."""


class Camt053Parser:
    _tree: ET._ElementTree
    _root: ET._Element
    _root_namespace: str
    _nsmap: dict[str, str]
    _settings: Camt053ParserSettings

    def __init__(self, xml_tree: ET._ElementTree, settings: Camt053ParserSettings = Camt053ParserSettings()):
        self._tree = xml_tree
        self._root = self._tree.getroot()
        self._root_namespace = _extract_ns(self._root.tag)
        self._nsmap = {"ns": self._root_namespace}
        self._settings = settings

    @staticmethod
    def from_file(file_path: str | pathlib.PurePath, settings: Camt053ParserSettings = Camt053ParserSettings()) -> "Camt053Parser":
        """
        Factory method to create a Camt053Parser instance from a file path.
        """
        file_path = pathlib.Path(file_path)
        tree = ET.parse(file_path)
        return Camt053Parser(tree, settings=settings)

    def _get_statements(self) -> list[_StatementData]:
        ns = self._nsmap
        statements: list[_StatementData] = []
        for stmt_el in self._root.findall("./ns:BkToCstmrStmt/ns:Stmt", namespaces=ns):
            # get IDs first for better logging and error messages
            statement_id = _find_unique_elem_text(stmt_el, "./ns:Id", ns)
            statement_log_prefix = f"Statement '{statement_id or '<unknown>'}'"
            # Get opening and closing balances with currency
            opening_balance_elem = _find_unique_elem(stmt_el, "./ns:Bal[ns:Tp/ns:CdOrPrtry/ns:Cd='OPBD']/ns:Amt", ns)
            opening_amt, opening_ccy = _get_amount_and_currency(opening_balance_elem)
            closing_balance_elem = _find_unique_elem(stmt_el, "./ns:Bal[ns:Tp/ns:CdOrPrtry/ns:Cd='CLBD']/ns:Amt", ns)
            closing_amt, closing_ccy = _get_amount_and_currency(closing_balance_elem)
            # Get account currency with fallback to opening or closing balance if standard tag is missing
            account_ccy = _find_unique_elem_text(stmt_el, "./ns:Acct/ns:Ccy", ns)
            if not account_ccy:
                account_ccy = opening_ccy or closing_ccy
            if not account_ccy:
                raise ValueError(f"{statement_log_prefix}: failed to determine account currency")
            # get date / times
            creation_dt = _get_date_or_datetime_from_base_elem(stmt_el, ns, datetime_tag="CreDtTm", date_tag="CreDt")
            from_to_dt_elem = _find_unique_elem(stmt_el, "./ns:FrToDt", ns)
            from_dt = _get_date_or_datetime_from_base_elem(from_to_dt_elem, ns, datetime_tag="FrDtTm", date_tag="FrDt")
            to_dt = _get_date_or_datetime_from_base_elem(from_to_dt_elem, ns, datetime_tag="ToDtTm", date_tag="ToDt")
            # build the StatementInfo dict
            stmt_info = StatementInfo(
                StatementId=statement_id,
                LegalSequenceNumber=_find_unique_elem_text(stmt_el, "./ns:LglSeqNb", ns),
                ElectronicSequenceNumber=_find_unique_elem_text(stmt_el, "./ns:ElctrncSeqNb", ns),
                StatementCreationDate=creation_dt,
                FromDateTime=from_dt,
                ToDateTime=to_dt,
                AccountIBAN=_find_unique_elem_text(stmt_el, "./ns:Acct/ns:Id/ns:IBAN", ns),
                AccountIdOther=_find_unique_elem_text(stmt_el, "./ns:Acct/ns:Id/ns:Othr/ns:Id", ns),
                AccountCurrency=account_ccy,
                AccountOwner=_find_unique_elem_text(stmt_el, "./ns:Acct/ns:Ownr/ns:Nm", ns, normalize=True),
                OpeningBalance=opening_amt,
                ClosingBalance=closing_amt,
                Advanced=_elem_to_dict(stmt_el),
            )
            statements.append(_StatementData(xml_element=stmt_el, info=stmt_info))
        return statements

    def _get_entries_from_statement(self, statement_data: _StatementData) -> list[_EntryData]:
        ns = self._nsmap
        statement_elem = statement_data.xml_element
        statement = statement_data.info
        entries: list[_EntryData] = []
        for ntry_el in statement_elem.findall("./ns:Ntry", ns):
            # get IDs first for better logging and error messages
            entry_reference = _find_unique_elem_text(ntry_el, "./ns:NtryRef", ns)
            account_servicer_reference = _find_unique_elem_text(ntry_el, "./ns:AcctSvcrRef", ns)
            entry_log_prefix = f"Entry '{account_servicer_reference or entry_reference or '<unknown>'}'"
            # amount and foreign amount handling
            account_currency = statement.AccountCurrency
            amt_details = _get_amount_details_from_base_elem(ntry_el, account_currency, ns, self._settings)
            if amt_details.Currency != account_currency:
                log_currency = amt_details.Currency or amt_details.ForeignCurrency or "None"
                raise ValueError(f"{entry_log_prefix}: Currency {log_currency} does not match the account currency {account_currency}.")
            if not amt_details.Amount or not amt_details.Currency:
                raise ValueError(f"{entry_log_prefix} does not have a valid amount or currency.")
            credit_debit_indicator = _find_unique_elem_text(ntry_el, "./ns:CdtDbtInd", ns)
            if not credit_debit_indicator in ("CRDT", "DBIT"):
                raise ValueError(f"{entry_log_prefix} has an invalid <CdtDbtInd> '{credit_debit_indicator}'. Must be 'CRDT' or 'DBIT'.")
            # other data which is not directly mapped to the EntryInfo dict
            reversal_text = _find_unique_elem_text(ntry_el, "./ns:RvslInd", ns) or "false"
            reversal_indicator = reversal_text.lower() == "true"
            booking_date_elem = _find_unique_elem(ntry_el, "./ns:BookgDt", ns)
            booking_date = _get_date_or_datetime_from_base_elem(booking_date_elem, ns)
            value_date_elem = _find_unique_elem(ntry_el, "./ns:ValDt", ns)
            value_date = _get_date_or_datetime_from_base_elem(value_date_elem, ns)
            # charges
            charges_elem = _find_oneof_unique_elem(
                ntry_el, ["./ns:Chrgs/ns:TtlChrgsAndTaxAmt", "./ns:Chrgs/ns:Rcrd/ns:Amt", "./ns:Chrgs/ns:Amt"], ns
            )
            chrgs_amt, chrgs_ccy = _get_amount_and_currency(charges_elem)
            # Build XML tree dict -> overwrite Ntry list with only this
            entry_xml_dict = _elem_to_dict(ntry_el)
            statement_xml_dict = copy.deepcopy(statement.Advanced)
            statement_xml_dict.children["Ntry"] = [entry_xml_dict]
            # build the EntryInfo dict
            entry_info = EntryInfo(
                # Identifiers & References
                EntryReference=entry_reference,
                AccountServicerReference=account_servicer_reference,
                # Financial Details - Account / Ledger (always in Account Currency)
                Amount=amt_details.Amount,
                Currency=amt_details.Currency,
                CreditDebitIndicator=credit_debit_indicator,
                BookingDate=booking_date,
                ValueDate=value_date,
                ChargesAmount=chrgs_amt,
                ChargesCurrency=chrgs_ccy,
                # Secondary Foreign Financials (Only if a currency conversion happened)
                ForeignAmount=amt_details.ForeignAmount,
                ForeignCurrency=amt_details.ForeignCurrency,
                ExchangeRate=amt_details.ExchangeRate,
                # other metadata
                Status=_find_unique_elem_text(ntry_el, "./ns:Sts", ns),
                ReversalIndicator=reversal_indicator,
                AdditionalEntryInfo=_find_unique_elem_text(ntry_el, "./ns:AddtlNtryInf", ns, normalize=True),
                DomainCode=_find_unique_elem_text(ntry_el, "./ns:BkTxCd/ns:Domn/ns:Cd", ns),
                TransactionFamilyCode=_find_unique_elem_text(ntry_el, "./ns:BkTxCd/ns:Domn/ns:Fmly/ns:Cd", ns),
                TransactionSubFamilyCode=_find_unique_elem_text(ntry_el, "./ns:BkTxCd/ns:Domn/ns:Fmly/ns:SubFmlyCd", ns),
                ProprietaryTransactionCode=_find_unique_elem_text(ntry_el, "./ns:BkTxCd/ns:Prtry/ns:Cd", ns),
                ReturnReasonCode=_find_oneof_unique_elem_text(ntry_el, ["./ns:RtrInf/ns:Rsn/ns:Cd", "./ns:RtrInf/ns:Rsn/ns:Prtry"], ns),
                PurposeCode=_find_unique_elem_text(ntry_el, "./ns:Purp/ns:Cd", ns),
                PurposeProprietary=_find_unique_elem_text(ntry_el, "./ns:Purp/ns:Prtry", ns, normalize=True),
                CardPoiId=_find_unique_elem_text(ntry_el, "./ns:CardTx/ns:POI/ns:Id/ns:Id", ns),
                CardPan=_find_unique_elem_text(ntry_el, "./ns:CardTx/ns:Card/ns:PlainCardData/ns:PAN", ns),
                # Advanced Raw XML Payload Includes whole tree, but stripped of all elements which are not descendants or ancestors
                Advanced=statement_xml_dict,
            )
            entries.append(_EntryData(statement=statement_data, xml_element=ntry_el, info=entry_info))
        return entries

    def _get_entries_from_statements(self, statements: list[_StatementData]) -> list[_EntryData]:
        entries: list[_EntryData] = []
        for statement in statements:
            entries.extend(self._get_entries_from_statement(statement))
        return entries

    def _get_transaction_from_entry_without_txdetails(self, entry_data: _EntryData) -> _TransactionData:
        """
        Build transaction info directly from the entry when no TxDtls are present.
        This is used for simple entries that do not have individual transaction details.
        """
        entry = entry_data.info
        statement = entry_data.statement.info
        tx_info = TransactionInfo(
            # Statement Context
            AccountIBAN=statement.AccountIBAN,
            StatementId=statement.StatementId,
            # Identifiers & References
            EntryAccountServicerReference=entry.AccountServicerReference,
            TransactionAccountServicerReference=None,
            EntryReference=entry.EntryReference,
            PaymentInformationId=None,
            ClearingSystemReference=None,
            EndToEndId=None,
            InstructionId=None,
            MandateId=None,
            # Financial Details - Account / Ledger (Always present, always in Account Currency)
            Amount=entry.Amount,
            Currency=entry.Currency,
            CreditDebitIndicator=entry.CreditDebitIndicator,
            BookingDate=entry.BookingDate,
            ValueDate=entry.ValueDate,
            ChargesAmount=entry.ChargesAmount,
            ChargesCurrency=entry.ChargesCurrency,
            # Financial Details - Foreign / Instructed (Only populated when foreign currency is involved)
            ForeignAmount=entry.ForeignAmount,
            ForeignCurrency=entry.ForeignCurrency,
            ExchangeRate=entry.ExchangeRate,
            # Parties & Channels
            CreditorName=None,
            CreditorAccountIBAN=None,
            CreditorAccountIdOther=None,
            UltimateCreditorName=None,
            DebtorName=None,
            DebtorAccountIBAN=None,
            DebtorAccountIdOther=None,
            UltimateDebtorName=None,
            CardPoiId=entry.CardPoiId,
            CardPan=entry.CardPan,
            # ISO & Proprietary Codes
            EntryDomainCode=entry.DomainCode,
            EntryTransactionFamilyCode=entry.TransactionFamilyCode,
            EntryTransactionSubFamilyCode=entry.TransactionSubFamilyCode,
            EntryProprietaryTransactionCode=entry.ProprietaryTransactionCode,
            EntryReturnReasonCode=entry.ReturnReasonCode,
            EntryPurposeCode=entry.PurposeCode,
            EntryPurposeProprietary=entry.PurposeProprietary,
            DomainCode=None,
            TransactionFamilyCode=None,
            TransactionSubFamilyCode=None,
            ProprietaryTransactionCode=None,
            ReturnReasonCode=None,
            PurposeCode=None,
            PurposeProprietary=None,
            # Text & Remittance
            AdditionalEntryInfo=entry.AdditionalEntryInfo,
            AdditionalTransactionInfo=None,
            UnstructuredRemittanceInfo=None,
            ReturnAdditionalInfo=None,
            CreditorReference=None,
            DocumentReferenceNumber=None,
            # Batch Metadata & Advanced
            IsBatch=False,
            BatchIndex=1,
            BatchTotal=1,
            Advanced=copy.deepcopy(entry.Advanced),
        )
        tx_data = _TransactionData(
            entry=entry_data,
            xml_element=entry_data.xml_element,
            info=tx_info,
        )
        _validate_transaction_batch([tx_data], self._settings)
        return tx_data

    def _get_transactions_from_entry(self, entry_data: _EntryData) -> list[_TransactionData]:
        ns = self._nsmap
        statement = entry_data.statement.info
        entry_elem = entry_data.xml_element
        entry = entry_data.info
        entry_log_prefix = _get_entry_log_prefix(entry_data)
        tx_details_elements = entry_elem.findall("./ns:NtryDtls/ns:TxDtls", ns)
        # Simple entry with no TxDtls, use Entry level data
        if not tx_details_elements:
            tx_data = self._get_transaction_from_entry_without_txdetails(entry_data)
            return [tx_data]
        # check batch tags data
        batch_num_payments_text = _find_unique_elem_text(entry_elem, "./ns:NtryDtls/ns:Btch/ns:NbOfTxs", ns)
        batch_num_payments = int(batch_num_payments_text) if batch_num_payments_text else None
        num_tx_elements = len(tx_details_elements)
        if batch_num_payments is not None and batch_num_payments != num_tx_elements:
            raise ValueError(
                f"{entry_log_prefix} has a batch with {batch_num_payments} payments, but {num_tx_elements} TxDtls elements were found."
            )
        if num_tx_elements > 1 and not batch_num_payments:
            raise ValueError(
                f"{entry_log_prefix} has {num_tx_elements} TxDtls elements, but no batch information is present. Batch information is required for multiple transactions."
            )
        is_batch = num_tx_elements > 1
        # -- NORMAL FLOW: Parse individual TxDtls --
        transactions_data: list[_TransactionData] = []
        for idx, tx_el in enumerate(tx_details_elements):
            # get IDs first for better logging and error messages
            tx_account_servicer_ref = _find_unique_elem_text(tx_el, "./ns:Refs/ns:AcctSvcrRef", ns)
            tx_pmt_inf_id = _find_unique_elem_text(tx_el, "./ns:Refs/ns:PmtInfId", ns)
            tx_clr_sys_ref = _find_unique_elem_text(tx_el, "./ns:Refs/ns:ClrSysRef", ns)
            tx_end_to_end_id = _find_unique_elem_text(tx_el, "./ns:Refs/ns:EndToEndId", ns)
            tx_instruction_id = _find_unique_elem_text(tx_el, "./ns:Refs/ns:InstrId", ns)
            tx_mandate_id = _find_unique_elem_text(tx_el, "./ns:Refs/ns:MndtId", ns)
            tx_log_id = (
                tx_account_servicer_ref
                or tx_end_to_end_id
                or tx_instruction_id
                or tx_mandate_id
                or tx_pmt_inf_id
                or tx_clr_sys_ref
                or f"<idx-{idx + 1}>"
            )
            tx_log_prefix = f"{entry_log_prefix} Transaction '{tx_log_id}'"
            # Normalizing Unstructured Remittance info
            ustrd_raw = "\n".join([u.text.strip() for u in tx_el.findall("./ns:RmtInf/ns:Ustrd", ns) if u.text])
            ustrd_info = _normalize_info_text(ustrd_raw)
            # Extract Document/Invoice References (comma separated if multiple)
            doc_ref_elems = tx_el.findall("./ns:RmtInf/ns:Strd/ns:RfrdDocInf/ns:Nb", ns)
            doc_refs = [el.text.strip() for el in doc_ref_elems if el.text and el.text.strip()]
            doc_ref_info = ", ".join(doc_refs) if doc_refs else None
            # Get the transaction amount and currency, with fallback to Entry level if not present in TxDtls
            tx_amt_details = _get_amount_details_from_base_elem(tx_el, statement.AccountCurrency, ns, self._settings)
            if is_batch and (tx_amt_details.Amount is None or tx_amt_details.Currency is None):
                raise ValueError(
                    f"{tx_log_prefix} is part of a batch but has no amount or currency, which is required for batch transactions."
                )
            tx_amt = tx_amt_details.Amount or entry.Amount
            tx_ccy = tx_amt_details.Currency or entry.Currency
            tx_credit_debit_indicator = _find_unique_elem_text(tx_el, "./ns:CdtDbtInd", ns)
            if tx_credit_debit_indicator is not None and not tx_credit_debit_indicator in ("CRDT", "DBIT"):
                raise ValueError(
                    f"{tx_log_prefix} has an invalid CreditDebitIndicator '{tx_credit_debit_indicator}'. Must be 'CRDT' or 'DBIT'."
                )
            # Get charges from transaction details, with conditional fallback to Entry level if not present in TxDtls
            tx_charges_elem = _find_oneof_unique_elem(tx_el, ["./ns:Chrgs/ns:Amt", "./ns:Chrgs/ns:Rcrd/ns:Amt"], ns)
            tx_chrgs_amt, tx_chrgs_ccy = _get_amount_and_currency(tx_charges_elem)
            if not is_batch and tx_chrgs_amt is None:
                tx_chrgs_amt = entry.ChargesAmount
                tx_chrgs_ccy = entry.ChargesCurrency
            # Build XML tree dict -> overwrite Ntry list with only this
            tx_xml_dict = _elem_to_dict(tx_el)
            entry_xml_dict = copy.deepcopy(entry.Advanced)
            entry_xml_dict.children["Ntry"][0].children["TxDtls"] = [tx_xml_dict]
            # Build the TransactionInfo dict
            tx_info = TransactionInfo(
                # Statement Context
                AccountIBAN=statement.AccountIBAN,
                StatementId=statement.StatementId,
                # Identifiers & References
                EntryAccountServicerReference=entry.AccountServicerReference,
                TransactionAccountServicerReference=tx_account_servicer_ref,
                EntryReference=entry.EntryReference,
                PaymentInformationId=tx_pmt_inf_id,
                ClearingSystemReference=tx_clr_sys_ref,
                EndToEndId=tx_end_to_end_id,
                InstructionId=tx_instruction_id,
                MandateId=tx_mandate_id,
                # Financial Details - Account / Ledger (Always present, always in Account Currency)
                Amount=tx_amt,
                Currency=tx_ccy,
                CreditDebitIndicator=tx_credit_debit_indicator or entry.CreditDebitIndicator,
                BookingDate=entry.BookingDate,
                ValueDate=entry.ValueDate,
                ChargesAmount=tx_chrgs_amt,
                ChargesCurrency=tx_chrgs_ccy,
                # Financial Details - Foreign / Instructed (Only populated when foreign currency is involved)
                ForeignAmount=tx_amt_details.ForeignAmount or entry.ForeignAmount,
                ForeignCurrency=tx_amt_details.ForeignCurrency or entry.ForeignCurrency,
                ExchangeRate=tx_amt_details.ExchangeRate or entry.ExchangeRate,
                # Parties & Channels
                CreditorName=_find_unique_elem_text(tx_el, "./ns:RltdPties/ns:Cdtr/ns:Nm", ns, normalize=True),
                CreditorAccountIBAN=_find_unique_elem_text(tx_el, "./ns:RltdPties/ns:CdtrAcct/ns:Id/ns:IBAN", ns),
                CreditorAccountIdOther=_find_unique_elem_text(tx_el, "./ns:RltdPties/ns:CdtrAcct/ns:Id/ns:Othr/ns:Id", ns),
                UltimateCreditorName=_find_unique_elem_text(tx_el, "./ns:RltdPties/ns:UltmtCdtr/ns:Nm", ns, normalize=True),
                DebtorName=_find_unique_elem_text(tx_el, "./ns:RltdPties/ns:Dbtr/ns:Nm", ns, normalize=True),
                DebtorAccountIBAN=_find_unique_elem_text(tx_el, "./ns:RltdPties/ns:DbtrAcct/ns:Id/ns:IBAN", ns),
                DebtorAccountIdOther=_find_unique_elem_text(tx_el, "./ns:RltdPties/ns:DbtrAcct/ns:Id/ns:Othr/ns:Id", ns),
                UltimateDebtorName=_find_unique_elem_text(tx_el, "./ns:RltdPties/ns:UltmtDbtr/ns:Nm", ns, normalize=True),
                CardPoiId=_find_unique_elem_text(tx_el, "./ns:CardTx/ns:POI/ns:Id/ns:Id", ns) or entry.CardPoiId,
                CardPan=_find_unique_elem_text(tx_el, "./ns:CardTx/ns:Card/ns:PlainCardData/ns:PAN", ns) or entry.CardPan,
                # ISO & Proprietary Codes
                EntryDomainCode=entry.DomainCode,
                EntryTransactionFamilyCode=entry.TransactionFamilyCode,
                EntryTransactionSubFamilyCode=entry.TransactionSubFamilyCode,
                EntryProprietaryTransactionCode=entry.ProprietaryTransactionCode,
                EntryReturnReasonCode=entry.ReturnReasonCode,
                EntryPurposeCode=entry.PurposeCode,
                EntryPurposeProprietary=entry.PurposeProprietary,
                DomainCode=_find_unique_elem_text(tx_el, "./ns:BkTxCd/ns:Domn/ns:Cd", ns),
                TransactionFamilyCode=_find_unique_elem_text(tx_el, "./ns:BkTxCd/ns:Domn/ns:Fmly/ns:Cd", ns),
                TransactionSubFamilyCode=_find_unique_elem_text(tx_el, "./ns:BkTxCd/ns:Domn/ns:Fmly/ns:SubFmlyCd", ns),
                ProprietaryTransactionCode=_find_unique_elem_text(tx_el, "./ns:BkTxCd/ns:Prtry/ns:Cd", ns),
                ReturnReasonCode=_find_oneof_unique_elem_text(tx_el, ["./ns:RtrInf/ns:Rsn/ns:Cd", "./ns:RtrInf/ns:Rsn/ns:Prtry"], ns),
                PurposeCode=_find_unique_elem_text(tx_el, "./ns:Purp/ns:Cd", ns),
                PurposeProprietary=_find_unique_elem_text(tx_el, "./ns:Purp/ns:Prtry", ns, normalize=True),
                # Text & Remittance
                AdditionalEntryInfo=entry.AdditionalEntryInfo,
                AdditionalTransactionInfo=_find_unique_elem_text(tx_el, "./ns:AddtlTxInf", ns, normalize=True),
                UnstructuredRemittanceInfo=ustrd_info,
                ReturnAdditionalInfo=_find_unique_elem_text(tx_el, "./ns:RtrInf/ns:AddtlInf", ns, normalize=True),
                CreditorReference=_find_unique_elem_text(tx_el, "./ns:RmtInf/ns:Strd/ns:CdtrRefInf/ns:Ref", ns),
                DocumentReferenceNumber=doc_ref_info,
                # Batch Metadata & Advanced
                IsBatch=is_batch,
                BatchIndex=idx + 1,
                BatchTotal=num_tx_elements,
                Advanced=entry_xml_dict,
            )
            transactions_data.append(_TransactionData(entry=entry_data, xml_element=tx_el, info=tx_info))
        # result
        _validate_transaction_batch(transactions_data, self._settings)
        return transactions_data

    def _get_transactions_from_entries(self, entries_data: list[_EntryData]) -> list[_TransactionData]:
        transactions: list[_TransactionData] = []
        for entry in entries_data:
            transactions.extend(self._get_transactions_from_entry(entry))
        return transactions

    def get_transactions(self) -> list[TransactionInfo]:
        """
        Parses the CAMT.053 file and returns a clean, flat list of typed TransactionInfo dicts.
        """
        statements = self._get_statements()
        entries = self._get_entries_from_statements(statements)
        transactions = self._get_transactions_from_entries(entries)
        return [tx.info for tx in transactions]


def _extract_ns(tag: str) -> str:
    return tag.split("}", 1)[0].strip("{") if "}" in tag else ""


def _remove_ns(tag: str) -> str:
    return tag.split("}", 1)[-1] if "}" in tag else tag


def _find_unique_elem(elem: ET._Element, path: str, ns: dict, strip: bool = True) -> ET._Element | None:
    """
    Finds an element by full XPath
    The XPath must return a single element. If it returns multiple elements, an exception is raised.
    """
    found_data = elem.xpath(path, namespaces=ns)
    # xpath returns various types, including lists of elements, strings, or numbers depending on the XPath expression.
    # so we need to narrow it down to a single element and ensure it's a list of elements.
    if not isinstance(found_data, list):
        raise ValueError(f"Expected XPath '{path}' to return a list of nodes, but got {type(found_data).__name__}.")
    if not found_data:
        return None
    if len(found_data) > 1:
        raise ValueError(f"Expected a single element for path '{path}', but found {len(found_data)}.")
    if not isinstance(found_data[0], ET._Element):
        raise ValueError(f"Expected xpath result to be an element for path '{path}', but found type {type(found_data[0]).__name__}.")
    return found_data[0]


def _find_oneof_unique_elem(elem: ET._Element, possible_path: list[str], ns: dict, strip: bool = True) -> ET._Element | None:
    """
    Finds an element by one of the full XPath.
    This method allows for multiple possible paths to be provided, and will return the text of the first found element.
    Each XPath must return a single element. If it returns multiple elements, an exception is raised.
    """
    for path in possible_path:
        found_elem = _find_unique_elem(elem, path, ns, strip)
        if found_elem is not None:
            return found_elem
    return None


def _find_unique_elem_text(elem: ET._Element, path: str, ns: dict, strip: bool = True, normalize: bool = False) -> str | None:
    """
    Finds an element by full XPath and returns its text.
    The XPath must return a single element. If it returns multiple elements, an exception is raised.
    """
    found_elem = _find_unique_elem(elem, path, ns)
    if found_elem is None:
        return None
    text = found_elem.text
    if text is None:
        return None
    if normalize:
        return _normalize_info_text(text)
    return text.strip() if strip else text


def _find_oneof_unique_elem_text(
    elem: ET._Element, possible_path: list[str], ns: dict, strip: bool = True, normalize: bool = False
) -> str | None:
    """
    Finds an element by one of the full XPath and returns its text.
    This method allows for multiple possible paths to be provided, and will return the text of the first found element.
    Each XPath must return a single element. If it returns multiple elements, an exception is raised.
    """
    for path in possible_path:
        text = _find_unique_elem_text(elem, path, ns, strip=strip, normalize=normalize)
        if text is not None:
            return text
    return None


def _elem_to_dict(elem: ET._Element) -> XmlElementDict:
    """
    Recursively converts an lxml ElementTree into a namespace-stripped Python dictionary.
    """
    # Extract text
    # if the text is only whitespace, we will discard it and return None.
    # But if there is any non-whitespace text, we will keep it as-is without any stripping (lossless).
    raw_text = elem.text
    normalized_text = _normalize_info_text(raw_text)
    text = normalized_text if not normalized_text else raw_text
    # Extract attributes as a dictionary of strings
    attribs: dict[str, str] = {str(k): str(v) for k, v in elem.attrib.items()}
    # get children dicts and group them by tag name
    children_dict: dict[str, list[XmlElementDict]] = {}
    for child in elem.iterchildren(tag="*"):
        child_tag = _remove_ns(child.tag)
        if child_tag not in children_dict:
            # Initialize the list if the tag hasn't been seen yet, then append
            children_dict[child_tag] = []
        child_dict = _elem_to_dict(child)
        children_dict[child_tag].append(child_dict)
    # Resulting dictionary structure
    return XmlElementDict(
        text=text,
        attrib=attribs,
        children=children_dict,
    )


def _get_amount_and_currency(amt_elem: ET._Element | None) -> tuple[Decimal, str] | tuple[None, None]:
    """
    Extracts the amount and currency from an element.
    Returns a tuple of (amount, currency) or None if the amount element is not found.
    """
    if amt_elem is None:
        return (None, None)
    tag_name = _remove_ns(amt_elem.tag)
    if tag_name != "Amt":
        raise ValueError(f"Expected an 'Amt' element, but got '{tag_name}'.")
    amt_text = amt_elem.text.strip() if amt_elem.text else None
    amt_ccy = amt_elem.attrib.get("Ccy", "").strip()
    if not amt_text:
        raise ValueError(f"Element '{amt_elem.tag}' has an amount element with no text, which is invalid.")
    if not amt_ccy:
        raise ValueError(f"Element '{amt_elem.tag}' has no or empty currency attribute, which is invalid.")
    # Convert amount
    try:
        amt_decimal = Decimal(amt_text)
    except Exception as e:
        raise ValueError(f"Failed to convert amount '{amt_text}' to Decimal: {e}")
    # check not negative (not allowed in CAMT.053)
    if amt_decimal < Decimal("0"):
        raise ValueError(f"Element '{amt_elem.tag}' has a negative amount '{amt_decimal}', which is invalid.")
    # return
    return (amt_decimal, amt_ccy)


def _get_amount_details_from_base_elem(
    base_elem: ET._Element | None, account_currency: str, ns: dict, settings: Camt053ParserSettings
) -> _AmountDetails:
    """
    Extracts the amount, currency, foreign amount, foreign currency, and exchange rate from a given XML element.
    If the source element is None, all values will be None.

    @param base_elem: The XML element containing the amount details (<Ntry> or <TxDtls>).
    @param account_currency: The currency of the account, used to determine if a foreign currency is involved, and which element represents the base currency.
    @param ns: The namespace mapping for XPath queries.
    """
    if base_elem is None:
        return _AmountDetails(
            Amount=None,
            Currency=None,
            ForeignAmount=None,
            ForeignCurrency=None,
            ExchangeRate=None,
        )
    # Base Amount
    base_amt_el = _find_unique_elem(base_elem, "./ns:Amt", ns)
    base_amt, base_ccy = _get_amount_and_currency(base_amt_el)
    # Base exchange details - out of spec, but some banks put a CcyXchg directly on the Ntry or TxDtls element
    base_exchange_el = _find_unique_elem(base_elem, "./ns:CcyXchg", ns)
    base_exchange_details = _get_currency_exchange_details(base_exchange_el, ns)
    # InstdAmt Amount exchanged between the debtor and creditor (invoice amount).
    instructed_amt_el = _find_unique_elem(base_elem, "./ns:AmtDtls/ns:InstdAmt/ns:Amt", ns)
    instructed_amt, instructed_ccy = _get_amount_and_currency(instructed_amt_el)
    instructed_exchange_el = _find_unique_elem(base_elem, "./ns:AmtDtls/ns:InstdAmt/ns:CcyXchg", ns)
    instructed_exchange_details = _get_currency_exchange_details(instructed_exchange_el, ns)
    # TxAmt Amount exchanged between the financial institutions involved (credit amount).
    tx_amt_el = _find_unique_elem(base_elem, "./ns:AmtDtls/ns:TxAmt/ns:Amt", ns)
    tx_amt, tx_ccy = _get_amount_and_currency(tx_amt_el)
    tx_exchange_el = _find_unique_elem(base_elem, "./ns:AmtDtls/ns:TxAmt/ns:CcyXchg", ns)
    tx_exchange_details = _get_currency_exchange_details(tx_exchange_el, ns)
    # CntrValAmt
    cntr_val_amt_el = _find_unique_elem(base_elem, "./ns:AmtDtls/ns:CntrValAmt/ns:Amt", ns)
    cntr_val_amt, cntr_val_ccy = _get_amount_and_currency(cntr_val_amt_el)
    cntr_val_exchange_el = _find_unique_elem(base_elem, "./ns:AmtDtls/ns:CntrValAmt/ns:CcyXchg", ns)
    cntr_val_exchange_details = _get_currency_exchange_details(cntr_val_exchange_el, ns)
    # --- AMOUNT SELECTION LOGIC ---
    # Determine Primary Ledger Amount (MUST match account_currency)
    # Order of precedence: CntrValAmt > base_amt > tx_amt > instructed_amt
    ledger_amt = None
    ledger_ccy = None
    if cntr_val_amt is not None and cntr_val_ccy == account_currency:
        ledger_amt, ledger_ccy = cntr_val_amt, cntr_val_ccy
    elif base_amt is not None and base_ccy == account_currency:
        ledger_amt, ledger_ccy = base_amt, base_ccy
    elif tx_amt is not None and tx_ccy == account_currency:
        ledger_amt, ledger_ccy = tx_amt, tx_ccy
    elif instructed_amt is not None and instructed_ccy == account_currency:
        ledger_amt, ledger_ccy = instructed_amt, instructed_ccy
    # Determine Foreign Amount (MUST NOT match account_currency)
    # Order of precedence: instructed_amt (Invoice) > tx_amt (Wire) > base_amt > cntr_val_amt
    foreign_amt = None
    foreign_ccy = None
    if instructed_amt is not None and instructed_ccy != account_currency:
        foreign_amt, foreign_ccy = instructed_amt, instructed_ccy
    elif tx_amt is not None and tx_ccy != account_currency:
        foreign_amt, foreign_ccy = tx_amt, tx_ccy
    elif base_amt is not None and base_ccy != account_currency:
        foreign_amt, foreign_ccy = base_amt, base_ccy
    elif cntr_val_amt is not None and cntr_val_ccy != account_currency:
        foreign_amt, foreign_ccy = cntr_val_amt, cntr_val_ccy
    # Determine Exchange Rate
    # Order of precedence: CntrValAmt > TxAmt > InstdAmt > BaseAmt
    xchg_rate = None
    if cntr_val_exchange_details:
        xchg_rate = cntr_val_exchange_details.ExchangeRate
    elif tx_exchange_details:
        xchg_rate = tx_exchange_details.ExchangeRate
    elif instructed_exchange_details:
        xchg_rate = instructed_exchange_details.ExchangeRate
    elif base_exchange_details:
        xchg_rate = base_exchange_details.ExchangeRate
    # If no explicit exchange rate is provided, but both foreign and ledger amounts are present, we can calculate the exchange rate.
    if xchg_rate is None and foreign_amt is not None and ledger_amt is not None:
        # If no explicit exchange rate is provided, we can calculate it from the foreign and ledger amounts.
        try:
            xchg_rate = ledger_amt / foreign_amt
        except Exception as e:
            raise ValueError(
                f"Failed to calculate exchange rate from foreign amount {foreign_amt} {foreign_ccy} and ledger amount {ledger_amt} {ledger_ccy}: {e}"
            )
    # Check if the exchange rate must be inverted. According to the ISO spec this should not happen, but some banks do it anyway...
    if xchg_rate is not None and foreign_amt is not None and ledger_amt is not None:
        # we expect foreign * rate = ledger
        if (foreign_amt > ledger_amt) and (xchg_rate > Decimal("1")):
            logger.warning(
                f"Exchange rate inverted by heuristic: foreign_amt={foreign_amt}, ledger_amt={ledger_amt}, stated_rate={xchg_rate}"
            )
            xchg_rate = Decimal("1") / xchg_rate
        if (foreign_amt < ledger_amt) and (xchg_rate < Decimal("1")):
            # TODO how to best log from libary code? In an application I would just log a warning...
            logger.warning(f"DEBUG EXCHANGE RATE INVERSION: foreign_amt={foreign_amt}, ledger_amt={ledger_amt}, xchg_rate={xchg_rate}")
            xchg_rate = Decimal("1") / xchg_rate
    # build and validate the result
    result = _AmountDetails(
        Amount=ledger_amt,
        Currency=ledger_ccy,
        ForeignAmount=foreign_amt,
        ForeignCurrency=foreign_ccy,
        ExchangeRate=xchg_rate,
    )
    _validate_amount_details(result, settings, check_completeness=False)
    return result


def _validate_amount_details(amt_details: _AmountDetails, settings: Camt053ParserSettings, check_completeness: bool) -> None:
    """
    Validates the amount details to ensure that the ledger and foreign amounts and currencies are consistent.
    Raises ValueError if any inconsistencies are found.
    """
    ledger_amt = amt_details.Amount
    ledger_ccy = amt_details.Currency
    foreign_amt = amt_details.ForeignAmount
    foreign_ccy = amt_details.ForeignCurrency
    xchg_rate = amt_details.ExchangeRate
    if (ledger_amt is None and ledger_ccy is not None) or (ledger_amt is not None and ledger_ccy is None):
        raise ValueError(
            f"Ledger amount and currency must both be present or both be None. Found: Amount={ledger_amt}, Currency={ledger_ccy}"
        )
    if (foreign_amt is None and foreign_ccy is not None) or (foreign_amt is not None and foreign_ccy is None):
        raise ValueError(
            f"Foreign amount and currency must both be present or both be None. Found: Amount={foreign_amt}, Currency={foreign_ccy}"
        )
    if ledger_ccy is not None and foreign_ccy is not None and ledger_ccy == foreign_ccy:
        raise ValueError(
            f"Ledger currency {ledger_ccy} and foreign currency {foreign_ccy} must be different. If they are the same, there is no foreign exchange involved."
        )
    # Validate that the exchange rate is consistent with the amounts
    if ledger_amt is not None and foreign_amt is not None and xchg_rate is not None:
        try:
            calculated_amt = foreign_amt * xchg_rate
            exchange_error = abs(calculated_amt - ledger_amt)
            if exchange_error > settings.exchange_rate_result_tolerance:  # amounts usually round to 2 decimal places, so allow
                raise ValueError(
                    f"Exchange rate error too big. {foreign_amt}{foreign_ccy} * {xchg_rate} = {calculated_amt}{ledger_ccy}, which differs from the ledger amount {ledger_amt}{ledger_ccy} by more than the allowed tolerance of {settings.exchange_rate_result_tolerance}."
                )
        except Exception as e:
            raise
    # Validate that all amounts are positive (CAMT.053 does not allow negative amounts)
    if ledger_amt is not None and ledger_amt < Decimal("0"):
        raise ValueError(f"Ledger amount {ledger_amt} {ledger_ccy} is negative, which is invalid in CAMT.053.")
    if foreign_amt is not None and foreign_amt < Decimal("0"):
        raise ValueError(f"Foreign amount {foreign_amt} {foreign_ccy} is negative, which is invalid in CAMT.053.")
    # Optionally check for completeness: if any of the foreign amount, foreign currency, or exchange rate is present, all must be present.
    if not check_completeness:
        return
    if (foreign_amt is not None and foreign_ccy is not None) and xchg_rate is None:
        raise ValueError(f"Foreign amount {foreign_amt} {foreign_ccy} is present, but no exchange rate could be determined.")
    if (foreign_amt is None and foreign_ccy is None) and xchg_rate is not None:
        raise ValueError(f"Exchange rate {xchg_rate} is present, but no foreign amount or currency could be determined.")


def _get_currency_exchange_details(exchange_elem: ET._Element | None, ns: dict) -> _CurrencyExchangeDetails | None:
    """
    Extracts the source currency, target currency, and exchange rate from a CcyXchg element.
    Returns a CurrencyExchangeDetails dict or None if the input element is None.
    Raises ValueError if the element is not a CcyXchg element or if required sub-elements are missing.
    """
    # basic element checks
    if exchange_elem is None:
        return None
    tag_name = _remove_ns(exchange_elem.tag)
    if tag_name != "CcyXchg":
        raise ValueError(f"Expected a 'CcyXchg' element, but got '{tag_name}'.")
    # get and check currencies
    source_ccy = _find_unique_elem_text(exchange_elem, "./ns:SrcCcy", ns)
    if not source_ccy:
        raise ValueError("CcyXchg element is missing required 'SrcCcy' sub-element or it is empty.")
    target_ccy = _find_unique_elem_text(exchange_elem, "./ns:TrgtCcy", ns)
    if not target_ccy:
        # this is not mandatory in the spec, but it is required for our use case.
        raise ValueError("CcyXchg element is missing required 'TrgtCcy' sub-element or it is empty.")
    unit_ccy = _find_unique_elem_text(exchange_elem, "./ns:UnitCcy", ns)
    unit_ccy = unit_ccy or target_ccy  # According to the spec, if UnitCcy is missing, it is same as TrgtCcy.
    # Determine if the exchange rate needs to be inverted based on the UnitCcy
    if unit_ccy == target_ccy:
        invert_exchange = False
    elif unit_ccy == source_ccy:
        invert_exchange = True
    else:
        # I don't think this is a valid case, so for now, we will raise an error.
        raise ValueError(
            f"CcyXchg element 'UnitCcy' value '{unit_ccy}' does not match either the 'SrcCcy' value '{source_ccy}' or the 'TrgtCcy' value '{target_ccy}'."
        )
    # get and normalize exchange rate
    exch_rate_text = _find_unique_elem_text(exchange_elem, "./ns:XchgRate", ns)
    if not exch_rate_text:
        raise ValueError("CcyXchg element is missing required 'XchgRate' sub-element or it is empty.")
    try:
        exch_rate_stated = Decimal(exch_rate_text)
    except Exception as e:
        raise ValueError(f"Failed to convert exchange rate '{exch_rate_text}' to Decimal: {e}")
    exch_rate = exch_rate_stated if not invert_exchange else Decimal("1") / exch_rate_stated
    # return the details
    return _CurrencyExchangeDetails(
        SourceCurrency=source_ccy,
        TargetCurrency=target_ccy,
        ExchangeRate=exch_rate,
    )


def _get_date_or_datetime_from_base_elem(
    elem: ET._Element | None, ns: dict, datetime_tag: str | None = "DtTm", date_tag: str | None = "Dt"
) -> date | datetime | None:
    """
    Extracts a date or datetime from an element.
    For elements such as BkngDt or ValDt, you can use the default tags of DtTm and Dt. For other elements, you can specify the tags to use.
    If the input element is None, None is returned (good for optional elements).
    If both datetime and date tags are present, an exception is raised.
    If neither is present, an exception is raised.
    """
    if elem is None:
        return None
    # get elements and validate that only one of them is present
    datetime_elem = _find_unique_elem(elem, f"./ns:{datetime_tag}", ns) if datetime_tag else None
    date_elem = _find_unique_elem(elem, f"./ns:{date_tag}", ns) if date_tag else None
    if datetime_elem is not None and date_elem is not None:
        raise ValueError(f"Element '{elem.tag}' has both '<{datetime_tag}>' and '<{date_tag}>' sub-elements, which is invalid.")
    # parse datetime if available
    if datetime_elem is not None:
        datetime_text = (datetime_elem.text or "").strip()
        if not datetime_text:
            raise ValueError(f"Element '<{datetime_elem.tag}>' has no text, which is invalid.")
        try:
            return datetime.fromisoformat(datetime_text)
        except ValueError as e:
            raise ValueError(f"Failed to parse datetime '{datetime_text}' from element '<{datetime_elem.tag}>': {e}")
    # parse date if available
    if date_elem is not None:
        date_text = (date_elem.text or "").strip()
        if not date_text:
            raise ValueError(f"Element '<{date_elem.tag}>' has no text, which is invalid.")
        try:
            return date.fromisoformat(date_text)
        except ValueError as e:
            raise ValueError(f"Failed to parse date '{date_text}' from element '<{date_elem.tag}>': {e}")
    # If neither is present on a date element, this is invalid according to the spec
    raise ValueError(f"Element '{elem.tag}' has neither a '<{datetime_tag}>' nor a '<{date_tag}>' sub-element, which is invalid.")


def _validate_transaction(tx_data: _TransactionData, settings: Camt053ParserSettings) -> None:
    """
    Validates the transaction info to ensure that required fields are present and consistent.
    Please call _validate_transaction_batch for validation, as it will also check entry consistency and batch totals.
    Raises ValueError if any inconsistencies are found.
    """
    statement = tx_data.entry.statement.info
    entry = tx_data.entry.info
    tx = tx_data.info
    tx_log_prefix = _get_tx_log_prefix(tx_data)
    # validate amounts and currencies
    if tx.Currency != statement.AccountCurrency:
        raise ValueError(f"{tx_log_prefix}: Currency ({tx.Currency}) does not match the account currency ({statement.AccountCurrency}).")
    if tx.Currency != entry.Currency:
        raise ValueError(f"{tx_log_prefix}: Currency ({tx.Currency}) does not match the entry currency ({entry.Currency}).")
    amt_details = _AmountDetails(
        Amount=tx.Amount,
        Currency=tx.Currency,
        ForeignAmount=tx.ForeignAmount,
        ForeignCurrency=tx.ForeignCurrency,
        ExchangeRate=tx.ExchangeRate,
    )
    _validate_amount_details(amt_details, settings=settings, check_completeness=True)


def _validate_transaction_batch(transactions_data: list[_TransactionData], settings: Camt053ParserSettings) -> None:
    """
    Validates a batch of transactions to ensure that all transactions in the batch are valid and consistent with the entry they belong to.
    This checks the single transactions as well as the batch consistency, including the sum of the transaction amounts, the currencies,
    and the uniqueness of the TransactionAccountServicerReference.

    Raises ValueError if any inconsistencies are found.
    """
    if len(transactions_data) < 1:
        raise ValueError("Transaction batch validation requires at least one transaction.")
    entry_data = transactions_data[0].entry
    entry = entry_data.info
    entry_log_prefix = _get_entry_log_prefix(entry_data)
    # prepare values for total batch validation
    seen_tx_acct_svcr_refs: set[str] = set()
    tx_total_amt = Decimal("0")
    # Validate each transaction in the batch
    for tx_data in transactions_data:
        _validate_transaction(tx_data, settings=settings)
        tx = tx_data.info
        tx_log_prefix = _get_tx_log_prefix(tx_data)
        # If we mess up the entry reference, we want to catch it here and raise an error.
        if tx_data.entry is not entry_data:
            raise ValueError(f"{tx_log_prefix}: belongs to a different entry than the first batch transaction.")
        # Building sum
        if tx.CreditDebitIndicator == entry.CreditDebitIndicator:
            tx_total_amt += tx.Amount
        else:
            tx_total_amt -= tx.Amount
        # Validate unique TransactionAccountServicerReference for each transaction in a batch
        tx_asr = tx.TransactionAccountServicerReference
        if tx_asr is not None:
            if tx_asr in seen_tx_acct_svcr_refs:
                raise ValueError(f"{tx_log_prefix}: reused the AccountServicerReference '{tx_asr}', which must be unique within a batch.")
            seen_tx_acct_svcr_refs.add(tx_asr)
    # Sum Validation
    if tx_total_amt != entry.Amount:
        raise ValueError(
            f"{entry_log_prefix}: The sum of batch transaction amounts ({tx_total_amt}) is not equal to the entry amount ({entry.Amount})."
        )


def _normalize_info_text(raw_text: str | None) -> str | None:
    if raw_text is None:
        return None
    if not raw_text.strip():
        return None
    raw_lines = raw_text.splitlines()
    normalized_lines = [line.strip() for line in raw_lines if line.strip()]
    if not normalized_lines:
        return None
    return " ".join(normalized_lines)


def _get_tx_log_prefix(tx_data: _TransactionData) -> str:
    """
    Generates an identifier for log messages, based on the entry and transaction references. If no references are available, it falls back to using the batch index.
    This is useful for logging and error messages to identify a transaction within an entry.
    """
    entry_prefix = _get_entry_log_prefix(tx_data.entry)
    tx = tx_data.info
    tx_id = tx.TransactionAccountServicerReference or tx.EndToEndId or tx.InstructionId or tx.MandateId or f"<idx={tx.BatchIndex}>"
    return f"{entry_prefix}, Transaction '{tx_id}'"


def _get_entry_log_prefix(entry_data: _EntryData) -> str:
    """
    Generates an identifier for log messages, based on the entry references. If no references are available, it falls back to using the entry index.
    This is useful for logging and error messages to identify an entry within a statement.
    """
    entry = entry_data.info
    entry_id = entry.AccountServicerReference or entry.EntryReference or "<unknown>"
    return f"Entry '{entry_id}'"
