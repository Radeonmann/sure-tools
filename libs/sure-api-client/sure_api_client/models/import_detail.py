from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_detail_status import ImportDetailStatus
from ..models.import_detail_type import ImportDetailType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_configuration import ImportConfiguration
    from ..models.import_stats import ImportStats
    from ..models.import_status_detail import ImportStatusDetail
    from ..models.import_verification import ImportVerification


T = TypeVar("T", bound="ImportDetail")


@_attrs_define
class ImportDetail:
    """
    Attributes:
        id (UUID):
        type_ (ImportDetailType):
        status (ImportDetailStatus):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        status_detail (ImportStatusDetail):
        configuration (ImportConfiguration):
        stats (ImportStats):
        account_id (None | Unset | UUID):
        error (None | str | Unset):
        verification (ImportVerification | Unset): SureImport only. Captured at upload and completed after import
            publish.
    """

    id: UUID
    type_: ImportDetailType
    status: ImportDetailStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status_detail: ImportStatusDetail
    configuration: ImportConfiguration
    stats: ImportStats
    account_id: None | Unset | UUID = UNSET
    error: None | str | Unset = UNSET
    verification: ImportVerification | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_.value

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status_detail = self.status_detail.to_dict()

        configuration = self.configuration.to_dict()

        stats = self.stats.to_dict()

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        elif isinstance(self.account_id, UUID):
            account_id = str(self.account_id)
        else:
            account_id = self.account_id

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

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
                "configuration": configuration,
                "stats": stats,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if error is not UNSET:
            field_dict["error"] = error
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_configuration import ImportConfiguration
        from ..models.import_stats import ImportStats
        from ..models.import_status_detail import ImportStatusDetail
        from ..models.import_verification import ImportVerification

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = ImportDetailType(d.pop("type"))

        status = ImportDetailStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        status_detail = ImportStatusDetail.from_dict(d.pop("status_detail"))

        configuration = ImportConfiguration.from_dict(d.pop("configuration"))

        stats = ImportStats.from_dict(d.pop("stats"))

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

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        _verification = d.pop("verification", UNSET)
        verification: ImportVerification | Unset
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = ImportVerification.from_dict(_verification)

        import_detail = cls(
            id=id,
            type_=type_,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            status_detail=status_detail,
            configuration=configuration,
            stats=stats,
            account_id=account_id,
            error=error,
            verification=verification,
        )

        import_detail.additional_properties = d
        return import_detail

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
