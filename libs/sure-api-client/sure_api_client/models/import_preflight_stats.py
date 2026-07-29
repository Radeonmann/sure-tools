from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_preflight_stats_entity_counts_type_0 import ImportPreflightStatsEntityCountsType0
    from ..models.import_preflight_stats_record_type_counts_type_0 import ImportPreflightStatsRecordTypeCountsType0


T = TypeVar("T", bound="ImportPreflightStats")


@_attrs_define
class ImportPreflightStats:
    """
    Attributes:
        rows_count (int): CSV parsed non-header rows, or nonblank Sure NDJSON lines.
        valid_rows_count (int | Unset): SureImport only. Valid NDJSON records.
        invalid_rows_count (int | Unset): SureImport only. Invalid NDJSON records. CSV malformed content returns a 422
            instead.
        entity_counts (ImportPreflightStatsEntityCountsType0 | None | Unset):
        record_type_counts (ImportPreflightStatsRecordTypeCountsType0 | None | Unset):
    """

    rows_count: int
    valid_rows_count: int | Unset = UNSET
    invalid_rows_count: int | Unset = UNSET
    entity_counts: ImportPreflightStatsEntityCountsType0 | None | Unset = UNSET
    record_type_counts: ImportPreflightStatsRecordTypeCountsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.import_preflight_stats_entity_counts_type_0 import ImportPreflightStatsEntityCountsType0
        from ..models.import_preflight_stats_record_type_counts_type_0 import ImportPreflightStatsRecordTypeCountsType0

        rows_count = self.rows_count

        valid_rows_count = self.valid_rows_count

        invalid_rows_count = self.invalid_rows_count

        entity_counts: dict[str, Any] | None | Unset
        if isinstance(self.entity_counts, Unset):
            entity_counts = UNSET
        elif isinstance(self.entity_counts, ImportPreflightStatsEntityCountsType0):
            entity_counts = self.entity_counts.to_dict()
        else:
            entity_counts = self.entity_counts

        record_type_counts: dict[str, Any] | None | Unset
        if isinstance(self.record_type_counts, Unset):
            record_type_counts = UNSET
        elif isinstance(self.record_type_counts, ImportPreflightStatsRecordTypeCountsType0):
            record_type_counts = self.record_type_counts.to_dict()
        else:
            record_type_counts = self.record_type_counts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows_count": rows_count,
            }
        )
        if valid_rows_count is not UNSET:
            field_dict["valid_rows_count"] = valid_rows_count
        if invalid_rows_count is not UNSET:
            field_dict["invalid_rows_count"] = invalid_rows_count
        if entity_counts is not UNSET:
            field_dict["entity_counts"] = entity_counts
        if record_type_counts is not UNSET:
            field_dict["record_type_counts"] = record_type_counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_preflight_stats_entity_counts_type_0 import ImportPreflightStatsEntityCountsType0
        from ..models.import_preflight_stats_record_type_counts_type_0 import ImportPreflightStatsRecordTypeCountsType0

        d = dict(src_dict)
        rows_count = d.pop("rows_count")

        valid_rows_count = d.pop("valid_rows_count", UNSET)

        invalid_rows_count = d.pop("invalid_rows_count", UNSET)

        def _parse_entity_counts(data: object) -> ImportPreflightStatsEntityCountsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                entity_counts_type_0 = ImportPreflightStatsEntityCountsType0.from_dict(data)

                return entity_counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImportPreflightStatsEntityCountsType0 | None | Unset, data)

        entity_counts = _parse_entity_counts(d.pop("entity_counts", UNSET))

        def _parse_record_type_counts(data: object) -> ImportPreflightStatsRecordTypeCountsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_type_counts_type_0 = ImportPreflightStatsRecordTypeCountsType0.from_dict(data)

                return record_type_counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImportPreflightStatsRecordTypeCountsType0 | None | Unset, data)

        record_type_counts = _parse_record_type_counts(d.pop("record_type_counts", UNSET))

        import_preflight_stats = cls(
            rows_count=rows_count,
            valid_rows_count=valid_rows_count,
            invalid_rows_count=invalid_rows_count,
            entity_counts=entity_counts,
            record_type_counts=record_type_counts,
        )

        import_preflight_stats.additional_properties = d
        return import_preflight_stats

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
