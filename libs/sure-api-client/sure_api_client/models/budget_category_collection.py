from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.budget_category_summary import BudgetCategorySummary
    from ..models.pagination import Pagination


T = TypeVar("T", bound="BudgetCategoryCollection")


@_attrs_define
class BudgetCategoryCollection:
    """
    Attributes:
        budget_categories (list[BudgetCategorySummary]):
        pagination (Pagination):
    """

    budget_categories: list[BudgetCategorySummary]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget_categories = []
        for budget_categories_item_data in self.budget_categories:
            budget_categories_item = budget_categories_item_data.to_dict()
            budget_categories.append(budget_categories_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budget_categories": budget_categories,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_category_summary import BudgetCategorySummary
        from ..models.pagination import Pagination

        d = dict(src_dict)
        budget_categories = []
        _budget_categories = d.pop("budget_categories")
        for budget_categories_item_data in _budget_categories:
            budget_categories_item = BudgetCategorySummary.from_dict(budget_categories_item_data)

            budget_categories.append(budget_categories_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        budget_category_collection = cls(
            budget_categories=budget_categories,
            pagination=pagination,
        )

        budget_category_collection.additional_properties = d
        return budget_category_collection

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
