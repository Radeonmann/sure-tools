from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.holding import Holding
    from ..models.pagination import Pagination


T = TypeVar("T", bound="HoldingCollection")


@_attrs_define
class HoldingCollection:
    """
    Attributes:
        holdings (list[Holding]):
        pagination (Pagination):
    """

    holdings: list[Holding]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        holdings = []
        for holdings_item_data in self.holdings:
            holdings_item = holdings_item_data.to_dict()
            holdings.append(holdings_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "holdings": holdings,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.holding import Holding
        from ..models.pagination import Pagination

        d = dict(src_dict)
        holdings = []
        _holdings = d.pop("holdings")
        for holdings_item_data in _holdings:
            holdings_item = Holding.from_dict(holdings_item_data)

            holdings.append(holdings_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        holding_collection = cls(
            holdings=holdings,
            pagination=pagination,
        )

        holding_collection.additional_properties = d
        return holding_collection

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
