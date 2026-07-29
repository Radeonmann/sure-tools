from enum import Enum


class MerchantDetailType(str, Enum):
    FAMILYMERCHANT = "FamilyMerchant"
    PROVIDERMERCHANT = "ProviderMerchant"

    def __str__(self) -> str:
        return str(self.value)
