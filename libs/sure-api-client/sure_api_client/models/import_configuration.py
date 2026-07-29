from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportConfiguration")


@_attrs_define
class ImportConfiguration:
    """
    Attributes:
        date_col_label (None | str | Unset):
        amount_col_label (None | str | Unset):
        name_col_label (None | str | Unset):
        category_col_label (None | str | Unset):
        tags_col_label (None | str | Unset):
        notes_col_label (None | str | Unset):
        account_col_label (None | str | Unset):
        date_format (None | str | Unset):
        number_format (None | str | Unset):
        signage_convention (None | str | Unset):
    """

    date_col_label: None | str | Unset = UNSET
    amount_col_label: None | str | Unset = UNSET
    name_col_label: None | str | Unset = UNSET
    category_col_label: None | str | Unset = UNSET
    tags_col_label: None | str | Unset = UNSET
    notes_col_label: None | str | Unset = UNSET
    account_col_label: None | str | Unset = UNSET
    date_format: None | str | Unset = UNSET
    number_format: None | str | Unset = UNSET
    signage_convention: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_col_label: None | str | Unset
        if isinstance(self.date_col_label, Unset):
            date_col_label = UNSET
        else:
            date_col_label = self.date_col_label

        amount_col_label: None | str | Unset
        if isinstance(self.amount_col_label, Unset):
            amount_col_label = UNSET
        else:
            amount_col_label = self.amount_col_label

        name_col_label: None | str | Unset
        if isinstance(self.name_col_label, Unset):
            name_col_label = UNSET
        else:
            name_col_label = self.name_col_label

        category_col_label: None | str | Unset
        if isinstance(self.category_col_label, Unset):
            category_col_label = UNSET
        else:
            category_col_label = self.category_col_label

        tags_col_label: None | str | Unset
        if isinstance(self.tags_col_label, Unset):
            tags_col_label = UNSET
        else:
            tags_col_label = self.tags_col_label

        notes_col_label: None | str | Unset
        if isinstance(self.notes_col_label, Unset):
            notes_col_label = UNSET
        else:
            notes_col_label = self.notes_col_label

        account_col_label: None | str | Unset
        if isinstance(self.account_col_label, Unset):
            account_col_label = UNSET
        else:
            account_col_label = self.account_col_label

        date_format: None | str | Unset
        if isinstance(self.date_format, Unset):
            date_format = UNSET
        else:
            date_format = self.date_format

        number_format: None | str | Unset
        if isinstance(self.number_format, Unset):
            number_format = UNSET
        else:
            number_format = self.number_format

        signage_convention: None | str | Unset
        if isinstance(self.signage_convention, Unset):
            signage_convention = UNSET
        else:
            signage_convention = self.signage_convention

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_col_label is not UNSET:
            field_dict["date_col_label"] = date_col_label
        if amount_col_label is not UNSET:
            field_dict["amount_col_label"] = amount_col_label
        if name_col_label is not UNSET:
            field_dict["name_col_label"] = name_col_label
        if category_col_label is not UNSET:
            field_dict["category_col_label"] = category_col_label
        if tags_col_label is not UNSET:
            field_dict["tags_col_label"] = tags_col_label
        if notes_col_label is not UNSET:
            field_dict["notes_col_label"] = notes_col_label
        if account_col_label is not UNSET:
            field_dict["account_col_label"] = account_col_label
        if date_format is not UNSET:
            field_dict["date_format"] = date_format
        if number_format is not UNSET:
            field_dict["number_format"] = number_format
        if signage_convention is not UNSET:
            field_dict["signage_convention"] = signage_convention

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_date_col_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_col_label = _parse_date_col_label(d.pop("date_col_label", UNSET))

        def _parse_amount_col_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount_col_label = _parse_amount_col_label(d.pop("amount_col_label", UNSET))

        def _parse_name_col_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_col_label = _parse_name_col_label(d.pop("name_col_label", UNSET))

        def _parse_category_col_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_col_label = _parse_category_col_label(d.pop("category_col_label", UNSET))

        def _parse_tags_col_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tags_col_label = _parse_tags_col_label(d.pop("tags_col_label", UNSET))

        def _parse_notes_col_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes_col_label = _parse_notes_col_label(d.pop("notes_col_label", UNSET))

        def _parse_account_col_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_col_label = _parse_account_col_label(d.pop("account_col_label", UNSET))

        def _parse_date_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_format = _parse_date_format(d.pop("date_format", UNSET))

        def _parse_number_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number_format = _parse_number_format(d.pop("number_format", UNSET))

        def _parse_signage_convention(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signage_convention = _parse_signage_convention(d.pop("signage_convention", UNSET))

        import_configuration = cls(
            date_col_label=date_col_label,
            amount_col_label=amount_col_label,
            name_col_label=name_col_label,
            category_col_label=category_col_label,
            tags_col_label=tags_col_label,
            notes_col_label=notes_col_label,
            account_col_label=account_col_label,
            date_format=date_format,
            number_format=number_format,
            signage_convention=signage_convention,
        )

        import_configuration.additional_properties = d
        return import_configuration

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
