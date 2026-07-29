from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.rejected_transfer import RejectedTransfer


T = TypeVar("T", bound="RejectedTransferCollection")


@_attrs_define
class RejectedTransferCollection:
    """
    Attributes:
        rejected_transfers (list[RejectedTransfer]):
        pagination (Pagination):
    """

    rejected_transfers: list[RejectedTransfer]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rejected_transfers = []
        for rejected_transfers_item_data in self.rejected_transfers:
            rejected_transfers_item = rejected_transfers_item_data.to_dict()
            rejected_transfers.append(rejected_transfers_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rejected_transfers": rejected_transfers,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.rejected_transfer import RejectedTransfer

        d = dict(src_dict)
        rejected_transfers = []
        _rejected_transfers = d.pop("rejected_transfers")
        for rejected_transfers_item_data in _rejected_transfers:
            rejected_transfers_item = RejectedTransfer.from_dict(rejected_transfers_item_data)

            rejected_transfers.append(rejected_transfers_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        rejected_transfer_collection = cls(
            rejected_transfers=rejected_transfers,
            pagination=pagination,
        )

        rejected_transfer_collection.additional_properties = d
        return rejected_transfer_collection

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
