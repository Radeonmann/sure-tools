from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiV1AuthLoginBodyDevice")


@_attrs_define
class PostApiV1AuthLoginBodyDevice:
    """
    Attributes:
        device_id (str):
        device_name (str):
        device_type (str):
        os_version (str):
        app_version (str):
    """

    device_id: str
    device_name: str
    device_type: str
    os_version: str
    app_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        device_name = self.device_name

        device_type = self.device_type

        os_version = self.os_version

        app_version = self.app_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device_id": device_id,
                "device_name": device_name,
                "device_type": device_type,
                "os_version": os_version,
                "app_version": app_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_id = d.pop("device_id")

        device_name = d.pop("device_name")

        device_type = d.pop("device_type")

        os_version = d.pop("os_version")

        app_version = d.pop("app_version")

        post_api_v1_auth_login_body_device = cls(
            device_id=device_id,
            device_name=device_name,
            device_type=device_type,
            os_version=os_version,
            app_version=app_version,
        )

        post_api_v1_auth_login_body_device.additional_properties = d
        return post_api_v1_auth_login_body_device

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
