from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImportStatusSummary")


@_attrs_define
class ImportStatusSummary:
    """
    Attributes:
        uploaded (bool):
        configured (bool):
        terminal (bool):
    """

    uploaded: bool
    configured: bool
    terminal: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uploaded = self.uploaded

        configured = self.configured

        terminal = self.terminal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploaded": uploaded,
                "configured": configured,
                "terminal": terminal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uploaded = d.pop("uploaded")

        configured = d.pop("configured")

        terminal = d.pop("terminal")

        import_status_summary = cls(
            uploaded=uploaded,
            configured=configured,
            terminal=terminal,
        )

        import_status_summary.additional_properties = d
        return import_status_summary

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
