from enum import Enum


class PostApiV1ImportsFilesBodyType(str, Enum):
    ACCOUNTIMPORT = "AccountImport"
    ACTUALIMPORT = "ActualImport"
    CATEGORYIMPORT = "CategoryImport"
    MERCHANTIMPORT = "MerchantImport"
    MINTIMPORT = "MintImport"
    PDFIMPORT = "PdfImport"
    QIFIMPORT = "QifImport"
    RULEIMPORT = "RuleImport"
    SUREIMPORT = "SureImport"
    TRADEIMPORT = "TradeImport"
    TRANSACTIONIMPORT = "TransactionImport"
    YNABIMPORT = "YnabImport"

    def __str__(self) -> str:
        return str(self.value)
