from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_verification_readback_status import ImportVerificationReadbackStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_verification_readback_actual_delta_counts import ImportVerificationReadbackActualDeltaCounts
    from ..models.import_verification_readback_after_counts import ImportVerificationReadbackAfterCounts
    from ..models.import_verification_readback_before_counts import ImportVerificationReadbackBeforeCounts
    from ..models.import_verification_readback_checked_counts import ImportVerificationReadbackCheckedCounts
    from ..models.import_verification_readback_expected_record_counts import (
        ImportVerificationReadbackExpectedRecordCounts,
    )
    from ..models.import_verification_readback_mismatches import ImportVerificationReadbackMismatches


T = TypeVar("T", bound="ImportVerificationReadback")


@_attrs_define
class ImportVerificationReadback:
    """SureImport only. Expected NDJSON counts compared to family-scoped database readback after publish.

    Attributes:
        status (ImportVerificationReadbackStatus | Unset):
        checked_at (datetime.datetime | None | Unset):
        expected_record_counts (ImportVerificationReadbackExpectedRecordCounts | Unset):
        before_counts (ImportVerificationReadbackBeforeCounts | Unset):
        after_counts (ImportVerificationReadbackAfterCounts | Unset):
        actual_delta_counts (ImportVerificationReadbackActualDeltaCounts | Unset):
        checked_counts (ImportVerificationReadbackCheckedCounts | Unset):
        mismatches (ImportVerificationReadbackMismatches | Unset):
        error (None | str | Unset):
    """

    status: ImportVerificationReadbackStatus | Unset = UNSET
    checked_at: datetime.datetime | None | Unset = UNSET
    expected_record_counts: ImportVerificationReadbackExpectedRecordCounts | Unset = UNSET
    before_counts: ImportVerificationReadbackBeforeCounts | Unset = UNSET
    after_counts: ImportVerificationReadbackAfterCounts | Unset = UNSET
    actual_delta_counts: ImportVerificationReadbackActualDeltaCounts | Unset = UNSET
    checked_counts: ImportVerificationReadbackCheckedCounts | Unset = UNSET
    mismatches: ImportVerificationReadbackMismatches | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        checked_at: None | str | Unset
        if isinstance(self.checked_at, Unset):
            checked_at = UNSET
        elif isinstance(self.checked_at, datetime.datetime):
            checked_at = self.checked_at.isoformat()
        else:
            checked_at = self.checked_at

        expected_record_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expected_record_counts, Unset):
            expected_record_counts = self.expected_record_counts.to_dict()

        before_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.before_counts, Unset):
            before_counts = self.before_counts.to_dict()

        after_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.after_counts, Unset):
            after_counts = self.after_counts.to_dict()

        actual_delta_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_delta_counts, Unset):
            actual_delta_counts = self.actual_delta_counts.to_dict()

        checked_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.checked_counts, Unset):
            checked_counts = self.checked_counts.to_dict()

        mismatches: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mismatches, Unset):
            mismatches = self.mismatches.to_dict()

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if checked_at is not UNSET:
            field_dict["checked_at"] = checked_at
        if expected_record_counts is not UNSET:
            field_dict["expected_record_counts"] = expected_record_counts
        if before_counts is not UNSET:
            field_dict["before_counts"] = before_counts
        if after_counts is not UNSET:
            field_dict["after_counts"] = after_counts
        if actual_delta_counts is not UNSET:
            field_dict["actual_delta_counts"] = actual_delta_counts
        if checked_counts is not UNSET:
            field_dict["checked_counts"] = checked_counts
        if mismatches is not UNSET:
            field_dict["mismatches"] = mismatches
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_verification_readback_actual_delta_counts import (
            ImportVerificationReadbackActualDeltaCounts,
        )
        from ..models.import_verification_readback_after_counts import ImportVerificationReadbackAfterCounts
        from ..models.import_verification_readback_before_counts import ImportVerificationReadbackBeforeCounts
        from ..models.import_verification_readback_checked_counts import ImportVerificationReadbackCheckedCounts
        from ..models.import_verification_readback_expected_record_counts import (
            ImportVerificationReadbackExpectedRecordCounts,
        )
        from ..models.import_verification_readback_mismatches import ImportVerificationReadbackMismatches

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ImportVerificationReadbackStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ImportVerificationReadbackStatus(_status)

        def _parse_checked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        checked_at = _parse_checked_at(d.pop("checked_at", UNSET))

        _expected_record_counts = d.pop("expected_record_counts", UNSET)
        expected_record_counts: ImportVerificationReadbackExpectedRecordCounts | Unset
        if isinstance(_expected_record_counts, Unset):
            expected_record_counts = UNSET
        else:
            expected_record_counts = ImportVerificationReadbackExpectedRecordCounts.from_dict(_expected_record_counts)

        _before_counts = d.pop("before_counts", UNSET)
        before_counts: ImportVerificationReadbackBeforeCounts | Unset
        if isinstance(_before_counts, Unset):
            before_counts = UNSET
        else:
            before_counts = ImportVerificationReadbackBeforeCounts.from_dict(_before_counts)

        _after_counts = d.pop("after_counts", UNSET)
        after_counts: ImportVerificationReadbackAfterCounts | Unset
        if isinstance(_after_counts, Unset):
            after_counts = UNSET
        else:
            after_counts = ImportVerificationReadbackAfterCounts.from_dict(_after_counts)

        _actual_delta_counts = d.pop("actual_delta_counts", UNSET)
        actual_delta_counts: ImportVerificationReadbackActualDeltaCounts | Unset
        if isinstance(_actual_delta_counts, Unset):
            actual_delta_counts = UNSET
        else:
            actual_delta_counts = ImportVerificationReadbackActualDeltaCounts.from_dict(_actual_delta_counts)

        _checked_counts = d.pop("checked_counts", UNSET)
        checked_counts: ImportVerificationReadbackCheckedCounts | Unset
        if isinstance(_checked_counts, Unset):
            checked_counts = UNSET
        else:
            checked_counts = ImportVerificationReadbackCheckedCounts.from_dict(_checked_counts)

        _mismatches = d.pop("mismatches", UNSET)
        mismatches: ImportVerificationReadbackMismatches | Unset
        if isinstance(_mismatches, Unset):
            mismatches = UNSET
        else:
            mismatches = ImportVerificationReadbackMismatches.from_dict(_mismatches)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        import_verification_readback = cls(
            status=status,
            checked_at=checked_at,
            expected_record_counts=expected_record_counts,
            before_counts=before_counts,
            after_counts=after_counts,
            actual_delta_counts=actual_delta_counts,
            checked_counts=checked_counts,
            mismatches=mismatches,
            error=error,
        )

        import_verification_readback.additional_properties = d
        return import_verification_readback

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
