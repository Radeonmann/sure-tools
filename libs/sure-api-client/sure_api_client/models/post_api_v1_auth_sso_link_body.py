from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiV1AuthSsoLinkBody")


@_attrs_define
class PostApiV1AuthSsoLinkBody:
    """
    Attributes:
        linking_code (str): One-time linking code from mobile SSO onboarding redirect
        email (str): Email of the existing account to link
        password (str): Password for the existing account
    """

    linking_code: str
    email: str
    password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linking_code = self.linking_code

        email = self.email

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linking_code": linking_code,
                "email": email,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linking_code = d.pop("linking_code")

        email = d.pop("email")

        password = d.pop("password")

        post_api_v1_auth_sso_link_body = cls(
            linking_code=linking_code,
            email=email,
            password=password,
        )

        post_api_v1_auth_sso_link_body.additional_properties = d
        return post_api_v1_auth_sso_link_body

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
