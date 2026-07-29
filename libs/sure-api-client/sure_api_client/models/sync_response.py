from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_resource import SyncResource


T = TypeVar("T", bound="SyncResponse")


@_attrs_define
class SyncResponse:
    """
    Attributes:
        data (None | SyncResource):
    """

    data: None | SyncResource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_resource import SyncResource

        data: dict[str, Any] | None
        if isinstance(self.data, SyncResource):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_resource import SyncResource

        d = dict(src_dict)

        def _parse_data(data: object) -> None | SyncResource:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = SyncResource.from_dict(data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SyncResource, data)

        data = _parse_data(d.pop("data"))

        sync_response = cls(
            data=data,
        )

        sync_response.additional_properties = d
        return sync_response

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
