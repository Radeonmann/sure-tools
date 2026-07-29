from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_v1_tags_body_tag import PostApiV1TagsBodyTag


T = TypeVar("T", bound="PostApiV1TagsBody")


@_attrs_define
class PostApiV1TagsBody:
    """
    Attributes:
        tag (PostApiV1TagsBodyTag):
    """

    tag: PostApiV1TagsBodyTag
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag = self.tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_v1_tags_body_tag import PostApiV1TagsBodyTag

        d = dict(src_dict)
        tag = PostApiV1TagsBodyTag.from_dict(d.pop("tag"))

        post_api_v1_tags_body = cls(
            tag=tag,
        )

        post_api_v1_tags_body.additional_properties = d
        return post_api_v1_tags_body

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
