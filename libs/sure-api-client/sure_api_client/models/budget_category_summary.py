from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_category_summary_category import BudgetCategorySummaryCategory


T = TypeVar("T", bound="BudgetCategorySummary")


@_attrs_define
class BudgetCategorySummary:
    """
    Attributes:
        id (UUID):
        budget_id (UUID):
        currency (str):
        subcategory (bool):
        inherits_parent_budget (bool):
        category (BudgetCategorySummaryCategory):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        budgeted_spending (str | Unset):
        budgeted_spending_cents (int | Unset):
        display_budgeted_spending (str | Unset):
        display_budgeted_spending_cents (int | Unset):
    """

    id: UUID
    budget_id: UUID
    currency: str
    subcategory: bool
    inherits_parent_budget: bool
    category: BudgetCategorySummaryCategory
    created_at: datetime.datetime
    updated_at: datetime.datetime
    budgeted_spending: str | Unset = UNSET
    budgeted_spending_cents: int | Unset = UNSET
    display_budgeted_spending: str | Unset = UNSET
    display_budgeted_spending_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        budget_id = str(self.budget_id)

        currency = self.currency

        subcategory = self.subcategory

        inherits_parent_budget = self.inherits_parent_budget

        category = self.category.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        budgeted_spending = self.budgeted_spending

        budgeted_spending_cents = self.budgeted_spending_cents

        display_budgeted_spending = self.display_budgeted_spending

        display_budgeted_spending_cents = self.display_budgeted_spending_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "budget_id": budget_id,
                "currency": currency,
                "subcategory": subcategory,
                "inherits_parent_budget": inherits_parent_budget,
                "category": category,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if budgeted_spending is not UNSET:
            field_dict["budgeted_spending"] = budgeted_spending
        if budgeted_spending_cents is not UNSET:
            field_dict["budgeted_spending_cents"] = budgeted_spending_cents
        if display_budgeted_spending is not UNSET:
            field_dict["display_budgeted_spending"] = display_budgeted_spending
        if display_budgeted_spending_cents is not UNSET:
            field_dict["display_budgeted_spending_cents"] = display_budgeted_spending_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_category_summary_category import BudgetCategorySummaryCategory

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        budget_id = UUID(d.pop("budget_id"))

        currency = d.pop("currency")

        subcategory = d.pop("subcategory")

        inherits_parent_budget = d.pop("inherits_parent_budget")

        category = BudgetCategorySummaryCategory.from_dict(d.pop("category"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        budgeted_spending = d.pop("budgeted_spending", UNSET)

        budgeted_spending_cents = d.pop("budgeted_spending_cents", UNSET)

        display_budgeted_spending = d.pop("display_budgeted_spending", UNSET)

        display_budgeted_spending_cents = d.pop("display_budgeted_spending_cents", UNSET)

        budget_category_summary = cls(
            id=id,
            budget_id=budget_id,
            currency=currency,
            subcategory=subcategory,
            inherits_parent_budget=inherits_parent_budget,
            category=category,
            created_at=created_at,
            updated_at=updated_at,
            budgeted_spending=budgeted_spending,
            budgeted_spending_cents=budgeted_spending_cents,
            display_budgeted_spending=display_budgeted_spending,
            display_budgeted_spending_cents=display_budgeted_spending_cents,
        )

        budget_category_summary.additional_properties = d
        return budget_category_summary

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
