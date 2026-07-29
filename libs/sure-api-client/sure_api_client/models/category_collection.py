from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.category_detail import CategoryDetail
    from ..models.pagination import Pagination


T = TypeVar("T", bound="CategoryCollection")


@_attrs_define
class CategoryCollection:
    """
    Attributes:
        categories (list[CategoryDetail]):
        pagination (Pagination):
    """

    categories: list[CategoryDetail]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categories": categories,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_detail import CategoryDetail
        from ..models.pagination import Pagination

        d = dict(src_dict)
        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = CategoryDetail.from_dict(categories_item_data)

            categories.append(categories_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        category_collection = cls(
            categories=categories,
            pagination=pagination,
        )

        category_collection.additional_properties = d
        return category_collection

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
