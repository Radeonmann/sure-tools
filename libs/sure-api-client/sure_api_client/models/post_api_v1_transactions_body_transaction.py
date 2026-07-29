from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_v1_transactions_body_transaction_nature import PostApiV1TransactionsBodyTransactionNature
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiV1TransactionsBodyTransaction")


@_attrs_define
class PostApiV1TransactionsBodyTransaction:
    """
    Attributes:
        account_id (UUID): Account ID (required)
        date (datetime.date): Transaction date
        amount (float): Transaction amount
        name (str): Transaction name/description
        description (str | Unset): Alternative to name field
        notes (str | Unset): Additional notes
        currency (str | Unset): Currency code (defaults to family currency)
        category_id (UUID | Unset): Category ID
        merchant_id (UUID | Unset): Merchant ID
        nature (PostApiV1TransactionsBodyTransactionNature | Unset): Transaction nature (determines sign)
        external_id (str | Unset): Optional external idempotency key scoped to account and source
        source (str | Unset): Optional source namespace for external_id. Requires external_id and defaults to api when
            external_id is provided
        tag_ids (list[UUID] | Unset): Array of tag IDs
    """

    account_id: UUID
    date: datetime.date
    amount: float
    name: str
    description: str | Unset = UNSET
    notes: str | Unset = UNSET
    currency: str | Unset = UNSET
    category_id: UUID | Unset = UNSET
    merchant_id: UUID | Unset = UNSET
    nature: PostApiV1TransactionsBodyTransactionNature | Unset = UNSET
    external_id: str | Unset = UNSET
    source: str | Unset = UNSET
    tag_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = str(self.account_id)

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

        external_id = self.external_id

        source = self.source

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = []
            for tag_ids_item_data in self.tag_ids:
                tag_ids_item = str(tag_ids_item_data)
                tag_ids.append(tag_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "date": date,
                "amount": amount,
                "name": name,
            }
        )
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
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if source is not UNSET:
            field_dict["source"] = source
        if tag_ids is not UNSET:
            field_dict["tag_ids"] = tag_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = UUID(d.pop("account_id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        amount = d.pop("amount")

        name = d.pop("name")

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
        nature: PostApiV1TransactionsBodyTransactionNature | Unset
        if isinstance(_nature, Unset):
            nature = UNSET
        else:
            nature = PostApiV1TransactionsBodyTransactionNature(_nature)

        external_id = d.pop("external_id", UNSET)

        source = d.pop("source", UNSET)

        _tag_ids = d.pop("tag_ids", UNSET)
        tag_ids: list[UUID] | Unset = UNSET
        if _tag_ids is not UNSET:
            tag_ids = []
            for tag_ids_item_data in _tag_ids:
                tag_ids_item = UUID(tag_ids_item_data)

                tag_ids.append(tag_ids_item)

        post_api_v1_transactions_body_transaction = cls(
            account_id=account_id,
            date=date,
            amount=amount,
            name=name,
            description=description,
            notes=notes,
            currency=currency,
            category_id=category_id,
            merchant_id=merchant_id,
            nature=nature,
            external_id=external_id,
            source=source,
            tag_ids=tag_ids,
        )

        post_api_v1_transactions_body_transaction.additional_properties = d
        return post_api_v1_transactions_body_transaction

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
