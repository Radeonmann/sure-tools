# camt-parser

A robust, mathematically safe, and fully typed Python parser for ISO 20022 CAMT.053 bank statements.

`camt-parser` takes deeply nested, highly complex banking XML files and flattens them into clean, easy-to-digest Python dictionaries (`TransactionInfo`). It is designed to handle edge cases, batch payments, complex foreign exchange calculations, and rich metadata extraction out-of-the-box.

## Features

- **Strict Validation:** Automatically validates that the sum of batch transactions exactly matches the entry ledger amount, and verifies foreign exchange math against a configurable tolerance.
- **Rich Data Extraction:** Pulls high-value accounting data including ISO Purpose Codes, Return Reasons, structured invoice references, and masked Card PANs.
- **Safe Fallbacks:** Intelligently inherits entry-level data (like charges and domain codes) for simple transactions while safely isolating them during batch processing.
- **Whitespace Normalization:** Automatically sanitizes and concatenates artificially wrapped free-text remittance blocks.
- **Lossless Raw Payload:** Exposes an `Advanced` dictionary containing the exact XML ancestral tree (Statement -> Entry -> Transaction) with sibling nodes safely pruned, ensuring no data is ever truly lost.

## Requirements

- Python >= 3.12
- `lxml` >= 6.1.1

## Installation

If you are using `uv` (recommended):

```bash
uv add camt-parser
```

Or via pip:

```bash
pip install camt-parser
```

## Quick Start

```python
from camt_parser import Camt053Parser

# Initialize the parser from a file
parser = Camt053Parser.from_file("path/to/statement.xml")

# Extract all transactions as a flat list of dictionaries
transactions = parser.get_transactions()

for tx in transactions:
    print(f"Date: {tx['BookingDate']}, Amount: {tx['Amount']} {tx['Currency']}")
    print(f"Debtor: {tx['DebtorName']}, Remittance: {tx['UnstructuredRemittanceInfo']}")
    print("-" * 20)
```

## Documentation

- [TransactionInfo Data Dictionary](docs/transaction_info.md): A detailed breakdown of every field extracted by the parser.
- [Known Limitations & Edge Cases](docs/known_limitations.md): Documentation on unsupported bank anomalies (e.g., Gross/Net mismatch).
