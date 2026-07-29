from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reset_status_response_status import ResetStatusResponseStatus

if TYPE_CHECKING:
    from ..models.reset_status_response_counts import ResetStatusResponseCounts


T = TypeVar("T", bound="ResetStatusResponse")


@_attrs_define
class ResetStatusResponse:
    """
    Attributes:
        status (ResetStatusResponseStatus): Counts-based family reset status at response time.
        family_id (UUID): UUID of the family whose reset target counts were checked.
        reset_complete (bool): True when all reset target counts are zero at response time. This is a family data
            snapshot, not a durable per-job completion record.
        counts (ResetStatusResponseCounts):
    """

    status: ResetStatusResponseStatus
    family_id: UUID
    reset_complete: bool
    counts: ResetStatusResponseCounts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        family_id = str(self.family_id)

        reset_complete = self.reset_complete

        counts = self.counts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "family_id": family_id,
                "reset_complete": reset_complete,
                "counts": counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reset_status_response_counts import ResetStatusResponseCounts

        d = dict(src_dict)
        status = ResetStatusResponseStatus(d.pop("status"))

        family_id = UUID(d.pop("family_id"))

        reset_complete = d.pop("reset_complete")

        counts = ResetStatusResponseCounts.from_dict(d.pop("counts"))

        reset_status_response = cls(
            status=status,
            family_id=family_id,
            reset_complete=reset_complete,
            counts=counts,
        )

        reset_status_response.additional_properties = d
        return reset_status_response

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
