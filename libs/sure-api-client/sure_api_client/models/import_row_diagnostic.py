from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_row_diagnostic_fields import ImportRowDiagnosticFields
    from ..models.import_row_diagnostic_mappings import ImportRowDiagnosticMappings


T = TypeVar("T", bound="ImportRowDiagnostic")


@_attrs_define
class ImportRowDiagnostic:
    """
    Attributes:
        id (UUID):
        row_number (int):
        valid (bool):
        errors (list[str]):
        fields (ImportRowDiagnosticFields):
        mappings (ImportRowDiagnosticMappings):
    """

    id: UUID
    row_number: int
    valid: bool
    errors: list[str]
    fields: ImportRowDiagnosticFields
    mappings: ImportRowDiagnosticMappings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        row_number = self.row_number

        valid = self.valid

        errors = self.errors

        fields = self.fields.to_dict()

        mappings = self.mappings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "row_number": row_number,
                "valid": valid,
                "errors": errors,
                "fields": fields,
                "mappings": mappings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_row_diagnostic_fields import ImportRowDiagnosticFields
        from ..models.import_row_diagnostic_mappings import ImportRowDiagnosticMappings

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        row_number = d.pop("row_number")

        valid = d.pop("valid")

        errors = cast(list[str], d.pop("errors"))

        fields = ImportRowDiagnosticFields.from_dict(d.pop("fields"))

        mappings = ImportRowDiagnosticMappings.from_dict(d.pop("mappings"))

        import_row_diagnostic = cls(
            id=id,
            row_number=row_number,
            valid=valid,
            errors=errors,
            fields=fields,
            mappings=mappings,
        )

        import_row_diagnostic.additional_properties = d
        return import_row_diagnostic

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
