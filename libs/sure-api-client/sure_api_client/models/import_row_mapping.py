from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_row_mapping_mappable_type_0 import ImportRowMappingMappableType0


T = TypeVar("T", bound="ImportRowMapping")


@_attrs_define
class ImportRowMapping:
    """
    Attributes:
        key (None | str):
        type_ (str):
        value (None | str):
        create_when_empty (bool):
        creatable (bool):
        mappable (ImportRowMappingMappableType0 | None):
    """

    key: None | str
    type_: str
    value: None | str
    create_when_empty: bool
    creatable: bool
    mappable: ImportRowMappingMappableType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.import_row_mapping_mappable_type_0 import ImportRowMappingMappableType0

        key: None | str
        key = self.key

        type_ = self.type_

        value: None | str
        value = self.value

        create_when_empty = self.create_when_empty

        creatable = self.creatable

        mappable: dict[str, Any] | None
        if isinstance(self.mappable, ImportRowMappingMappableType0):
            mappable = self.mappable.to_dict()
        else:
            mappable = self.mappable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "type": type_,
                "value": value,
                "create_when_empty": create_when_empty,
                "creatable": creatable,
                "mappable": mappable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_row_mapping_mappable_type_0 import ImportRowMappingMappableType0

        d = dict(src_dict)

        def _parse_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key = _parse_key(d.pop("key"))

        type_ = d.pop("type")

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        create_when_empty = d.pop("create_when_empty")

        creatable = d.pop("creatable")

        def _parse_mappable(data: object) -> ImportRowMappingMappableType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mappable_type_0 = ImportRowMappingMappableType0.from_dict(data)

                return mappable_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImportRowMappingMappableType0 | None, data)

        mappable = _parse_mappable(d.pop("mappable"))

        import_row_mapping = cls(
            key=key,
            type_=type_,
            value=value,
            create_when_empty=create_when_empty,
            creatable=creatable,
            mappable=mappable,
        )

        import_row_mapping.additional_properties = d
        return import_row_mapping

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
