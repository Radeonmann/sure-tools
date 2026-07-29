from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_v1_auth_refresh_body_device import PostApiV1AuthRefreshBodyDevice


T = TypeVar("T", bound="PostApiV1AuthRefreshBody")


@_attrs_define
class PostApiV1AuthRefreshBody:
    """
    Attributes:
        refresh_token (str): The refresh token from a previous login or refresh
        device (PostApiV1AuthRefreshBodyDevice):
    """

    refresh_token: str
    device: PostApiV1AuthRefreshBodyDevice
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        refresh_token = self.refresh_token

        device = self.device.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refresh_token": refresh_token,
                "device": device,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_v1_auth_refresh_body_device import PostApiV1AuthRefreshBodyDevice

        d = dict(src_dict)
        refresh_token = d.pop("refresh_token")

        device = PostApiV1AuthRefreshBodyDevice.from_dict(d.pop("device"))

        post_api_v1_auth_refresh_body = cls(
            refresh_token=refresh_token,
            device=device,
        )

        post_api_v1_auth_refresh_body.additional_properties = d
        return post_api_v1_auth_refresh_body

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
