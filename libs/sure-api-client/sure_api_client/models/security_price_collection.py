from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.security_price import SecurityPrice


T = TypeVar("T", bound="SecurityPriceCollection")


@_attrs_define
class SecurityPriceCollection:
    """
    Attributes:
        security_prices (list[SecurityPrice]):
        pagination (Pagination):
    """

    security_prices: list[SecurityPrice]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_prices = []
        for security_prices_item_data in self.security_prices:
            security_prices_item = security_prices_item_data.to_dict()
            security_prices.append(security_prices_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "security_prices": security_prices,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.security_price import SecurityPrice

        d = dict(src_dict)
        security_prices = []
        _security_prices = d.pop("security_prices")
        for security_prices_item_data in _security_prices:
            security_prices_item = SecurityPrice.from_dict(security_prices_item_data)

            security_prices.append(security_prices_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        security_price_collection = cls(
            security_prices=security_prices,
            pagination=pagination,
        )

        security_price_collection.additional_properties = d
        return security_price_collection

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
