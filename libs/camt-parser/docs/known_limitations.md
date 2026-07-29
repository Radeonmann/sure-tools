# Known Limitations & Edge Cases

## The Gross/Net Charges Mismatch

### The common cases ("Scenario 1 and 2")

Please write something short and concise here

### The Rare Bank Case ("Scenario 3")

In ISO 20022 CAMT.053 files, banks occasionally charge fees directly on a transaction. In extremely rare circumstances, a bank might report an entry where the booked ledger amount (`<Ntry><Amt>`) represents the **gross amount** (Transaction Amount + Charges), but the nested transaction details (`<TxDtls><Amt>`) only report the **net amount**.

For example, a $15 ledger deduction consisting of a $12 payment and a $3 fee might be structured like this:

- `<Ntry><Amt>` = 15
- `<TxDtls><Amt>` = 12
- `<Chrgs><Amt>` = 3

### The Issue with Our Parser

Our parser enforces a strict, mathematically safe batch validation check: the sum of the transaction amounts within an entry MUST exactly equal the total entry amount.

If a bank sends the structure above, the parser will intentionally crash and throw a `ValueError` during `_validate_transaction_batch`, because the sum of the transactions (`12`) does not equal the entry amount (`15`).

### Why This Is Not Supported

This structure is **extremely rare** and technically violates the **Common Global Implementation (CGI-MP) guidelines** for ISO 20022. The specification strongly dictates that `<Ntry><Amt>` must always equal the sum of the nested `<TxDtls><Amt>` elements.

Proper, compliant fee handling is done in one of two ways:

1.  **Separate Entries:** The fee is booked as a completely separate `<Ntry>` on the statement.
2.  **Instructed vs. Booked:** The fee is accounted for entirely inside the transaction block by showing the discrepancy between the invoice amount (`<InstdAmt>`) and the booked amount (`<TxAmt>`).

Because Scenario 3 represents non-compliant XML, our parser correctly fails loudly to prevent corrupted or mathematically unbalanced data from entering the downstream accounting system.

If this error ever surfaces in a production environment, it should be resolved entirely at the extraction level within the parser itself. The parser will need to be updated to mathematically reconcile and normalize these amounts internally before they are validated or returned. This guarantees that downstream consumers will always receive a mathematically balanced and standardized `TransactionInfo` dictionary, ensuring they never have to implement custom business logic or worry about how to interpret these discrepancies.

### Disclaimer

The expected scenarios and the evaluation of rare / common scenarios were provided by a strong state of the art AI model based on standard ISO 20022 CGI-MP compliance guidelines and current empirical data. So if the evaluation is inaccurate, please let me know. But because in my ledger files I never have scenario 3, I will not implement it for now.
