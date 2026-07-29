from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_v1_auth_signup_response_201_user import PostApiV1AuthSignupResponse201User


T = TypeVar("T", bound="PostApiV1AuthSignupResponse201")


@_attrs_define
class PostApiV1AuthSignupResponse201:
    """
    Attributes:
        access_token (str | Unset):
        refresh_token (str | Unset):
        token_type (str | Unset):
        expires_in (int | Unset):
        created_at (int | Unset):
        user (PostApiV1AuthSignupResponse201User | Unset):
    """

    access_token: str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    token_type: str | Unset = UNSET
    expires_in: int | Unset = UNSET
    created_at: int | Unset = UNSET
    user: PostApiV1AuthSignupResponse201User | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        refresh_token = self.refresh_token

        token_type = self.token_type

        expires_in = self.expires_in

        created_at = self.created_at

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_v1_auth_signup_response_201_user import PostApiV1AuthSignupResponse201User

        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        token_type = d.pop("token_type", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        created_at = d.pop("created_at", UNSET)

        _user = d.pop("user", UNSET)
        user: PostApiV1AuthSignupResponse201User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PostApiV1AuthSignupResponse201User.from_dict(_user)

        post_api_v1_auth_signup_response_201 = cls(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type=token_type,
            expires_in=expires_in,
            created_at=created_at,
            user=user,
        )

        post_api_v1_auth_signup_response_201.additional_properties = d
        return post_api_v1_auth_signup_response_201

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
