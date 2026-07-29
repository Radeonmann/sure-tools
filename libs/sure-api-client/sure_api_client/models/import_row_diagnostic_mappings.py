from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_row_mapping import ImportRowMapping


T = TypeVar("T", bound="ImportRowDiagnosticMappings")


@_attrs_define
class ImportRowDiagnosticMappings:
    """
    Attributes:
        account (ImportRowMapping | Unset):
        category (ImportRowMapping | Unset):
        account_type (ImportRowMapping | Unset):
        tags (list[ImportRowMapping] | Unset):
    """

    account: ImportRowMapping | Unset = UNSET
    category: ImportRowMapping | Unset = UNSET
    account_type: ImportRowMapping | Unset = UNSET
    tags: list[ImportRowMapping] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        account_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.to_dict()

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if category is not UNSET:
            field_dict["category"] = category
        if account_type is not UNSET:
            field_dict["account_type"] = account_type
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_row_mapping import ImportRowMapping

        d = dict(src_dict)
        _account = d.pop("account", UNSET)
        account: ImportRowMapping | Unset
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = ImportRowMapping.from_dict(_account)

        _category = d.pop("category", UNSET)
        category: ImportRowMapping | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ImportRowMapping.from_dict(_category)

        _account_type = d.pop("account_type", UNSET)
        account_type: ImportRowMapping | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = ImportRowMapping.from_dict(_account_type)

        _tags = d.pop("tags", UNSET)
        tags: list[ImportRowMapping] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = ImportRowMapping.from_dict(tags_item_data)

                tags.append(tags_item)

        import_row_diagnostic_mappings = cls(
            account=account,
            category=category,
            account_type=account_type,
            tags=tags,
        )

        import_row_diagnostic_mappings.additional_properties = d
        return import_row_diagnostic_mappings

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
