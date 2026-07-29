from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.category import Category
    from ..models.merchant import Merchant
    from ..models.tag import Tag
    from ..models.transfer import Transfer


T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """
    Attributes:
        id (UUID):
        date (datetime.date):
        amount (str):
        currency (str):
        name (str):
        classification (str):
        account (Account):
        tags (list[Tag]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        notes (None | str | Unset):
        external_id (None | str | Unset):
        source (None | str | Unset):
        category (Category | Unset):
        merchant (Merchant | Unset):
        transfer (Transfer | Unset):
    """

    id: UUID
    date: datetime.date
    amount: str
    currency: str
    name: str
    classification: str
    account: Account
    tags: list[Tag]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    notes: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    category: Category | Unset = UNSET
    merchant: Merchant | Unset = UNSET
    transfer: Transfer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        date = self.date.isoformat()

        amount = self.amount

        currency = self.currency

        name = self.name

        classification = self.classification

        account = self.account.to_dict()

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        transfer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transfer, Unset):
            transfer = self.transfer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "amount": amount,
                "currency": currency,
                "name": name,
                "classification": classification,
                "account": account,
                "tags": tags,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if source is not UNSET:
            field_dict["source"] = source
        if category is not UNSET:
            field_dict["category"] = category
        if merchant is not UNSET:
            field_dict["merchant"] = merchant
        if transfer is not UNSET:
            field_dict["transfer"] = transfer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.category import Category
        from ..models.merchant import Merchant
        from ..models.tag import Tag
        from ..models.transfer import Transfer

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        amount = d.pop("amount")

        currency = d.pop("currency")

        name = d.pop("name")

        classification = d.pop("classification")

        account = Account.from_dict(d.pop("account"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        _category = d.pop("category", UNSET)
        category: Category | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = Category.from_dict(_category)

        _merchant = d.pop("merchant", UNSET)
        merchant: Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = Merchant.from_dict(_merchant)

        _transfer = d.pop("transfer", UNSET)
        transfer: Transfer | Unset
        if isinstance(_transfer, Unset):
            transfer = UNSET
        else:
            transfer = Transfer.from_dict(_transfer)

        transaction = cls(
            id=id,
            date=date,
            amount=amount,
            currency=currency,
            name=name,
            classification=classification,
            account=account,
            tags=tags,
            created_at=created_at,
            updated_at=updated_at,
            notes=notes,
            external_id=external_id,
            source=source,
            category=category,
            merchant=merchant,
            transfer=transfer,
        )

        transaction.additional_properties = d
        return transaction

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
