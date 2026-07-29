from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_detail_status import AccountDetailStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountDetail")


@_attrs_define
class AccountDetail:
    """
    Attributes:
        id (UUID):
        name (str):
        balance (str):
        balance_cents (int): Signed balance in minor currency units
        cash_balance (str):
        cash_balance_cents (int): Signed cash balance in minor currency units
        currency (str):
        classification (str):
        account_type (None | str):
        status (AccountDetailStatus):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        subtype (None | str | Unset):
        institution_name (None | str | Unset):
        institution_domain (None | str | Unset):
    """

    id: UUID
    name: str
    balance: str
    balance_cents: int
    cash_balance: str
    cash_balance_cents: int
    currency: str
    classification: str
    account_type: None | str
    status: AccountDetailStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    subtype: None | str | Unset = UNSET
    institution_name: None | str | Unset = UNSET
    institution_domain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        balance = self.balance

        balance_cents = self.balance_cents

        cash_balance = self.cash_balance

        cash_balance_cents = self.cash_balance_cents

        currency = self.currency

        classification = self.classification

        account_type: None | str
        account_type = self.account_type

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        subtype: None | str | Unset
        if isinstance(self.subtype, Unset):
            subtype = UNSET
        else:
            subtype = self.subtype

        institution_name: None | str | Unset
        if isinstance(self.institution_name, Unset):
            institution_name = UNSET
        else:
            institution_name = self.institution_name

        institution_domain: None | str | Unset
        if isinstance(self.institution_domain, Unset):
            institution_domain = UNSET
        else:
            institution_domain = self.institution_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "balance": balance,
                "balance_cents": balance_cents,
                "cash_balance": cash_balance,
                "cash_balance_cents": cash_balance_cents,
                "currency": currency,
                "classification": classification,
                "account_type": account_type,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if institution_name is not UNSET:
            field_dict["institution_name"] = institution_name
        if institution_domain is not UNSET:
            field_dict["institution_domain"] = institution_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        balance = d.pop("balance")

        balance_cents = d.pop("balance_cents")

        cash_balance = d.pop("cash_balance")

        cash_balance_cents = d.pop("cash_balance_cents")

        currency = d.pop("currency")

        classification = d.pop("classification")

        def _parse_account_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_type = _parse_account_type(d.pop("account_type"))

        status = AccountDetailStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_subtype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtype = _parse_subtype(d.pop("subtype", UNSET))

        def _parse_institution_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        institution_name = _parse_institution_name(d.pop("institution_name", UNSET))

        def _parse_institution_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        institution_domain = _parse_institution_domain(d.pop("institution_domain", UNSET))

        account_detail = cls(
            id=id,
            name=name,
            balance=balance,
            balance_cents=balance_cents,
            cash_balance=cash_balance,
            cash_balance_cents=cash_balance_cents,
            currency=currency,
            classification=classification,
            account_type=account_type,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            subtype=subtype,
            institution_name=institution_name,
            institution_domain=institution_domain,
        )

        account_detail.additional_properties = d
        return account_detail

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
