from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_details_type_1 import ErrorResponseDetailsType1


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        error (str):
        message (None | str | Unset):
        details (ErrorResponseDetailsType1 | list[str] | None | Unset):
        errors (list[str] | None | Unset): Validation error messages (alternative to details used by trades, valuations,
            etc.)
    """

    error: str
    message: None | str | Unset = UNSET
    details: ErrorResponseDetailsType1 | list[str] | None | Unset = UNSET
    errors: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.error_response_details_type_1 import ErrorResponseDetailsType1

        error = self.error

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        details: dict[str, Any] | list[str] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details

        elif isinstance(self.details, ErrorResponseDetailsType1):
            details = self.details.to_dict()
        else:
            details = self.details

        errors: list[str] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = self.errors

        else:
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response_details_type_1 import ErrorResponseDetailsType1

        d = dict(src_dict)
        error = d.pop("error")

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_details(data: object) -> ErrorResponseDetailsType1 | list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[str], data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_1 = ErrorResponseDetailsType1.from_dict(data)

                return details_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ErrorResponseDetailsType1 | list[str] | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_errors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = cast(list[str], data)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        error_response = cls(
            error=error,
            message=message,
            details=details,
            errors=errors,
        )

        error_response.additional_properties = d
        return error_response

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
