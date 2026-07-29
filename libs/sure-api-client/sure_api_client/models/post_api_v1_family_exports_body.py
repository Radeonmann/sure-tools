from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostApiV1FamilyExportsBody")


@_attrs_define
class PostApiV1FamilyExportsBody:
    """Family export creation does not accept request parameters."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        post_api_v1_family_exports_body = cls()

        return post_api_v1_family_exports_body
