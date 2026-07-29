"""
camt_parser package
"""

import logging

# Local imports for public API
from .camt053_parser import (
    Camt053Parser,
    Camt053ParserSettings,
    TransactionInfo,
)

# Define the public API of this package
__all__ = [
    "Camt053Parser",
    "Camt053ParserSettings",
    "TransactionInfo",
]

# Initialize library logging with a NullHandler to prevent default stderr output
# to use logging in your application, configure logging in your main application code (logger.basicConfig, etc.)
logging.getLogger(__name__).addHandler(logging.NullHandler())
