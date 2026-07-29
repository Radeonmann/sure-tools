from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_summary_status import ImportSummaryStatus
from ..models.import_summary_type import ImportSummaryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_status_summary import ImportStatusSummary


T = TypeVar("T", bound="ImportSummary")


@_attrs_define
class ImportSummary:
    """
    Attributes:
        id (UUID):
        type_ (ImportSummaryType):
        status (ImportSummaryStatus):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        status_detail (ImportStatusSummary):
        account_id (None | Unset | UUID):
        rows_count (int | Unset):
        error (None | str | Unset):
    """

    id: UUID
    type_: ImportSummaryType
    status: ImportSummaryStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status_detail: ImportStatusSummary
    account_id: None | Unset | UUID = UNSET
    rows_count: int | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status_detail = self.status_detail.to_dict()

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        elif isinstance(self.account_id, UUID):
            account_id = str(self.account_id)
        else:
            account_id = self.account_id

        rows_count = self.rows_count

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
                "status_detail": status_detail,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if rows_count is not UNSET:
            field_dict["rows_count"] = rows_count
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_status_summary import ImportStatusSummary

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = ImportSummaryType(d.pop("type"))

        status = ImportSummaryStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        status_detail = ImportStatusSummary.from_dict(d.pop("status_detail"))

        def _parse_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                account_id_type_0 = UUID(data)

                return account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))

        rows_count = d.pop("rows_count", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        import_summary = cls(
            id=id,
            type_=type_,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            status_detail=status_detail,
            account_id=account_id,
            rows_count=rows_count,
            error=error,
        )

        import_summary.additional_properties = d
        return import_summary

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
