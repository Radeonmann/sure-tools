from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_v1_auth_login_body_device import PostApiV1AuthLoginBodyDevice


T = TypeVar("T", bound="PostApiV1AuthLoginBody")


@_attrs_define
class PostApiV1AuthLoginBody:
    """
    Attributes:
        email (str):
        password (str):
        device (PostApiV1AuthLoginBodyDevice):
        otp_code (None | str | Unset): TOTP code if MFA is enabled
    """

    email: str
    password: str
    device: PostApiV1AuthLoginBodyDevice
    otp_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password = self.password

        device = self.device.to_dict()

        otp_code: None | str | Unset
        if isinstance(self.otp_code, Unset):
            otp_code = UNSET
        else:
            otp_code = self.otp_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
                "device": device,
            }
        )
        if otp_code is not UNSET:
            field_dict["otp_code"] = otp_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_v1_auth_login_body_device import PostApiV1AuthLoginBodyDevice

        d = dict(src_dict)
        email = d.pop("email")

        password = d.pop("password")

        device = PostApiV1AuthLoginBodyDevice.from_dict(d.pop("device"))

        def _parse_otp_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        otp_code = _parse_otp_code(d.pop("otp_code", UNSET))

        post_api_v1_auth_login_body = cls(
            email=email,
            password=password,
            device=device,
            otp_code=otp_code,
        )

        post_api_v1_auth_login_body.additional_properties = d
        return post_api_v1_auth_login_body

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
