from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_response_ai_response_status import MessageResponseAiResponseStatus
from ..models.message_role import MessageRole
from ..models.message_type import MessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_call import ToolCall


T = TypeVar("T", bound="MessageResponse")


@_attrs_define
class MessageResponse:
    """
    Attributes:
        id (UUID):
        type_ (MessageType):
        role (MessageRole):
        content (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        chat_id (UUID):
        model (None | str | Unset):
        tool_calls (list[ToolCall] | None | Unset):
        ai_response_status (MessageResponseAiResponseStatus | Unset):
        ai_response_message (None | str | Unset):
    """

    id: UUID
    type_: MessageType
    role: MessageRole
    content: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    chat_id: UUID
    model: None | str | Unset = UNSET
    tool_calls: list[ToolCall] | None | Unset = UNSET
    ai_response_status: MessageResponseAiResponseStatus | Unset = UNSET
    ai_response_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        role = self.role.value

        content = self.content

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        chat_id = str(self.chat_id)

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

        ai_response_status: str | Unset = UNSET
        if not isinstance(self.ai_response_status, Unset):
            ai_response_status = self.ai_response_status.value

        ai_response_message: None | str | Unset
        if isinstance(self.ai_response_message, Unset):
            ai_response_message = UNSET
        else:
            ai_response_message = self.ai_response_message

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
                "chat_id": chat_id,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls
        if ai_response_status is not UNSET:
            field_dict["ai_response_status"] = ai_response_status
        if ai_response_message is not UNSET:
            field_dict["ai_response_message"] = ai_response_message

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

        chat_id = UUID(d.pop("chat_id"))

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

        _ai_response_status = d.pop("ai_response_status", UNSET)
        ai_response_status: MessageResponseAiResponseStatus | Unset
        if isinstance(_ai_response_status, Unset):
            ai_response_status = UNSET
        else:
            ai_response_status = MessageResponseAiResponseStatus(_ai_response_status)

        def _parse_ai_response_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ai_response_message = _parse_ai_response_message(d.pop("ai_response_message", UNSET))

        message_response = cls(
            id=id,
            type_=type_,
            role=role,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
            chat_id=chat_id,
            model=model,
            tool_calls=tool_calls,
            ai_response_status=ai_response_status,
            ai_response_message=ai_response_message,
        )

        message_response.additional_properties = d
        return message_response

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
