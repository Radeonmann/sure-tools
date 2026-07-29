from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_v1_auth_signup_body_device import PostApiV1AuthSignupBodyDevice
    from ..models.post_api_v1_auth_signup_body_user import PostApiV1AuthSignupBodyUser


T = TypeVar("T", bound="PostApiV1AuthSignupBody")


@_attrs_define
class PostApiV1AuthSignupBody:
    """
    Attributes:
        user (PostApiV1AuthSignupBodyUser):
        device (PostApiV1AuthSignupBodyDevice):
        invite_code (None | str | Unset): Invite code (required when invites are enforced)
    """

    user: PostApiV1AuthSignupBodyUser
    device: PostApiV1AuthSignupBodyDevice
    invite_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        device = self.device.to_dict()

        invite_code: None | str | Unset
        if isinstance(self.invite_code, Unset):
            invite_code = UNSET
        else:
            invite_code = self.invite_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "device": device,
            }
        )
        if invite_code is not UNSET:
            field_dict["invite_code"] = invite_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_v1_auth_signup_body_device import PostApiV1AuthSignupBodyDevice
        from ..models.post_api_v1_auth_signup_body_user import PostApiV1AuthSignupBodyUser

        d = dict(src_dict)
        user = PostApiV1AuthSignupBodyUser.from_dict(d.pop("user"))

        device = PostApiV1AuthSignupBodyDevice.from_dict(d.pop("device"))

        def _parse_invite_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invite_code = _parse_invite_code(d.pop("invite_code", UNSET))

        post_api_v1_auth_signup_body = cls(
            user=user,
            device=device,
            invite_code=invite_code,
        )

        post_api_v1_auth_signup_body.additional_properties = d
        return post_api_v1_auth_signup_body

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
