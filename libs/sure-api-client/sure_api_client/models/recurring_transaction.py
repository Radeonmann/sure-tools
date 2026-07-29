from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recurring_transaction_status import RecurringTransactionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.merchant import Merchant


T = TypeVar("T", bound="RecurringTransaction")


@_attrs_define
class RecurringTransaction:
    """
    Attributes:
        id (UUID):
        amount (str):
        amount_cents (int): Amount in currency minor units
        currency (str):
        expected_day_of_month (int):
        last_occurrence_date (datetime.date):
        next_expected_date (datetime.date):
        status (RecurringTransactionStatus):
        occurrence_count (int):
        manual (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (None | str | Unset):
        expected_amount_min (None | str | Unset):
        expected_amount_min_cents (int | None | Unset): Minimum expected amount in currency minor units
        expected_amount_max (None | str | Unset):
        expected_amount_max_cents (int | None | Unset): Maximum expected amount in currency minor units
        expected_amount_avg (None | str | Unset):
        expected_amount_avg_cents (int | None | Unset): Average expected amount in currency minor units
        account (Account | Unset):
        merchant (Merchant | Unset):
    """

    id: UUID
    amount: str
    amount_cents: int
    currency: str
    expected_day_of_month: int
    last_occurrence_date: datetime.date
    next_expected_date: datetime.date
    status: RecurringTransactionStatus
    occurrence_count: int
    manual: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: None | str | Unset = UNSET
    expected_amount_min: None | str | Unset = UNSET
    expected_amount_min_cents: int | None | Unset = UNSET
    expected_amount_max: None | str | Unset = UNSET
    expected_amount_max_cents: int | None | Unset = UNSET
    expected_amount_avg: None | str | Unset = UNSET
    expected_amount_avg_cents: int | None | Unset = UNSET
    account: Account | Unset = UNSET
    merchant: Merchant | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        amount = self.amount

        amount_cents = self.amount_cents

        currency = self.currency

        expected_day_of_month = self.expected_day_of_month

        last_occurrence_date = self.last_occurrence_date.isoformat()

        next_expected_date = self.next_expected_date.isoformat()

        status = self.status.value

        occurrence_count = self.occurrence_count

        manual = self.manual

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        expected_amount_min: None | str | Unset
        if isinstance(self.expected_amount_min, Unset):
            expected_amount_min = UNSET
        else:
            expected_amount_min = self.expected_amount_min

        expected_amount_min_cents: int | None | Unset
        if isinstance(self.expected_amount_min_cents, Unset):
            expected_amount_min_cents = UNSET
        else:
            expected_amount_min_cents = self.expected_amount_min_cents

        expected_amount_max: None | str | Unset
        if isinstance(self.expected_amount_max, Unset):
            expected_amount_max = UNSET
        else:
            expected_amount_max = self.expected_amount_max

        expected_amount_max_cents: int | None | Unset
        if isinstance(self.expected_amount_max_cents, Unset):
            expected_amount_max_cents = UNSET
        else:
            expected_amount_max_cents = self.expected_amount_max_cents

        expected_amount_avg: None | str | Unset
        if isinstance(self.expected_amount_avg, Unset):
            expected_amount_avg = UNSET
        else:
            expected_amount_avg = self.expected_amount_avg

        expected_amount_avg_cents: int | None | Unset
        if isinstance(self.expected_amount_avg_cents, Unset):
            expected_amount_avg_cents = UNSET
        else:
            expected_amount_avg_cents = self.expected_amount_avg_cents

        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        merchant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merchant, Unset):
            merchant = self.merchant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "amount": amount,
                "amount_cents": amount_cents,
                "currency": currency,
                "expected_day_of_month": expected_day_of_month,
                "last_occurrence_date": last_occurrence_date,
                "next_expected_date": next_expected_date,
                "status": status,
                "occurrence_count": occurrence_count,
                "manual": manual,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if expected_amount_min is not UNSET:
            field_dict["expected_amount_min"] = expected_amount_min
        if expected_amount_min_cents is not UNSET:
            field_dict["expected_amount_min_cents"] = expected_amount_min_cents
        if expected_amount_max is not UNSET:
            field_dict["expected_amount_max"] = expected_amount_max
        if expected_amount_max_cents is not UNSET:
            field_dict["expected_amount_max_cents"] = expected_amount_max_cents
        if expected_amount_avg is not UNSET:
            field_dict["expected_amount_avg"] = expected_amount_avg
        if expected_amount_avg_cents is not UNSET:
            field_dict["expected_amount_avg_cents"] = expected_amount_avg_cents
        if account is not UNSET:
            field_dict["account"] = account
        if merchant is not UNSET:
            field_dict["merchant"] = merchant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.merchant import Merchant

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        amount = d.pop("amount")

        amount_cents = d.pop("amount_cents")

        currency = d.pop("currency")

        expected_day_of_month = d.pop("expected_day_of_month")

        last_occurrence_date = datetime.date.fromisoformat(d.pop("last_occurrence_date"))

        next_expected_date = datetime.date.fromisoformat(d.pop("next_expected_date"))

        status = RecurringTransactionStatus(d.pop("status"))

        occurrence_count = d.pop("occurrence_count")

        manual = d.pop("manual")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_expected_amount_min(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_amount_min = _parse_expected_amount_min(d.pop("expected_amount_min", UNSET))

        def _parse_expected_amount_min_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_amount_min_cents = _parse_expected_amount_min_cents(d.pop("expected_amount_min_cents", UNSET))

        def _parse_expected_amount_max(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_amount_max = _parse_expected_amount_max(d.pop("expected_amount_max", UNSET))

        def _parse_expected_amount_max_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_amount_max_cents = _parse_expected_amount_max_cents(d.pop("expected_amount_max_cents", UNSET))

        def _parse_expected_amount_avg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_amount_avg = _parse_expected_amount_avg(d.pop("expected_amount_avg", UNSET))

        def _parse_expected_amount_avg_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_amount_avg_cents = _parse_expected_amount_avg_cents(d.pop("expected_amount_avg_cents", UNSET))

        _account = d.pop("account", UNSET)
        account: Account | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = Account.from_dict(_account)

        _merchant = d.pop("merchant", UNSET)
        merchant: Merchant | Unset
        if isinstance(_merchant, Unset):
            merchant = UNSET
        else:
            merchant = Merchant.from_dict(_merchant)

        recurring_transaction = cls(
            id=id,
            amount=amount,
            amount_cents=amount_cents,
            currency=currency,
            expected_day_of_month=expected_day_of_month,
            last_occurrence_date=last_occurrence_date,
            next_expected_date=next_expected_date,
            status=status,
            occurrence_count=occurrence_count,
            manual=manual,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            expected_amount_min=expected_amount_min,
            expected_amount_min_cents=expected_amount_min_cents,
            expected_amount_max=expected_amount_max,
            expected_amount_max_cents=expected_amount_max_cents,
            expected_amount_avg=expected_amount_avg,
            expected_amount_avg_cents=expected_amount_avg_cents,
            account=account,
            merchant=merchant,
        )

        recurring_transaction.additional_properties = d
        return recurring_transaction

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
