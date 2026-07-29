# TransactionInfo Data Dictionary

The `Camt053Parser.get_transactions()` method returns a flat list of `TransactionInfo` dictionaries. This schema collapses the deep XML hierarchy (`Statement` -> `Entry` -> `Transaction Details`) into a single, comprehensive record.

## Statement Context

- **`StatementId`**: The ID of the parent statement.
  - _Source:_ `<Stmt>/<Id>`
- **`AccountIBAN`**: The IBAN of the ledger account.
  - _Source:_ `<Stmt>/<Acct>/<Id>/<IBAN>`

## Identifiers & References

- **`EntryAccountServicerReference`**: The bank's internal reference for the Entry.
  - _Source:_ `<Ntry>/<AcctSvcrRef>`
- **`TransactionAccountServicerReference`**: The bank's internal reference for the specific transaction (if provided, it is unique within a batch in this parser).
  - _Source:_ `<TxDtls>/<Refs>/<AcctSvcrRef>`
- **`EntryReference`**: The primary reference of the Entry.
  - _Source:_ `<Ntry>/<NtryRef>`
- **`PaymentInformationId`**: The ID of the payment batch/instruction provided by the initiating system.
  - _Source:_ `<TxDtls>/<Refs>/<PmtInfId>`
- **`ClearingSystemReference`**: The central bank or clearing system trace ID.
  - _Source:_ `<TxDtls>/<Refs>/<ClrSysRef>`
- **`EndToEndId`**: The End-to-End tracking ID provided by the initiator.
  - _Source:_ `<TxDtls>/<Refs>/<EndToEndId>`
- **`InstructionId`**: Point-to-point reference assigned by the instructing party.
  - _Source:_ `<TxDtls>/<Refs>/<InstrId>`
- **`MandateId`**: Direct Debit mandate identifier.
  - _Source:_ `<TxDtls>/<Refs>/<MndtId>`

## Financial Details (Ledger)

- **`Amount`**: The final settled amount applied to the ledger.
  - _Source:_ Fallback hierarchy matching the account currency: `<AmtDtls>/<CntrValAmt>/<Amt>` → `<Ntry>/<Amt>` → `<AmtDtls>/<TxAmt>/<Amt>` → `<AmtDtls>/<InstdAmt>/<Amt>`
- **`Currency`**: The currency of the ledger account.
  - _Source:_ Sourced alongside `Amount` via the `Ccy` attribute.
- **`CreditDebitIndicator`**: `CRDT` (Deposit) or `DBIT` (Withdrawal).
  - _Source:_ `<Ntry>/<CdtDbtInd>`
- **`BookingDate`**: The date the transaction was booked to the ledger.
  - _Source:_ `<Ntry>/<BookgDt>`
- **`ValueDate`**: The date the transaction becomes effective for interest purposes.
  - _Source:_ `<Ntry>/<ValDt>`
- **`ChargesAmount` / `ChargesCurrency`**: Any fees explicitly deducted by the bank. Safely isolated per-transaction during batch processing.
  - _Source:_ `<TxDtls>/<Chrgs>/<Amt>` or `<TxDtls>/<Chrgs>/<Rcrd>/<Amt>` (Falls back to `<Ntry>/<Chrgs>` if not a batch).

## Foreign Exchange

_(Populated only if a currency conversion occurred)_

- **`ForeignAmount` / `ForeignCurrency`**: The original instructed invoice/wire amount before FX conversion.
  - _Source:_ The amount block whose `Ccy` attribute differs from the account currency (usually `<InstdAmt>` or `<TxAmt>`).
- **`ExchangeRate`**: The applied conversion rate. The exchange rate is always using the convention `foreign * rate = account`.
  - _Source:_ Extracted from the `<CcyXchg>` block of the matched amount, or calculated mathematically if missing.

## Parties & Channels

- **`CreditorName`**: The primary creditor counterparty name.
  - _Source:_ `<TxDtls>/<RltdPties>/<Cdtr>/<Nm>`
- **`CreditorAccountIBAN`**: The creditor counterparty's IBAN.
  - _Source:_ `<TxDtls>/<RltdPties>/<CdtrAcct>/<Id>/<IBAN>`
- **`CreditorAccountIdOther`**: The creditor counterparty's non-IBAN account identifier.
  - _Source:_ `<TxDtls>/<RltdPties>/<CdtrAcct>/<Id>/<Othr>/<Id>`
- **`UltimateCreditorName`**: The ultimate creditor in the transaction chain.
  - _Source:_ `<TxDtls>/<RltdPties>/<UltmtCdtr>/<Nm>`
