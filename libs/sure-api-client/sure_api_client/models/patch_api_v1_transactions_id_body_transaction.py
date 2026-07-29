from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_v1_transactions_id_body_transaction_nature import PatchApiV1TransactionsIdBodyTransactionNature
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiV1TransactionsIdBodyTransaction")


@_attrs_define
class PatchApiV1TransactionsIdBodyTransaction:
    """
    Attributes:
        date (datetime.date | Unset):
        amount (float | Unset):
        name (str | Unset):
        description (str | Unset): Alternative to name field
        notes (str | Unset):
        currency (str | Unset): Currency code
        category_id (UUID | Unset):
        merchant_id (UUID | Unset):
        nature (PatchApiV1TransactionsIdBodyTransactionNature | Unset):
        tag_ids (list[UUID] | Unset): Array of tag IDs to assign. Omit to preserve existing tags; use [] to clear all
            tags.
    """

    date: datetime.date | Unset = UNSET
    amount: float | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    notes: str | Unset = UNSET
    currency: str | Unset = UNSET
    category_id: UUID | Unset = UNSET
    merchant_id: UUID | Unset = UNSET
    nature: PatchApiV1TransactionsIdBodyTransactionNature | Unset = UNSET
    tag_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        amount = self.amount

        name = self.name

        description = self.description

        notes = self.notes

        currency = self.currency

        category_id: str | Unset = UNSET
        if not isinstance(self.category_id, Unset):
            category_id = str(self.category_id)

        merchant_id: str | Unset = UNSET
        if not isinstance(self.merchant_id, Unset):
            merchant_id = str(self.merchant_id)

        nature: str | Unset = UNSET
        if not isinstance(self.nature, Unset):
            nature = self.nature.value

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = []
            for tag_ids_item_data in self.tag_ids:
                tag_ids_item = str(tag_ids_item_data)
                tag_ids.append(tag_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if notes is not UNSET:
            field_dict["notes"] = notes
        if currency is not UNSET:
            field_dict["currency"] = currency
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if merchant_id is not UNSET:
            field_dict["merchant_id"] = merchant_id
        if nature is not UNSET:
            field_dict["nature"] = nature
        if tag_ids is not UNSET:
            field_dict["tag_ids"] = tag_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        amount = d.pop("amount", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        notes = d.pop("notes", UNSET)

        currency = d.pop("currency", UNSET)

        _category_id = d.pop("category_id", UNSET)
        category_id: UUID | Unset
        if isinstance(_category_id, Unset):
            category_id = UNSET
        else:
            category_id = UUID(_category_id)

        _merchant_id = d.pop("merchant_id", UNSET)
        merchant_id: UUID | Unset
        if isinstance(_merchant_id, Unset):
            merchant_id = UNSET
        else:
            merchant_id = UUID(_merchant_id)

        _nature = d.pop("nature", UNSET)
        nature: PatchApiV1TransactionsIdBodyTransactionNature | Unset
        if isinstance(_nature, Unset):
            nature = UNSET
        else:
            nature = PatchApiV1TransactionsIdBodyTransactionNature(_nature)

        _tag_ids = d.pop("tag_ids", UNSET)
        tag_ids: list[UUID] | Unset = UNSET
        if _tag_ids is not UNSET:
            tag_ids = []
            for tag_ids_item_data in _tag_ids:
                tag_ids_item = UUID(tag_ids_item_data)

                tag_ids.append(tag_ids_item)

        patch_api_v1_transactions_id_body_transaction = cls(
            date=date,
            amount=amount,
            name=name,
            description=description,
            notes=notes,
            currency=currency,
            category_id=category_id,
            merchant_id=merchant_id,
            nature=nature,
            tag_ids=tag_ids,
        )

        patch_api_v1_transactions_id_body_transaction.additional_properties = d
        return patch_api_v1_transactions_id_body_transaction

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
