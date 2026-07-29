from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_call_function_arguments import ToolCallFunctionArguments
    from ..models.tool_call_function_result_type_0 import ToolCallFunctionResultType0


T = TypeVar("T", bound="ToolCall")


@_attrs_define
class ToolCall:
    """
    Attributes:
        id (UUID):
        function_name (str):
        function_arguments (ToolCallFunctionArguments):
        created_at (datetime.datetime):
        function_result (None | ToolCallFunctionResultType0 | Unset):
    """

    id: UUID
    function_name: str
    function_arguments: ToolCallFunctionArguments
    created_at: datetime.datetime
    function_result: None | ToolCallFunctionResultType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_call_function_result_type_0 import ToolCallFunctionResultType0

        id = str(self.id)

        function_name = self.function_name

        function_arguments = self.function_arguments.to_dict()

        created_at = self.created_at.isoformat()

        function_result: dict[str, Any] | None | Unset
        if isinstance(self.function_result, Unset):
            function_result = UNSET
        elif isinstance(self.function_result, ToolCallFunctionResultType0):
            function_result = self.function_result.to_dict()
        else:
            function_result = self.function_result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "function_name": function_name,
                "function_arguments": function_arguments,
                "created_at": created_at,
            }
        )
        if function_result is not UNSET:
            field_dict["function_result"] = function_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_call_function_arguments import ToolCallFunctionArguments
        from ..models.tool_call_function_result_type_0 import ToolCallFunctionResultType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        function_name = d.pop("function_name")

        function_arguments = ToolCallFunctionArguments.from_dict(d.pop("function_arguments"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_function_result(data: object) -> None | ToolCallFunctionResultType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                function_result_type_0 = ToolCallFunctionResultType0.from_dict(data)

                return function_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolCallFunctionResultType0 | Unset, data)

        function_result = _parse_function_result(d.pop("function_result", UNSET))

        tool_call = cls(
            id=id,
            function_name=function_name,
            function_arguments=function_arguments,
            created_at=created_at,
            function_result=function_result,
        )

        tool_call.additional_properties = d
        return tool_call

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
