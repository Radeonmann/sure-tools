# TransactionInfo Data Dictionary

The `Camt053Parser.get_transactions()` method returns a flat list of `TransactionInfo` dictionaries. This schema collapses the deep XML hierarchy (`Statement` -> `Entry` -> `Transaction Details`) into a single, comprehensive record.

## Entry level / transaction details level

Even though we flatten the XML hierarchy into a single flat dict, we still provide many fields twice, once with an entry prefix and once without. The two fields repreent the value which was set on entry level and the value which was set on transaction level. The reason for this is, that otherwise information may get lost, and as a consumer I also may not know where the data originated.

One example are the transaction codes (DomainCode - TransactionFamilyCode - TransactionSubFamilyCode). If I have a standing order in my private bank statements, I get the codes `PMNT-ICDT-STDO` on Ntry level. But for the same transaction, I get `PMNT-ICDT-DMCT` on the TxDtls level. The bank does this to say: "This whole batch is a standing order (`STDO`), but this specific line item was executed as a domestic credit transfer (`DMCT`)." This also means, that with only the TxDtls codes, we would lose important information.

As our philisophy is a transparent parser with clear sources for each field, we also do not automatically inherit the fields from the entry level for the values which we state for both levels. It means if the XML e.g. has a value for DomainCode on the Ntry, but no TxDtls element, our field DomainCode will be `None` and only EntryDomainCode will be set. This allows clear decisions on the consumer side. The minor disadvantage is, that the consumer select the field themselves if they simply want one value. But this is trivial code, e.g.:

```python
domain_code = camt_tx.DomainCode or camt_tx.EntryDomainCode
```

## Statement Context

- **`StatementId`**: The ID of the parent statement.
  - _Source:_ `<Stmt>/<Id>`
- **`AccountIBAN`**: The IBAN of the ledger account.
  - _Source:_ `<Stmt>/<Acct>/<Id>/<IBAN>`

## Identifiers & References

- **`EntryAccountServicerReference`**: The bank's internal reference for the Entry (Ntry).
  - _Source:_ `<Ntry>/<AcctSvcrRef>`
- **`TransactionAccountServicerReference`**: The bank's internal reference for the specific transaction (TxDtls) (if provided, it is unique within a batch in this parser).
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

- **`Amount`**: The final settled amount applied to the ledger. Is always positive or zero.
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

- **`ForeignAmount` / `ForeignCurrency`**: The original instructed invoice/wire amount before FX conversion. Is always positive or zero.
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

- **`EntryDomainCode`**: ISO standard classification domain code at the Entry level (e.g., `PMNT`).
  - _Source:_ `<Ntry>/<BkTxCd>/<Domn>/<Cd>`
- **`EntryTransactionFamilyCode`**: ISO standard classification family code at the Entry level (e.g., `ICDT`).
  - _Source:_ `<Ntry>/<BkTxCd>/<Domn>/<Fmly>/<Cd>`
- **`EntryTransactionSubFamilyCode`**: ISO standard classification sub-family code at the Entry level (e.g., `STDO`).
  - _Source:_ `<Ntry>/<BkTxCd>/<Domn>/<Fmly>/<SubFmlyCd>`
- **`EntryProprietaryTransactionCode`**: Bank-specific internal transaction code at the Entry level.
  - _Source:_ `<Ntry>/<BkTxCd>/<Prtry>/<Cd>`
- **`EntryReturnReasonCode`**: The ISO reason code if the entry bounced/reversed (e.g., `AC01`) at the Entry level.
  - _Source:_ `<Ntry>/<RtrInf>/<Rsn>/<Cd>` or `<Prtry>`
- **`EntryPurposeCode`**: The ISO category for the payment (e.g., `SALA` for Salary) at the Entry level.
  - _Source:_ `<Ntry>/<Purp>/<Cd>`
- **`EntryPurposeProprietary`**: A proprietary category for the payment at the Entry level.
  - _Source:_ `<Ntry>/<Purp>/<Prtry>`
- **`DomainCode`**: ISO standard classification domain code (e.g., `PMNT`) at the TxDetails level.
  - _Source:_ `<TxDtls>/<BkTxCd>/<Domn>/<Cd>`
- **`TransactionFamilyCode`**: ISO standard classification family code (e.g., `ICDT`) at the TxDetails level.
  - _Source:_ `<TxDtls>/<BkTxCd>/<Domn>/<Fmly>/<Cd>`
- **`TransactionSubFamilyCode`**: ISO standard classification sub-family code (e.g., `DMCT`) at the TxDetails level.
  - _Source:_ `<TxDtls>/<BkTxCd>/<Domn>/<Fmly>/<SubFmlyCd>`
- **`ProprietaryTransactionCode`**: Bank-specific internal transaction code at the TxDetails level.
  - _Source:_ `<TxDtls>/<BkTxCd>/<Prtry>/<Cd>`
- **`ReturnReasonCode`**: The ISO reason code if the transaction bounced/reversed (e.g., `AC01`) at the TxDetails level.
  - _Source:_ `<TxDtls>/<RtrInf>/<Rsn>/<Cd>` or `<Prtry>`
- **`PurposeCode`**: The ISO category for the payment (e.g., `SALA` for Salary) at the TxDetails level.
  - _Source:_ `<TxDtls>/<Purp>/<Cd>`
- **`PurposeProprietary`**: A proprietary category for the payment at the TxDetails level.
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
