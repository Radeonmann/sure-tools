from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.transfer_decision import TransferDecision


T = TypeVar("T", bound="TransferDecisionCollection")


@_attrs_define
class TransferDecisionCollection:
    """
    Attributes:
        transfers (list[TransferDecision]):
        pagination (Pagination):
    """

    transfers: list[TransferDecision]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transfers = []
        for transfers_item_data in self.transfers:
            transfers_item = transfers_item_data.to_dict()
            transfers.append(transfers_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transfers": transfers,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.transfer_decision import TransferDecision

        d = dict(src_dict)
        transfers = []
        _transfers = d.pop("transfers")
        for transfers_item_data in _transfers:
            transfers_item = TransferDecision.from_dict(transfers_item_data)

            transfers.append(transfers_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        transfer_decision_collection = cls(
            transfers=transfers,
            pagination=pagination,
        )

        transfer_decision_collection.additional_properties = d
        return transfer_decision_collection

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
