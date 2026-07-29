from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_summary import ChatSummary
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ChatCollection")


@_attrs_define
class ChatCollection:
    """
    Attributes:
        chats (list[ChatSummary]):
        pagination (Pagination):
    """

    chats: list[ChatSummary]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chats = []
        for chats_item_data in self.chats:
            chats_item = chats_item_data.to_dict()
            chats.append(chats_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chats": chats,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_summary import ChatSummary
        from ..models.pagination import Pagination

        d = dict(src_dict)
        chats = []
        _chats = d.pop("chats")
        for chats_item_data in _chats:
            chats_item = ChatSummary.from_dict(chats_item_data)

            chats.append(chats_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        chat_collection = cls(
            chats=chats,
            pagination=pagination,
        )

        chat_collection.additional_properties = d
        return chat_collection

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
