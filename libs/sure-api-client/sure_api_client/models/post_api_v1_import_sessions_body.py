from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_v1_import_sessions_body_type import PostApiV1ImportSessionsBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiV1ImportSessionsBody")


@_attrs_define
class PostApiV1ImportSessionsBody:
    """
    Attributes:
        type_ (PostApiV1ImportSessionsBodyType | Unset): Import session type. Only SureImport is supported.
        client_session_id (None | str | Unset): Client-provided idempotency key for the full import session.
        expected_chunks (int | None | Unset): Expected number of ordered chunks before publish is allowed.
    """

    type_: PostApiV1ImportSessionsBodyType | Unset = UNSET
    client_session_id: None | str | Unset = UNSET
    expected_chunks: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        client_session_id: None | str | Unset
        if isinstance(self.client_session_id, Unset):
            client_session_id = UNSET
        else:
            client_session_id = self.client_session_id

        expected_chunks: int | None | Unset
        if isinstance(self.expected_chunks, Unset):
            expected_chunks = UNSET
        else:
            expected_chunks = self.expected_chunks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if client_session_id is not UNSET:
            field_dict["client_session_id"] = client_session_id
        if expected_chunks is not UNSET:
            field_dict["expected_chunks"] = expected_chunks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: PostApiV1ImportSessionsBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PostApiV1ImportSessionsBodyType(_type_)

        def _parse_client_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_session_id = _parse_client_session_id(d.pop("client_session_id", UNSET))

        def _parse_expected_chunks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_chunks = _parse_expected_chunks(d.pop("expected_chunks", UNSET))

        post_api_v1_import_sessions_body = cls(
            type_=type_,
            client_session_id=client_session_id,
            expected_chunks=expected_chunks,
        )

        post_api_v1_import_sessions_body.additional_properties = d
        return post_api_v1_import_sessions_body

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
