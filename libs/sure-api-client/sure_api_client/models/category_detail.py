from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_parent import CategoryParent


T = TypeVar("T", bound="CategoryDetail")


@_attrs_define
class CategoryDetail:
    """
    Attributes:
        id (UUID):
        name (str):
        color (str):
        icon (str):
        subcategories_count (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        parent (CategoryParent | Unset):
    """

    id: UUID
    name: str
    color: str
    icon: str
    subcategories_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    parent: CategoryParent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        color = self.color

        icon = self.icon

        subcategories_count = self.subcategories_count

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "color": color,
                "icon": icon,
                "subcategories_count": subcategories_count,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_parent import CategoryParent

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        color = d.pop("color")

        icon = d.pop("icon")

        subcategories_count = d.pop("subcategories_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _parent = d.pop("parent", UNSET)
        parent: CategoryParent | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = CategoryParent.from_dict(_parent)

        category_detail = cls(
            id=id,
            name=name,
            color=color,
            icon=icon,
            subcategories_count=subcategories_count,
            created_at=created_at,
            updated_at=updated_at,
            parent=parent,
        )

        category_detail.additional_properties = d
        return category_detail

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
