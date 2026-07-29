from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_v1_trades_body_trade_type import PostApiV1TradesBodyTradeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiV1TradesBodyTrade")


@_attrs_define
class PostApiV1TradesBodyTrade:
    """
    Attributes:
        account_id (UUID): Account ID (required)
        date (datetime.date): Trade date (required)
        type_ (PostApiV1TradesBodyTradeType): Trade type (required)
        qty (float | Unset): Quantity (required for buy/sell)
        price (float | Unset): Price (required for buy/sell)
        amount (float | Unset): Amount (required for dividend, deposit, withdrawal, interest)
        security_id (UUID | Unset): Security ID (one of security_id, ticker, manual_ticker required)
        ticker (str | Unset): Ticker symbol
        manual_ticker (str | Unset): Manual ticker for offline securities
        currency (str | Unset): Currency (defaults to account currency)
        investment_activity_label (str | Unset): Activity label (e.g. Buy, Sell)
        category_id (UUID | Unset): Category ID
        transfer_account_id (UUID | Unset): Destination/source account ID for linked transfers
    """

    account_id: UUID
    date: datetime.date
    type_: PostApiV1TradesBodyTradeType
    qty: float | Unset = UNSET
    price: float | Unset = UNSET
    amount: float | Unset = UNSET
    security_id: UUID | Unset = UNSET
    ticker: str | Unset = UNSET
    manual_ticker: str | Unset = UNSET
    currency: str | Unset = UNSET
    investment_activity_label: str | Unset = UNSET
    category_id: UUID | Unset = UNSET
    transfer_account_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = str(self.account_id)

        date = self.date.isoformat()

        type_ = self.type_.value

        qty = self.qty

        price = self.price

        amount = self.amount

        security_id: str | Unset = UNSET
        if not isinstance(self.security_id, Unset):
            security_id = str(self.security_id)

        ticker = self.ticker

        manual_ticker = self.manual_ticker

        currency = self.currency

        investment_activity_label = self.investment_activity_label

        category_id: str | Unset = UNSET
        if not isinstance(self.category_id, Unset):
            category_id = str(self.category_id)

        transfer_account_id: str | Unset = UNSET
        if not isinstance(self.transfer_account_id, Unset):
            transfer_account_id = str(self.transfer_account_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "date": date,
                "type": type_,
            }
        )
        if qty is not UNSET:
            field_dict["qty"] = qty
        if price is not UNSET:
            field_dict["price"] = price
        if amount is not UNSET:
            field_dict["amount"] = amount
        if security_id is not UNSET:
            field_dict["security_id"] = security_id
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if manual_ticker is not UNSET:
            field_dict["manual_ticker"] = manual_ticker
        if currency is not UNSET:
            field_dict["currency"] = currency
        if investment_activity_label is not UNSET:
            field_dict["investment_activity_label"] = investment_activity_label
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if transfer_account_id is not UNSET:
            field_dict["transfer_account_id"] = transfer_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = UUID(d.pop("account_id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        type_ = PostApiV1TradesBodyTradeType(d.pop("type"))

        qty = d.pop("qty", UNSET)

        price = d.pop("price", UNSET)

        amount = d.pop("amount", UNSET)

        _security_id = d.pop("security_id", UNSET)
        security_id: UUID | Unset
        if isinstance(_security_id, Unset):
            security_id = UNSET
        else:
            security_id = UUID(_security_id)

        ticker = d.pop("ticker", UNSET)

        manual_ticker = d.pop("manual_ticker", UNSET)

        currency = d.pop("currency", UNSET)

        investment_activity_label = d.pop("investment_activity_label", UNSET)

        _category_id = d.pop("category_id", UNSET)
        category_id: UUID | Unset
        if isinstance(_category_id, Unset):
            category_id = UNSET
        else:
            category_id = UUID(_category_id)

        _transfer_account_id = d.pop("transfer_account_id", UNSET)
        transfer_account_id: UUID | Unset
        if isinstance(_transfer_account_id, Unset):
            transfer_account_id = UNSET
        else:
            transfer_account_id = UUID(_transfer_account_id)

        post_api_v1_trades_body_trade = cls(
            account_id=account_id,
            date=date,
            type_=type_,
            qty=qty,
            price=price,
            amount=amount,
            security_id=security_id,
            ticker=ticker,
            manual_ticker=manual_ticker,
            currency=currency,
            investment_activity_label=investment_activity_label,
            category_id=category_id,
            transfer_account_id=transfer_account_id,
        )

        post_api_v1_trades_body_trade.additional_properties = d
        return post_api_v1_trades_body_trade

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
