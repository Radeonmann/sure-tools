from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transfer_transaction_side import TransferTransactionSide


T = TypeVar("T", bound="RejectedTransfer")


@_attrs_define
class RejectedTransfer:
    """
    Attributes:
        id (UUID):
        inflow_transaction (TransferTransactionSide):
        outflow_transaction (TransferTransactionSide):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    inflow_transaction: TransferTransactionSide
    outflow_transaction: TransferTransactionSide
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        inflow_transaction = self.inflow_transaction.to_dict()

        outflow_transaction = self.outflow_transaction.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "inflow_transaction": inflow_transaction,
                "outflow_transaction": outflow_transaction,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_transaction_side import TransferTransactionSide

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        inflow_transaction = TransferTransactionSide.from_dict(d.pop("inflow_transaction"))

        outflow_transaction = TransferTransactionSide.from_dict(d.pop("outflow_transaction"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        rejected_transfer = cls(
            id=id,
            inflow_transaction=inflow_transaction,
            outflow_transaction=outflow_transaction,
            created_at=created_at,
            updated_at=updated_at,
        )

        rejected_transfer.additional_properties = d
        return rejected_transfer

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
