from enum import Enum


class TransferDecisionTransferType(str, Enum):
    LIABILITY_PAYMENT = "liability_payment"
    LOAN_PAYMENT = "loan_payment"
    TRANSFER = "transfer"

    def __str__(self) -> str:
        return str(self.value)
