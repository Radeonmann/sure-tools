from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_preflight_type import ImportPreflightType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_preflight_content import ImportPreflightContent
    from ..models.import_preflight_error import ImportPreflightError
    from ..models.import_preflight_stats import ImportPreflightStats


T = TypeVar("T", bound="ImportPreflight")


@_attrs_define
class ImportPreflight:
    """
    Attributes:
        type_ (ImportPreflightType):
        valid (bool):
        content (ImportPreflightContent):
        stats (ImportPreflightStats):
        errors (list[ImportPreflightError]):
        warnings (list[str]):
        headers (list[str] | None | Unset):
        required_headers (list[str] | None | Unset):
        missing_required_headers (list[str] | None | Unset):
    """

    type_: ImportPreflightType
    valid: bool
    content: ImportPreflightContent
    stats: ImportPreflightStats
    errors: list[ImportPreflightError]
    warnings: list[str]
    headers: list[str] | None | Unset = UNSET
    required_headers: list[str] | None | Unset = UNSET
    missing_required_headers: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        valid = self.valid

        content = self.content.to_dict()

        stats = self.stats.to_dict()

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        warnings = self.warnings

        headers: list[str] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, list):
            headers = self.headers

        else:
            headers = self.headers

        required_headers: list[str] | None | Unset
        if isinstance(self.required_headers, Unset):
            required_headers = UNSET
        elif isinstance(self.required_headers, list):
            required_headers = self.required_headers

        else:
            required_headers = self.required_headers

        missing_required_headers: list[str] | None | Unset
        if isinstance(self.missing_required_headers, Unset):
            missing_required_headers = UNSET
        elif isinstance(self.missing_required_headers, list):
            missing_required_headers = self.missing_required_headers

        else:
            missing_required_headers = self.missing_required_headers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "valid": valid,
                "content": content,
                "stats": stats,
                "errors": errors,
                "warnings": warnings,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if required_headers is not UNSET:
            field_dict["required_headers"] = required_headers
        if missing_required_headers is not UNSET:
            field_dict["missing_required_headers"] = missing_required_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_preflight_content import ImportPreflightContent
        from ..models.import_preflight_error import ImportPreflightError
        from ..models.import_preflight_stats import ImportPreflightStats

        d = dict(src_dict)
        type_ = ImportPreflightType(d.pop("type"))

        valid = d.pop("valid")

        content = ImportPreflightContent.from_dict(d.pop("content"))

        stats = ImportPreflightStats.from_dict(d.pop("stats"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = ImportPreflightError.from_dict(errors_item_data)

            errors.append(errors_item)

        warnings = cast(list[str], d.pop("warnings"))

        def _parse_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                headers_type_0 = cast(list[str], data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        def _parse_required_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_headers_type_0 = cast(list[str], data)

                return required_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        required_headers = _parse_required_headers(d.pop("required_headers", UNSET))

        def _parse_missing_required_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_required_headers_type_0 = cast(list[str], data)

                return missing_required_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        missing_required_headers = _parse_missing_required_headers(d.pop("missing_required_headers", UNSET))

        import_preflight = cls(
            type_=type_,
            valid=valid,
            content=content,
            stats=stats,
            errors=errors,
            warnings=warnings,
            headers=headers,
            required_headers=required_headers,
            missing_required_headers=missing_required_headers,
        )

        import_preflight.additional_properties = d
        return import_preflight

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
