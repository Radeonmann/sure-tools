from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FamilyExportFile")


@_attrs_define
class FamilyExportFile:
    """
    Attributes:
        attached (bool):
        byte_size (int | None | Unset):
        content_type (None | str | Unset):
    """

    attached: bool
    byte_size: int | None | Unset = UNSET
    content_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attached = self.attached

        byte_size: int | None | Unset
        if isinstance(self.byte_size, Unset):
            byte_size = UNSET
        else:
            byte_size = self.byte_size

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attached": attached,
            }
        )
        if byte_size is not UNSET:
            field_dict["byte_size"] = byte_size
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attached = d.pop("attached")

        def _parse_byte_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        byte_size = _parse_byte_size(d.pop("byte_size", UNSET))

        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))

        family_export_file = cls(
            attached=attached,
            byte_size=byte_size,
            content_type=content_type,
        )

        family_export_file.additional_properties = d
        return family_export_file

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
