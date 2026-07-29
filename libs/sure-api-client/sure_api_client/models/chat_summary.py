from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatSummary")


@_attrs_define
class ChatSummary:
    """
    Attributes:
        id (UUID):
        title (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        message_count (int):
        error (None | str | Unset):
        last_message_at (datetime.datetime | None | Unset):
    """

    id: UUID
    title: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    message_count: int
    error: None | str | Unset = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        title = self.title

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        message_count = self.message_count

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
                "message_count": message_count,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if last_message_at is not UNSET:
            field_dict["last_message_at"] = last_message_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        title = d.pop("title")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        message_count = d.pop("message_count")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_last_message_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_message_at = _parse_last_message_at(d.pop("last_message_at", UNSET))

        chat_summary = cls(
            id=id,
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            message_count=message_count,
            error=error,
            last_message_at=last_message_at,
        )

        chat_summary.additional_properties = d
        return chat_summary

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
