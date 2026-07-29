from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.family_export_status import FamilyExportStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.family_export_file import FamilyExportFile


T = TypeVar("T", bound="FamilyExport")


@_attrs_define
class FamilyExport:
    """
    Attributes:
        id (UUID):
        status (FamilyExportStatus):
        filename (str):
        downloadable (bool):
        file (FamilyExportFile):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        download_path (None | str | Unset):
    """

    id: UUID
    status: FamilyExportStatus
    filename: str
    downloadable: bool
    file: FamilyExportFile
    created_at: datetime.datetime
    updated_at: datetime.datetime
    download_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status.value

        filename = self.filename

        downloadable = self.downloadable

        file = self.file.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        download_path: None | str | Unset
        if isinstance(self.download_path, Unset):
            download_path = UNSET
        else:
            download_path = self.download_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "filename": filename,
                "downloadable": downloadable,
                "file": file,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if download_path is not UNSET:
            field_dict["download_path"] = download_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.family_export_file import FamilyExportFile

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = FamilyExportStatus(d.pop("status"))

        filename = d.pop("filename")

        downloadable = d.pop("downloadable")

        file = FamilyExportFile.from_dict(d.pop("file"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_download_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        download_path = _parse_download_path(d.pop("download_path", UNSET))

        family_export = cls(
            id=id,
            status=status,
            filename=filename,
            downloadable=downloadable,
            file=file,
            created_at=created_at,
            updated_at=updated_at,
            download_path=download_path,
        )

        family_export.additional_properties = d
        return family_export

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
