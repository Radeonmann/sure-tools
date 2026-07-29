from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.valuation import Valuation


T = TypeVar("T", bound="ValuationCollection")


@_attrs_define
class ValuationCollection:
    """
    Attributes:
        valuations (list[Valuation]):
        pagination (Pagination):
    """

    valuations: list[Valuation]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valuations = []
        for valuations_item_data in self.valuations:
            valuations_item = valuations_item_data.to_dict()
            valuations.append(valuations_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valuations": valuations,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.valuation import Valuation

        d = dict(src_dict)
        valuations = []
        _valuations = d.pop("valuations")
        for valuations_item_data in _valuations:
            valuations_item = Valuation.from_dict(valuations_item_data)

            valuations.append(valuations_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        valuation_collection = cls(
            valuations=valuations,
            pagination=pagination,
        )

        valuation_collection.additional_properties = d
        return valuation_collection

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
