from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportRowDiagnosticFields")


@_attrs_define
class ImportRowDiagnosticFields:
    """
    Attributes:
        account (None | str | Unset):
        date (None | str | Unset):
        qty (None | str | Unset):
        ticker (None | str | Unset):
        exchange_operating_mic (None | str | Unset):
        price (None | str | Unset):
        amount (None | str | Unset):
        currency (None | str | Unset):
        name (None | str | Unset):
        category (None | str | Unset):
        tags (None | str | Unset):
        entity_type (None | str | Unset):
        notes (None | str | Unset):
        active (bool | None | Unset):
        effective_date (None | str | Unset):
        conditions (None | str | Unset):
        actions (None | str | Unset):
    """

    account: None | str | Unset = UNSET
    date: None | str | Unset = UNSET
    qty: None | str | Unset = UNSET
    ticker: None | str | Unset = UNSET
    exchange_operating_mic: None | str | Unset = UNSET
    price: None | str | Unset = UNSET
    amount: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    tags: None | str | Unset = UNSET
    entity_type: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    active: bool | None | Unset = UNSET
    effective_date: None | str | Unset = UNSET
    conditions: None | str | Unset = UNSET
    actions: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account: None | str | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        else:
            account = self.account

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        qty: None | str | Unset
        if isinstance(self.qty, Unset):
            qty = UNSET
        else:
            qty = self.qty

        ticker: None | str | Unset
        if isinstance(self.ticker, Unset):
            ticker = UNSET
        else:
            ticker = self.ticker

        exchange_operating_mic: None | str | Unset
        if isinstance(self.exchange_operating_mic, Unset):
            exchange_operating_mic = UNSET
        else:
            exchange_operating_mic = self.exchange_operating_mic

        price: None | str | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        tags: None | str | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        else:
            tags = self.tags

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        effective_date: None | str | Unset
        if isinstance(self.effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = self.effective_date

        conditions: None | str | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        else:
            conditions = self.conditions

        actions: None | str | Unset
        if isinstance(self.actions, Unset):
            actions = UNSET
        else:
            actions = self.actions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if date is not UNSET:
            field_dict["date"] = date
        if qty is not UNSET:
            field_dict["qty"] = qty
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if exchange_operating_mic is not UNSET:
            field_dict["exchange_operating_mic"] = exchange_operating_mic
        if price is not UNSET:
            field_dict["price"] = price
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if tags is not UNSET:
            field_dict["tags"] = tags
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if notes is not UNSET:
            field_dict["notes"] = notes
        if active is not UNSET:
            field_dict["active"] = active
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_account(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account = _parse_account(d.pop("account", UNSET))

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_qty(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qty = _parse_qty(d.pop("qty", UNSET))

        def _parse_ticker(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ticker = _parse_ticker(d.pop("ticker", UNSET))

        def _parse_exchange_operating_mic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_operating_mic = _parse_exchange_operating_mic(d.pop("exchange_operating_mic", UNSET))

        def _parse_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_tags(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entity_type", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_effective_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effective_date = _parse_effective_date(d.pop("effective_date", UNSET))

        def _parse_conditions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))

        def _parse_actions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actions = _parse_actions(d.pop("actions", UNSET))

        import_row_diagnostic_fields = cls(
            account=account,
            date=date,
            qty=qty,
            ticker=ticker,
            exchange_operating_mic=exchange_operating_mic,
            price=price,
            amount=amount,
            currency=currency,
            name=name,
            category=category,
            tags=tags,
            entity_type=entity_type,
            notes=notes,
            active=active,
            effective_date=effective_date,
            conditions=conditions,
            actions=actions,
        )

        import_row_diagnostic_fields.additional_properties = d
        return import_row_diagnostic_fields

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