- **`DebtorName`**: The primary debtor counterparty name.
  - _Source:_ `<TxDtls>/<RltdPties>/<Dbtr>/<Nm>`
- **`DebtorAccountIBAN`**: The debtor counterparty's IBAN.
  - _Source:_ `<TxDtls>/<RltdPties>/<DbtrAcct>/<Id>/<IBAN>`
- **`DebtorAccountIdOther`**: The debtor counterparty's non-IBAN account identifier.
  - _Source:_ `<TxDtls>/<RltdPties>/<DbtrAcct>/<Id>/<Othr>/<Id>`
- **`UltimateDebtorName`**: The ultimate debtor in the transaction chain.
  - _Source:_ `<TxDtls>/<RltdPties>/<UltmtDbtr>/<Nm>`
- **`CardPoiId`**: Point of Interaction (e.g., the store name for a POS terminal).
  - _Source:_ `<TxDtls>/<CardTx>/<POI>/<Id>/<Id>` (Falls back to `<Ntry>`)
- **`CardPan`**: The masked card number used for the transaction.
  - _Source:_ `<TxDtls>/<CardTx>/<Card>/<PlainCardData>/<PAN>` (Falls back to `<Ntry>`)

## ISO & Proprietary Codes

- **`DomainCode`**: ISO standard classification domain code (e.g., `PMNT`).
  - _Source:_ `<TxDtls>/<BkTxCd>/<Domn>/<Cd>` (Falls back to `<Ntry>`)
- **`TransactionFamilyCode`**: ISO standard classification family code (e.g., `ICDT`).
  - _Source:_ `<TxDtls>/<BkTxCd>/<Domn>/<Fmly>/<Cd>` (Falls back to `<Ntry>`)
- **`TransactionSubFamilyCode`**: ISO standard classification sub-family code (e.g., `DMCT`).
  - _Source:_ `<TxDtls>/<BkTxCd>/<Domn>/<Fmly>/<SubFmlyCd>` (Falls back to `<Ntry>`)
- **`ProprietaryTransactionCode`**: Bank-specific internal transaction code.
  - _Source:_ `<TxDtls>/<BkTxCd>/<Prtry>/<Cd>`
- **`ReturnReasonCode`**: The ISO reason code if the transaction bounced/reversed (e.g., `AC01`).
  - _Source:_ `<TxDtls>/<RtrInf>/<Rsn>/<Cd>` or `<Prtry>`
- **`PurposeCode`**: The ISO category for the payment (e.g., `SALA` for Salary).
  - _Source:_ `<TxDtls>/<Purp>/<Cd>`
- **`PurposeProprietary`**: A proprietary category for the payment.
  - _Source:_ `<TxDtls>/<Purp>/<Prtry>`

## Text & Remittance

- **`AdditionalEntryInfo`**: Bank-provided contextual text at the entry level.
  - _Source:_ `<Ntry>/<AddtlNtryInf>`
- **`AdditionalTransactionInfo`**: Bank-provided contextual text at the transaction level.
  - _Source:_ `<TxDtls>/<AddtlTxInf>`
- **`UnstructuredRemittanceInfo`**: Free-text invoice description or payment message.
  - _Source:_ `<TxDtls>/<RmtInf>/<Ustrd>` (Concatenated if multiple exist)
- **`ReturnAdditionalInfo`**: Human-readable explanation of why a payment was reversed.
  - _Source:_ `<TxDtls>/<RtrInf>/<AddtlInf>`
- **`CreditorReference`**: Structured payment references (e.g., Swiss QR-Bill reference).
  - _Source:_ `<TxDtls>/<RmtInf>/<Strd>/<CdtrRefInf>/<Ref>`
- **`DocumentReferenceNumber`**: Commercial invoice numbers.
  - _Source:_ `<TxDtls>/<RmtInf>/<Strd>/<RfrdDocInf>/<Nb>`

## Batch Metadata

- **`IsBatch`**: `True` if this transaction was part of a bundled batch payment.
  - _Source:_ Derived by checking if `<Ntry>` contains multiple `<TxDtls>`.
- **`BatchIndex`**: Tracking number to identify the transaction's position within the batch.
  - _Source:_ `1`-indexed loop counter inside `<NtryDtls>`.
- **`BatchTotal`**: The total number of transactions in the parent entry batch.
  - _Source:_ Total count of `<TxDtls>` elements.

## Advanced Raw Payload

- **`Advanced`**: A namespace-stripped, whitespace-normalized JSON representation of the exact XML path for this specific transaction.
  - _Source:_ Derived via `_elem_to_dict()` recursive parsing of the `<Stmt>` and `<Ntry>` nodes.
