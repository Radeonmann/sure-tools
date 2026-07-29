from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_verification_expected_record_counts import ImportVerificationExpectedRecordCounts
    from ..models.import_verification_readback import ImportVerificationReadback


T = TypeVar("T", bound="ImportVerification")


@_attrs_define
class ImportVerification:
    """SureImport only. Captured at upload and completed after import publish.

    Attributes:
        expected_record_counts (ImportVerificationExpectedRecordCounts):
        readback (ImportVerificationReadback): SureImport only. Expected NDJSON counts compared to family-scoped
            database readback after publish.
    """

    expected_record_counts: ImportVerificationExpectedRecordCounts
    readback: ImportVerificationReadback
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_record_counts = self.expected_record_counts.to_dict()

        readback = self.readback.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expected_record_counts": expected_record_counts,
                "readback": readback,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_verification_expected_record_counts import ImportVerificationExpectedRecordCounts
        from ..models.import_verification_readback import ImportVerificationReadback

        d = dict(src_dict)
        expected_record_counts = ImportVerificationExpectedRecordCounts.from_dict(d.pop("expected_record_counts"))

        readback = ImportVerificationReadback.from_dict(d.pop("readback"))

        import_verification = cls(
            expected_record_counts=expected_record_counts,
            readback=readback,
        )

        import_verification.additional_properties = d
        return import_verification

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
