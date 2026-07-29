from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        page (int):
        per_page (int):
        total_count (int):
        total_pages (int):
    """

    page: int
    per_page: int
    total_count: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        per_page = self.per_page

        total_count = self.total_count

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "per_page": per_page,
                "total_count": total_count,
                "total_pages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page")

        per_page = d.pop("per_page")

        total_count = d.pop("total_count")

        total_pages = d.pop("total_pages")

        pagination = cls(
            page=page,
            per_page=per_page,
            total_count=total_count,
            total_pages=total_pages,
        )

        pagination.additional_properties = d
        return pagination

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
