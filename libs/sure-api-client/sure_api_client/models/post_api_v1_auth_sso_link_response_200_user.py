from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_v1_auth_sso_link_response_200_user_ui_layout import PostApiV1AuthSsoLinkResponse200UserUiLayout
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiV1AuthSsoLinkResponse200User")


@_attrs_define
class PostApiV1AuthSsoLinkResponse200User:
    """
    Attributes:
        id (UUID | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        ui_layout (PostApiV1AuthSsoLinkResponse200UserUiLayout | Unset):
        ai_enabled (bool | Unset):
    """

    id: UUID | Unset = UNSET
    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    ui_layout: PostApiV1AuthSsoLinkResponse200UserUiLayout | Unset = UNSET
    ai_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        email = self.email

        first_name = self.first_name

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

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        _ui_layout = d.pop("ui_layout", UNSET)
        ui_layout: PostApiV1AuthSsoLinkResponse200UserUiLayout | Unset
        if isinstance(_ui_layout, Unset):
            ui_layout = UNSET
        else:
            ui_layout = PostApiV1AuthSsoLinkResponse200UserUiLayout(_ui_layout)

        ai_enabled = d.pop("ai_enabled", UNSET)

        post_api_v1_auth_sso_link_response_200_user = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            ui_layout=ui_layout,
            ai_enabled=ai_enabled,
        )

        post_api_v1_auth_sso_link_response_200_user.additional_properties = d
        return post_api_v1_auth_sso_link_response_200_user

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
