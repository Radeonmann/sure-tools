from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiV1AuthSsoCreateAccountBody")


@_attrs_define
class PostApiV1AuthSsoCreateAccountBody:
    """
    Attributes:
        linking_code (str): One-time linking code from mobile SSO onboarding redirect
        first_name (str | Unset): First name (overrides value from SSO provider if provided)
        last_name (str | Unset): Last name (overrides value from SSO provider if provided)
    """

    linking_code: str
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linking_code = self.linking_code

        first_name = self.first_name

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linking_code": linking_code,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linking_code = d.pop("linking_code")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        post_api_v1_auth_sso_create_account_body = cls(
            linking_code=linking_code,
            first_name=first_name,
            last_name=last_name,
        )

        post_api_v1_auth_sso_create_account_body.additional_properties = d
        return post_api_v1_auth_sso_create_account_body

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
