from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_decision_status import TransferDecisionStatus
from ..models.transfer_decision_transfer_type import TransferDecisionTransferType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfer_transaction_side import TransferTransactionSide


T = TypeVar("T", bound="TransferDecision")


@_attrs_define
class TransferDecision:
    """
    Attributes:
        id (UUID):
        status (TransferDecisionStatus):
        date (datetime.date):
        amount (str):
        amount_cents (int): Absolute transfer amount in currency minor units
        currency (str):
        transfer_type (TransferDecisionTransferType):
        inflow_transaction (TransferTransactionSide):
        outflow_transaction (TransferTransactionSide):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        notes (None | str | Unset):
    """

    id: UUID
    status: TransferDecisionStatus
    date: datetime.date
    amount: str
    amount_cents: int
    currency: str
    transfer_type: TransferDecisionTransferType
    inflow_transaction: TransferTransactionSide
    outflow_transaction: TransferTransactionSide
    created_at: datetime.datetime
    updated_at: datetime.datetime
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        date = self.date.isoformat()

        amount = self.amount

        amount_cents = self.amount_cents

        currency = self.currency

        transfer_type = self.transfer_type.value

        inflow_transaction = self.inflow_transaction.to_dict()

        outflow_transaction = self.outflow_transaction.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "date": date,
                "amount": amount,
                "amount_cents": amount_cents,
                "currency": currency,
                "transfer_type": transfer_type,
                "inflow_transaction": inflow_transaction,
                "outflow_transaction": outflow_transaction,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_transaction_side import TransferTransactionSide

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = TransferDecisionStatus(d.pop("status"))

        date = datetime.date.fromisoformat(d.pop("date"))

        amount = d.pop("amount")

        amount_cents = d.pop("amount_cents")

        currency = d.pop("currency")

        transfer_type = TransferDecisionTransferType(d.pop("transfer_type"))

        inflow_transaction = TransferTransactionSide.from_dict(d.pop("inflow_transaction"))

        outflow_transaction = TransferTransactionSide.from_dict(d.pop("outflow_transaction"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        transfer_decision = cls(
            id=id,
            status=status,
            date=date,
            amount=amount,
            amount_cents=amount_cents,
            currency=currency,
            transfer_type=transfer_type,
            inflow_transaction=inflow_transaction,
            outflow_transaction=outflow_transaction,
            created_at=created_at,
            updated_at=updated_at,
            notes=notes,
        )

        transfer_decision.additional_properties = d
        return transfer_decision

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
