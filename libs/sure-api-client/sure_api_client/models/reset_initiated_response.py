from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reset_initiated_response_status import ResetInitiatedResponseStatus

T = TypeVar("T", bound="ResetInitiatedResponse")


@_attrs_define
class ResetInitiatedResponse:
    """
    Attributes:
        message (str):
        status (ResetInitiatedResponseStatus):
        job_id (str): Informational Active Job identifier returned by the queue adapter; reset status is family-scoped,
            not job-scoped.
        family_id (UUID): UUID of the family being reset.
        status_url (str):
    """

    message: str
    status: ResetInitiatedResponseStatus
    job_id: str
    family_id: UUID
    status_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status = self.status.value

        job_id = self.job_id

        family_id = str(self.family_id)

        status_url = self.status_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "status": status,
                "job_id": job_id,
                "family_id": family_id,
                "status_url": status_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        status = ResetInitiatedResponseStatus(d.pop("status"))

        job_id = d.pop("job_id")

        family_id = UUID(d.pop("family_id"))

        status_url = d.pop("status_url")

        reset_initiated_response = cls(
            message=message,
            status=status,
            job_id=job_id,
            family_id=family_id,
            status_url=status_url,
        )

        reset_initiated_response.additional_properties = d
        return reset_initiated_response

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
