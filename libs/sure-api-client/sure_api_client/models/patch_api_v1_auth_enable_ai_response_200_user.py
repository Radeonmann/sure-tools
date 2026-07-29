from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_v1_auth_enable_ai_response_200_user_ui_layout import (
    PatchApiV1AuthEnableAiResponse200UserUiLayout,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiV1AuthEnableAiResponse200User")


@_attrs_define
class PatchApiV1AuthEnableAiResponse200User:
    """
    Attributes:
        id (UUID | Unset):
        email (str | Unset):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
        ui_layout (PatchApiV1AuthEnableAiResponse200UserUiLayout | Unset):
        ai_enabled (bool | Unset):
    """

    id: UUID | Unset = UNSET
    email: str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    ui_layout: PatchApiV1AuthEnableAiResponse200UserUiLayout | Unset = UNSET
    ai_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        ui_layout: str | Unset = UNSET
        if not isinstance(self.ui_layout, Unset):
            ui_layout = self.ui_layout.value

        ai_enabled = self.ai_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if ui_layout is not UNSET:
            field_dict["ui_layout"] = ui_layout
        if ai_enabled is not UNSET:
            field_dict["ai_enabled"] = ai_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        email = d.pop("email", UNSET)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        _ui_layout = d.pop("ui_layout", UNSET)
        ui_layout: PatchApiV1AuthEnableAiResponse200UserUiLayout | Unset
        if isinstance(_ui_layout, Unset):
            ui_layout = UNSET
        else:
            ui_layout = PatchApiV1AuthEnableAiResponse200UserUiLayout(_ui_layout)

        ai_enabled = d.pop("ai_enabled", UNSET)

        patch_api_v1_auth_enable_ai_response_200_user = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            ui_layout=ui_layout,
            ai_enabled=ai_enabled,
        )

        patch_api_v1_auth_enable_ai_response_200_user.additional_properties = d
        return patch_api_v1_auth_enable_ai_response_200_user

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
