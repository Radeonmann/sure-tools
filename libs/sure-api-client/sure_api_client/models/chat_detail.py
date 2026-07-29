from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ChatDetail")


@_attrs_define
class ChatDetail:
    """
    Attributes:
        id (UUID):
        title (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        messages (list[Message]):
        error (None | str | Unset):
        pagination (Pagination | Unset):
    """

    id: UUID
    title: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    messages: list[Message]
    error: None | str | Unset = UNSET
    pagination: Pagination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        title = self.title

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
                "messages": messages,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message
        from ..models.pagination import Pagination

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        title = d.pop("title")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = Message.from_dict(messages_item_data)

            messages.append(messages_item)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        _pagination = d.pop("pagination", UNSET)
        pagination: Pagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        chat_detail = cls(
            id=id,
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            messages=messages,
            error=error,
            pagination=pagination,
        )

        chat_detail.additional_properties = d
        return chat_detail

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
