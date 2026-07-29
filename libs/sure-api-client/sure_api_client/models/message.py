from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_role import MessageRole
from ..models.message_type import MessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_call import ToolCall


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        id (UUID):
        type_ (MessageType):
        role (MessageRole):
        content (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        model (None | str | Unset):
        tool_calls (list[ToolCall] | None | Unset):
    """

    id: UUID
    type_: MessageType
    role: MessageRole
    content: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    model: None | str | Unset = UNSET
    tool_calls: list[ToolCall] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        role = self.role.value

        content = self.content

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        tool_calls: list[dict[str, Any]] | None | Unset
        if isinstance(self.tool_calls, Unset):
            tool_calls = UNSET
        elif isinstance(self.tool_calls, list):
            tool_calls = []
            for tool_calls_type_0_item_data in self.tool_calls:
                tool_calls_type_0_item = tool_calls_type_0_item_data.to_dict()
                tool_calls.append(tool_calls_type_0_item)

        else:
            tool_calls = self.tool_calls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "role": role,
                "content": content,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_call import ToolCall

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = MessageType(d.pop("type"))

        role = MessageRole(d.pop("role"))

        content = d.pop("content")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_tool_calls(data: object) -> list[ToolCall] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tool_calls_type_0 = []
                _tool_calls_type_0 = data
                for tool_calls_type_0_item_data in _tool_calls_type_0:
                    tool_calls_type_0_item = ToolCall.from_dict(tool_calls_type_0_item_data)

                    tool_calls_type_0.append(tool_calls_type_0_item)

                return tool_calls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ToolCall] | None | Unset, data)

        tool_calls = _parse_tool_calls(d.pop("tool_calls", UNSET))

        message = cls(
            id=id,
            type_=type_,
            role=role,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
            model=model,
            tool_calls=tool_calls,
        )

        message.additional_properties = d
        return message

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
