from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoryCreateRequestCategory")


@_attrs_define
class CategoryCreateRequestCategory:
    """
    Attributes:
        name (str): Category name (required, unique within family)
        color (str | Unset): Hex color code (e.g. #22c55e). Defaults to #6172F3 if omitted; subcategories inherit parent
            color.
        icon (str | Unset): Lucide icon name (e.g. "coffee"). Auto-suggested from the name when omitted.
        parent_id (None | Unset | UUID): Parent category ID. Must belong to the same family. Categories support up to 2
            levels of nesting.
    """

    name: str
    color: str | Unset = UNSET
    icon: str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        color = self.color

        icon = self.icon

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        color = d.pop("color", UNSET)

        icon = d.pop("icon", UNSET)

        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        category_create_request_category = cls(
            name=name,
            color=color,
            icon=icon,
            parent_id=parent_id,
        )

        category_create_request_category.additional_properties = d
        return category_create_request_category

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
