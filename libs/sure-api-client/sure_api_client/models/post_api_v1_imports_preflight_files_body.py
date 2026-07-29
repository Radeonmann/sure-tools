from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.post_api_v1_imports_preflight_files_body_amount_type_strategy import (
    PostApiV1ImportsPreflightFilesBodyAmountTypeStrategy,
)
from ..models.post_api_v1_imports_preflight_files_body_col_sep import PostApiV1ImportsPreflightFilesBodyColSep
from ..models.post_api_v1_imports_preflight_files_body_number_format import (
    PostApiV1ImportsPreflightFilesBodyNumberFormat,
)
from ..models.post_api_v1_imports_preflight_files_body_signage_convention import (
    PostApiV1ImportsPreflightFilesBodySignageConvention,
)
from ..models.post_api_v1_imports_preflight_files_body_type import PostApiV1ImportsPreflightFilesBodyType
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostApiV1ImportsPreflightFilesBody")


@_attrs_define
class PostApiV1ImportsPreflightFilesBody:
    """
    Attributes:
        raw_file_content (str | Unset): Raw CSV or Sure NDJSON content as a string. CSV content is limited to 10MB.
        file (File | Unset): CSV or Sure NDJSON upload when using multipart/form-data. CSV files are limited to 10MB.
        type_ (PostApiV1ImportsPreflightFilesBodyType | Unset): Import type to validate (defaults to TransactionImport)
        account_id (UUID | Unset): Account ID used for account-scoped CSV import validation
        date_col_label (str | Unset): CSV imports only. Header name for the date column
        amount_col_label (str | Unset): CSV imports only. Header name for the amount column
        name_col_label (str | Unset): CSV imports only. Header name for the transaction name column
        category_col_label (str | Unset): CSV imports only. Header name for the category column
        tags_col_label (str | Unset): CSV imports only. Header name for the tags column
        notes_col_label (str | Unset): CSV imports only. Header name for the notes column
        account_col_label (str | Unset): CSV imports only. Header name for the account column
        qty_col_label (str | Unset): CSV trade imports only. Header name for the quantity column
        ticker_col_label (str | Unset): CSV trade imports only. Header name for the ticker column
        price_col_label (str | Unset): CSV trade imports only. Header name for the price column
        entity_type_col_label (str | Unset): CSV imports only. Header name for the entity type column
        currency_col_label (str | Unset): CSV imports only. Header name for the currency column
        exchange_operating_mic_col_label (str | Unset): CSV trade imports only. Header name for the exchange operating
            MIC column
        date_format (str | Unset): CSV imports only. Date format pattern
        number_format (PostApiV1ImportsPreflightFilesBodyNumberFormat | Unset): CSV imports only. Number format for
            parsing amounts
        signage_convention (PostApiV1ImportsPreflightFilesBodySignageConvention | Unset): CSV imports only. How to
            interpret positive/negative amounts
        col_sep (PostApiV1ImportsPreflightFilesBodyColSep | Unset): CSV imports only. Column separator
        rows_to_skip (int | Unset): CSV imports only. Number of leading rows to skip before reading headers
        amount_type_strategy (PostApiV1ImportsPreflightFilesBodyAmountTypeStrategy | Unset): CSV imports only. Amount
            parsing strategy
        amount_type_inflow_value (str | Unset): CSV imports only. Column value that marks an amount as an inflow when
            using custom_column strategy
    """

    raw_file_content: str | Unset = UNSET
    file: File | Unset = UNSET
    type_: PostApiV1ImportsPreflightFilesBodyType | Unset = UNSET
    account_id: UUID | Unset = UNSET
    date_col_label: str | Unset = UNSET
    amount_col_label: str | Unset = UNSET
    name_col_label: str | Unset = UNSET
    category_col_label: str | Unset = UNSET
    tags_col_label: str | Unset = UNSET
    notes_col_label: str | Unset = UNSET
    account_col_label: str | Unset = UNSET
    qty_col_label: str | Unset = UNSET
    ticker_col_label: str | Unset = UNSET
    price_col_label: str | Unset = UNSET
    entity_type_col_label: str | Unset = UNSET
    currency_col_label: str | Unset = UNSET
    exchange_operating_mic_col_label: str | Unset = UNSET
    date_format: str | Unset = UNSET
    number_format: PostApiV1ImportsPreflightFilesBodyNumberFormat | Unset = UNSET
    signage_convention: PostApiV1ImportsPreflightFilesBodySignageConvention | Unset = UNSET
    col_sep: PostApiV1ImportsPreflightFilesBodyColSep | Unset = UNSET
    rows_to_skip: int | Unset = UNSET
    amount_type_strategy: PostApiV1ImportsPreflightFilesBodyAmountTypeStrategy | Unset = UNSET
    amount_type_inflow_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        raw_file_content = self.raw_file_content

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        account_id: str | Unset = UNSET
        if not isinstance(self.account_id, Unset):
            account_id = str(self.account_id)

        date_col_label = self.date_col_label

        amount_col_label = self.amount_col_label

        name_col_label = self.name_col_label

        category_col_label = self.category_col_label

        tags_col_label = self.tags_col_label

        notes_col_label = self.notes_col_label

        account_col_label = self.account_col_label

        qty_col_label = self.qty_col_label

        ticker_col_label = self.ticker_col_label

        price_col_label = self.price_col_label

        entity_type_col_label = self.entity_type_col_label

        currency_col_label = self.currency_col_label

        exchange_operating_mic_col_label = self.exchange_operating_mic_col_label

        date_format = self.date_format

        number_format: str | Unset = UNSET
        if not isinstance(self.number_format, Unset):
            number_format = self.number_format.value

        signage_convention: str | Unset = UNSET
        if not isinstance(self.signage_convention, Unset):
            signage_convention = self.signage_convention.value

        col_sep: str | Unset = UNSET
        if not isinstance(self.col_sep, Unset):
            col_sep = self.col_sep.value

        rows_to_skip = self.rows_to_skip

        amount_type_strategy: str | Unset = UNSET
        if not isinstance(self.amount_type_strategy, Unset):
            amount_type_strategy = self.amount_type_strategy.value

        amount_type_inflow_value = self.amount_type_inflow_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if raw_file_content is not UNSET:
            field_dict["raw_file_content"] = raw_file_content
        if file is not UNSET:
            field_dict["file"] = file
        if type_ is not UNSET:
            field_dict["type"] = type_
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
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
        if qty_col_label is not UNSET:
            field_dict["qty_col_label"] = qty_col_label
        if ticker_col_label is not UNSET:
            field_dict["ticker_col_label"] = ticker_col_label
        if price_col_label is not UNSET:
            field_dict["price_col_label"] = price_col_label
        if entity_type_col_label is not UNSET:
            field_dict["entity_type_col_label"] = entity_type_col_label
        if currency_col_label is not UNSET:
            field_dict["currency_col_label"] = currency_col_label
        if exchange_operating_mic_col_label is not UNSET:
            field_dict["exchange_operating_mic_col_label"] = exchange_operating_mic_col_label
        if date_format is not UNSET:
            field_dict["date_format"] = date_format
        if number_format is not UNSET:
            field_dict["number_format"] = number_format
        if signage_convention is not UNSET:
            field_dict["signage_convention"] = signage_convention
        if col_sep is not UNSET:
            field_dict["col_sep"] = col_sep
        if rows_to_skip is not UNSET:
            field_dict["rows_to_skip"] = rows_to_skip
        if amount_type_strategy is not UNSET:
            field_dict["amount_type_strategy"] = amount_type_strategy
        if amount_type_inflow_value is not UNSET:
            field_dict["amount_type_inflow_value"] = amount_type_inflow_value

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.raw_file_content, Unset):
            files.append(("raw_file_content", (None, str(self.raw_file_content).encode(), "text/plain")))

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        if not isinstance(self.type_, Unset):
            files.append(("type", (None, str(self.type_.value).encode(), "text/plain")))

        if not isinstance(self.account_id, Unset):
            files.append(("account_id", (None, str(self.account_id), "text/plain")))

        if not isinstance(self.date_col_label, Unset):
            files.append(("date_col_label", (None, str(self.date_col_label).encode(), "text/plain")))

        if not isinstance(self.amount_col_label, Unset):
            files.append(("amount_col_label", (None, str(self.amount_col_label).encode(), "text/plain")))

        if not isinstance(self.name_col_label, Unset):
            files.append(("name_col_label", (None, str(self.name_col_label).encode(), "text/plain")))

        if not isinstance(self.category_col_label, Unset):
            files.append(("category_col_label", (None, str(self.category_col_label).encode(), "text/plain")))

        if not isinstance(self.tags_col_label, Unset):
            files.append(("tags_col_label", (None, str(self.tags_col_label).encode(), "text/plain")))

        if not isinstance(self.notes_col_label, Unset):
            files.append(("notes_col_label", (None, str(self.notes_col_label).encode(), "text/plain")))

        if not isinstance(self.account_col_label, Unset):
            files.append(("account_col_label", (None, str(self.account_col_label).encode(), "text/plain")))

        if not isinstance(self.qty_col_label, Unset):
            files.append(("qty_col_label", (None, str(self.qty_col_label).encode(), "text/plain")))

        if not isinstance(self.ticker_col_label, Unset):
            files.append(("ticker_col_label", (None, str(self.ticker_col_label).encode(), "text/plain")))

        if not isinstance(self.price_col_label, Unset):
            files.append(("price_col_label", (None, str(self.price_col_label).encode(), "text/plain")))

        if not isinstance(self.entity_type_col_label, Unset):
            files.append(("entity_type_col_label", (None, str(self.entity_type_col_label).encode(), "text/plain")))

        if not isinstance(self.currency_col_label, Unset):
            files.append(("currency_col_label", (None, str(self.currency_col_label).encode(), "text/plain")))

        if not isinstance(self.exchange_operating_mic_col_label, Unset):
            files.append(
                (
                    "exchange_operating_mic_col_label",
                    (None, str(self.exchange_operating_mic_col_label).encode(), "text/plain"),
                )
            )

        if not isinstance(self.date_format, Unset):
            files.append(("date_format", (None, str(self.date_format).encode(), "text/plain")))

        if not isinstance(self.number_format, Unset):
            files.append(("number_format", (None, str(self.number_format.value).encode(), "text/plain")))

        if not isinstance(self.signage_convention, Unset):
            files.append(("signage_convention", (None, str(self.signage_convention.value).encode(), "text/plain")))

        if not isinstance(self.col_sep, Unset):
            files.append(("col_sep", (None, str(self.col_sep.value).encode(), "text/plain")))

        if not isinstance(self.rows_to_skip, Unset):
            files.append(("rows_to_skip", (None, str(self.rows_to_skip).encode(), "text/plain")))

        if not isinstance(self.amount_type_strategy, Unset):
            files.append(("amount_type_strategy", (None, str(self.amount_type_strategy.value).encode(), "text/plain")))

        if not isinstance(self.amount_type_inflow_value, Unset):
            files.append(
                ("amount_type_inflow_value", (None, str(self.amount_type_inflow_value).encode(), "text/plain"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        raw_file_content = d.pop("raw_file_content", UNSET)

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        _type_ = d.pop("type", UNSET)
        type_: PostApiV1ImportsPreflightFilesBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PostApiV1ImportsPreflightFilesBodyType(_type_)

        _account_id = d.pop("account_id", UNSET)
        account_id: UUID | Unset
        if isinstance(_account_id, Unset):
            account_id = UNSET
        else:
            account_id = UUID(_account_id)

        date_col_label = d.pop("date_col_label", UNSET)

        amount_col_label = d.pop("amount_col_label", UNSET)

        name_col_label = d.pop("name_col_label", UNSET)

        category_col_label = d.pop("category_col_label", UNSET)

        tags_col_label = d.pop("tags_col_label", UNSET)

        notes_col_label = d.pop("notes_col_label", UNSET)

        account_col_label = d.pop("account_col_label", UNSET)

        qty_col_label = d.pop("qty_col_label", UNSET)

        ticker_col_label = d.pop("ticker_col_label", UNSET)

        price_col_label = d.pop("price_col_label", UNSET)

        entity_type_col_label = d.pop("entity_type_col_label", UNSET)

        currency_col_label = d.pop("currency_col_label", UNSET)

        exchange_operating_mic_col_label = d.pop("exchange_operating_mic_col_label", UNSET)

        date_format = d.pop("date_format", UNSET)

        _number_format = d.pop("number_format", UNSET)
        number_format: PostApiV1ImportsPreflightFilesBodyNumberFormat | Unset
        if isinstance(_number_format, Unset):
            number_format = UNSET
        else:
            number_format = PostApiV1ImportsPreflightFilesBodyNumberFormat(_number_format)

        _signage_convention = d.pop("signage_convention", UNSET)
        signage_convention: PostApiV1ImportsPreflightFilesBodySignageConvention | Unset
        if isinstance(_signage_convention, Unset):
            signage_convention = UNSET
        else:
            signage_convention = PostApiV1ImportsPreflightFilesBodySignageConvention(_signage_convention)

        _col_sep = d.pop("col_sep", UNSET)
        col_sep: PostApiV1ImportsPreflightFilesBodyColSep | Unset
        if isinstance(_col_sep, Unset):
            col_sep = UNSET
        else:
            col_sep = PostApiV1ImportsPreflightFilesBodyColSep(_col_sep)

        rows_to_skip = d.pop("rows_to_skip", UNSET)

        _amount_type_strategy = d.pop("amount_type_strategy", UNSET)
        amount_type_strategy: PostApiV1ImportsPreflightFilesBodyAmountTypeStrategy | Unset
        if isinstance(_amount_type_strategy, Unset):
            amount_type_strategy = UNSET
        else:
            amount_type_strategy = PostApiV1ImportsPreflightFilesBodyAmountTypeStrategy(_amount_type_strategy)

        amount_type_inflow_value = d.pop("amount_type_inflow_value", UNSET)

        post_api_v1_imports_preflight_files_body = cls(
            raw_file_content=raw_file_content,
            file=file,
            type_=type_,
            account_id=account_id,
            date_col_label=date_col_label,
            amount_col_label=amount_col_label,
            name_col_label=name_col_label,
            category_col_label=category_col_label,
            tags_col_label=tags_col_label,
            notes_col_label=notes_col_label,
            account_col_label=account_col_label,
            qty_col_label=qty_col_label,
            ticker_col_label=ticker_col_label,
            price_col_label=price_col_label,
            entity_type_col_label=entity_type_col_label,
            currency_col_label=currency_col_label,
            exchange_operating_mic_col_label=exchange_operating_mic_col_label,
            date_format=date_format,
            number_format=number_format,
            signage_convention=signage_convention,
            col_sep=col_sep,
            rows_to_skip=rows_to_skip,
            amount_type_strategy=amount_type_strategy,
            amount_type_inflow_value=amount_type_inflow_value,
        )

        post_api_v1_imports_preflight_files_body.additional_properties = d
        return post_api_v1_imports_preflight_files_body

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
