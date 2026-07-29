from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Budget")


@_attrs_define
class Budget:
    """
    Attributes:
        id (UUID):
        start_date (datetime.date):
        end_date (datetime.date):
        name (str):
        currency (str):
        initialized (bool):
        current (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        budgeted_spending (None | str | Unset):
        budgeted_spending_cents (int | None | Unset):
        expected_income (None | str | Unset):
        expected_income_cents (int | None | Unset):
        allocated_spending (str | Unset):
        allocated_spending_cents (int | Unset):
        actual_spending (str | Unset):
        actual_spending_cents (int | Unset):
        actual_income (str | Unset):
        actual_income_cents (int | Unset):
        available_to_spend (str | Unset):
        available_to_spend_cents (int | Unset):
        available_to_allocate (str | Unset):
        available_to_allocate_cents (int | Unset):
    """

    id: UUID
    start_date: datetime.date
    end_date: datetime.date
    name: str
    currency: str
    initialized: bool
    current: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    budgeted_spending: None | str | Unset = UNSET
    budgeted_spending_cents: int | None | Unset = UNSET
    expected_income: None | str | Unset = UNSET
    expected_income_cents: int | None | Unset = UNSET
    allocated_spending: str | Unset = UNSET
    allocated_spending_cents: int | Unset = UNSET
    actual_spending: str | Unset = UNSET
    actual_spending_cents: int | Unset = UNSET
    actual_income: str | Unset = UNSET
    actual_income_cents: int | Unset = UNSET
    available_to_spend: str | Unset = UNSET
    available_to_spend_cents: int | Unset = UNSET
    available_to_allocate: str | Unset = UNSET
    available_to_allocate_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        name = self.name

        currency = self.currency

        initialized = self.initialized

        current = self.current

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        budgeted_spending: None | str | Unset
        if isinstance(self.budgeted_spending, Unset):
            budgeted_spending = UNSET
        else:
            budgeted_spending = self.budgeted_spending

        budgeted_spending_cents: int | None | Unset
        if isinstance(self.budgeted_spending_cents, Unset):
            budgeted_spending_cents = UNSET
        else:
            budgeted_spending_cents = self.budgeted_spending_cents

        expected_income: None | str | Unset
        if isinstance(self.expected_income, Unset):
            expected_income = UNSET
        else:
            expected_income = self.expected_income

        expected_income_cents: int | None | Unset
        if isinstance(self.expected_income_cents, Unset):
            expected_income_cents = UNSET
        else:
            expected_income_cents = self.expected_income_cents

        allocated_spending = self.allocated_spending

        allocated_spending_cents = self.allocated_spending_cents

        actual_spending = self.actual_spending

        actual_spending_cents = self.actual_spending_cents

        actual_income = self.actual_income

        actual_income_cents = self.actual_income_cents

        available_to_spend = self.available_to_spend

        available_to_spend_cents = self.available_to_spend_cents

        available_to_allocate = self.available_to_allocate

        available_to_allocate_cents = self.available_to_allocate_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start_date": start_date,
                "end_date": end_date,
                "name": name,
                "currency": currency,
                "initialized": initialized,
                "current": current,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if budgeted_spending is not UNSET:
            field_dict["budgeted_spending"] = budgeted_spending
        if budgeted_spending_cents is not UNSET:
            field_dict["budgeted_spending_cents"] = budgeted_spending_cents
        if expected_income is not UNSET:
            field_dict["expected_income"] = expected_income
        if expected_income_cents is not UNSET:
            field_dict["expected_income_cents"] = expected_income_cents
        if allocated_spending is not UNSET:
            field_dict["allocated_spending"] = allocated_spending
        if allocated_spending_cents is not UNSET:
            field_dict["allocated_spending_cents"] = allocated_spending_cents
        if actual_spending is not UNSET:
            field_dict["actual_spending"] = actual_spending
        if actual_spending_cents is not UNSET:
            field_dict["actual_spending_cents"] = actual_spending_cents
        if actual_income is not UNSET:
            field_dict["actual_income"] = actual_income
        if actual_income_cents is not UNSET:
            field_dict["actual_income_cents"] = actual_income_cents
        if available_to_spend is not UNSET:
            field_dict["available_to_spend"] = available_to_spend
        if available_to_spend_cents is not UNSET:
            field_dict["available_to_spend_cents"] = available_to_spend_cents
        if available_to_allocate is not UNSET:
            field_dict["available_to_allocate"] = available_to_allocate
        if available_to_allocate_cents is not UNSET:
            field_dict["available_to_allocate_cents"] = available_to_allocate_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        start_date = datetime.date.fromisoformat(d.pop("start_date"))

        end_date = datetime.date.fromisoformat(d.pop("end_date"))

        name = d.pop("name")

        currency = d.pop("currency")

        initialized = d.pop("initialized")

        current = d.pop("current")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_budgeted_spending(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budgeted_spending = _parse_budgeted_spending(d.pop("budgeted_spending", UNSET))

        def _parse_budgeted_spending_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        budgeted_spending_cents = _parse_budgeted_spending_cents(d.pop("budgeted_spending_cents", UNSET))

        def _parse_expected_income(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_income = _parse_expected_income(d.pop("expected_income", UNSET))

        def _parse_expected_income_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_income_cents = _parse_expected_income_cents(d.pop("expected_income_cents", UNSET))

        allocated_spending = d.pop("allocated_spending", UNSET)

        allocated_spending_cents = d.pop("allocated_spending_cents", UNSET)

        actual_spending = d.pop("actual_spending", UNSET)

        actual_spending_cents = d.pop("actual_spending_cents", UNSET)

        actual_income = d.pop("actual_income", UNSET)

        actual_income_cents = d.pop("actual_income_cents", UNSET)

        available_to_spend = d.pop("available_to_spend", UNSET)

        available_to_spend_cents = d.pop("available_to_spend_cents", UNSET)

        available_to_allocate = d.pop("available_to_allocate", UNSET)

        available_to_allocate_cents = d.pop("available_to_allocate_cents", UNSET)

        budget = cls(
            id=id,
            start_date=start_date,
            end_date=end_date,
            name=name,
            currency=currency,
            initialized=initialized,
            current=current,
            created_at=created_at,
            updated_at=updated_at,
            budgeted_spending=budgeted_spending,
            budgeted_spending_cents=budgeted_spending_cents,
            expected_income=expected_income,
            expected_income_cents=expected_income_cents,
            allocated_spending=allocated_spending,
            allocated_spending_cents=allocated_spending_cents,
            actual_spending=actual_spending,
            actual_spending_cents=actual_spending_cents,
            actual_income=actual_income,
            actual_income_cents=actual_income_cents,
            available_to_spend=available_to_spend,
            available_to_spend_cents=available_to_spend_cents,
            available_to_allocate=available_to_allocate,
            available_to_allocate_cents=available_to_allocate_cents,
        )

        budget.additional_properties = d
        return budget

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
