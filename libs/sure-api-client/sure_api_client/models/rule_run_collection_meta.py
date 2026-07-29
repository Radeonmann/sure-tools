from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleRunCollectionMeta")


@_attrs_define
class RuleRunCollectionMeta:
    """
    Attributes:
        current_page (int):
        total_pages (int):
        total_count (int):
        per_page (int):
        next_page (int | None | Unset):
        prev_page (int | None | Unset):
    """

    current_page: int
    total_pages: int
    total_count: int
    per_page: int
    next_page: int | None | Unset = UNSET
    prev_page: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        total_pages = self.total_pages

        total_count = self.total_count

        per_page = self.per_page

        next_page: int | None | Unset
        if isinstance(self.next_page, Unset):
            next_page = UNSET
        else:
            next_page = self.next_page

        prev_page: int | None | Unset
        if isinstance(self.prev_page, Unset):
            prev_page = UNSET
        else:
            prev_page = self.prev_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_page": current_page,
                "total_pages": total_pages,
                "total_count": total_count,
                "per_page": per_page,
            }
        )
        if next_page is not UNSET:
            field_dict["next_page"] = next_page
        if prev_page is not UNSET:
            field_dict["prev_page"] = prev_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_page = d.pop("current_page")

        total_pages = d.pop("total_pages")

        total_count = d.pop("total_count")

        per_page = d.pop("per_page")

        def _parse_next_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_page = _parse_next_page(d.pop("next_page", UNSET))

        def _parse_prev_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prev_page = _parse_prev_page(d.pop("prev_page", UNSET))

        rule_run_collection_meta = cls(
            current_page=current_page,
            total_pages=total_pages,
            total_count=total_count,
            per_page=per_page,
            next_page=next_page,
            prev_page=prev_page,
        )

        rule_run_collection_meta.additional_properties = d
        return rule_run_collection_meta

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
