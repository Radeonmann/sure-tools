from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_v1_recurring_transactions_id_body_recurring_transaction_status import (
    PatchApiV1RecurringTransactionsIdBodyRecurringTransactionStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiV1RecurringTransactionsIdBodyRecurringTransaction")


@_attrs_define
class PatchApiV1RecurringTransactionsIdBodyRecurringTransaction:
    """
    Attributes:
        status (PatchApiV1RecurringTransactionsIdBodyRecurringTransactionStatus | Unset):
        expected_day_of_month (int | Unset):
        next_expected_date (datetime.date | Unset):
    """

    status: PatchApiV1RecurringTransactionsIdBodyRecurringTransactionStatus | Unset = UNSET
    expected_day_of_month: int | Unset = UNSET
    next_expected_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        expected_day_of_month = self.expected_day_of_month

        next_expected_date: str | Unset = UNSET
        if not isinstance(self.next_expected_date, Unset):
            next_expected_date = self.next_expected_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if expected_day_of_month is not UNSET:
            field_dict["expected_day_of_month"] = expected_day_of_month
        if next_expected_date is not UNSET:
            field_dict["next_expected_date"] = next_expected_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: PatchApiV1RecurringTransactionsIdBodyRecurringTransactionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchApiV1RecurringTransactionsIdBodyRecurringTransactionStatus(_status)

        expected_day_of_month = d.pop("expected_day_of_month", UNSET)

        _next_expected_date = d.pop("next_expected_date", UNSET)
        next_expected_date: datetime.date | Unset
        if isinstance(_next_expected_date, Unset):
            next_expected_date = UNSET
        else:
            next_expected_date = datetime.date.fromisoformat(_next_expected_date)

        patch_api_v1_recurring_transactions_id_body_recurring_transaction = cls(
            status=status,
            expected_day_of_month=expected_day_of_month,
            next_expected_date=next_expected_date,
        )

        patch_api_v1_recurring_transactions_id_body_recurring_transaction.additional_properties = d
        return patch_api_v1_recurring_transactions_id_body_recurring_transaction

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
