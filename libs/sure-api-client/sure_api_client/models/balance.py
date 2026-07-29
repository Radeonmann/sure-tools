from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.balance_account import BalanceAccount


T = TypeVar("T", bound="Balance")


@_attrs_define
class Balance:
    """
    Attributes:
        id (UUID):
        date (datetime.date):
        currency (str):
        flows_factor (float):
        balance (str):
        balance_cents (int): Balance in currency minor units
        start_balance (str):
        start_balance_cents (int): Starting total balance in currency minor units
        end_balance (str):
        end_balance_cents (int): Ending total balance in currency minor units
        account (BalanceAccount):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        cash_balance (None | str | Unset):
        cash_balance_cents (int | None | Unset): Cash balance in currency minor units
        start_cash_balance (str | Unset):
        start_cash_balance_cents (int | Unset): Starting cash balance in currency minor units
        start_non_cash_balance (str | Unset):
        start_non_cash_balance_cents (int | Unset): Starting non-cash balance in currency minor units
        cash_inflows (str | Unset):
        cash_inflows_cents (int | Unset): Cash inflows in currency minor units
        cash_outflows (str | Unset):
        cash_outflows_cents (int | Unset): Cash outflows in currency minor units
        non_cash_inflows (str | Unset):
        non_cash_inflows_cents (int | Unset): Non-cash inflows in currency minor units
        non_cash_outflows (str | Unset):
        non_cash_outflows_cents (int | Unset): Non-cash outflows in currency minor units
        net_market_flows (str | Unset):
        net_market_flows_cents (int | Unset): Net market flows in currency minor units
        cash_adjustments (str | Unset):
        cash_adjustments_cents (int | Unset): Cash adjustments in currency minor units
        non_cash_adjustments (str | Unset):
        non_cash_adjustments_cents (int | Unset): Non-cash adjustments in currency minor units
        end_cash_balance (str | Unset):
        end_cash_balance_cents (int | Unset): Ending cash balance in currency minor units
        end_non_cash_balance (str | Unset):
        end_non_cash_balance_cents (int | Unset): Ending non-cash balance in currency minor units
    """

    id: UUID
    date: datetime.date
    currency: str
    flows_factor: float
    balance: str
    balance_cents: int
    start_balance: str
    start_balance_cents: int
    end_balance: str
    end_balance_cents: int
    account: BalanceAccount
    created_at: datetime.datetime
    updated_at: datetime.datetime
    cash_balance: None | str | Unset = UNSET
    cash_balance_cents: int | None | Unset = UNSET
    start_cash_balance: str | Unset = UNSET
    start_cash_balance_cents: int | Unset = UNSET
    start_non_cash_balance: str | Unset = UNSET
    start_non_cash_balance_cents: int | Unset = UNSET
    cash_inflows: str | Unset = UNSET
    cash_inflows_cents: int | Unset = UNSET
    cash_outflows: str | Unset = UNSET
    cash_outflows_cents: int | Unset = UNSET
    non_cash_inflows: str | Unset = UNSET
    non_cash_inflows_cents: int | Unset = UNSET
    non_cash_outflows: str | Unset = UNSET
    non_cash_outflows_cents: int | Unset = UNSET
    net_market_flows: str | Unset = UNSET
    net_market_flows_cents: int | Unset = UNSET
    cash_adjustments: str | Unset = UNSET
    cash_adjustments_cents: int | Unset = UNSET
    non_cash_adjustments: str | Unset = UNSET
    non_cash_adjustments_cents: int | Unset = UNSET
    end_cash_balance: str | Unset = UNSET
    end_cash_balance_cents: int | Unset = UNSET
    end_non_cash_balance: str | Unset = UNSET
    end_non_cash_balance_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        date = self.date.isoformat()

        currency = self.currency

        flows_factor = self.flows_factor

        balance = self.balance

        balance_cents = self.balance_cents

        start_balance = self.start_balance

        start_balance_cents = self.start_balance_cents

        end_balance = self.end_balance

        end_balance_cents = self.end_balance_cents

        account = self.account.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        cash_balance: None | str | Unset
        if isinstance(self.cash_balance, Unset):
            cash_balance = UNSET
        else:
            cash_balance = self.cash_balance

        cash_balance_cents: int | None | Unset
        if isinstance(self.cash_balance_cents, Unset):
            cash_balance_cents = UNSET
        else:
            cash_balance_cents = self.cash_balance_cents

        start_cash_balance = self.start_cash_balance

        start_cash_balance_cents = self.start_cash_balance_cents

        start_non_cash_balance = self.start_non_cash_balance

        start_non_cash_balance_cents = self.start_non_cash_balance_cents

        cash_inflows = self.cash_inflows

        cash_inflows_cents = self.cash_inflows_cents

        cash_outflows = self.cash_outflows

        cash_outflows_cents = self.cash_outflows_cents

        non_cash_inflows = self.non_cash_inflows

        non_cash_inflows_cents = self.non_cash_inflows_cents

        non_cash_outflows = self.non_cash_outflows

        non_cash_outflows_cents = self.non_cash_outflows_cents

        net_market_flows = self.net_market_flows

        net_market_flows_cents = self.net_market_flows_cents

        cash_adjustments = self.cash_adjustments

        cash_adjustments_cents = self.cash_adjustments_cents

        non_cash_adjustments = self.non_cash_adjustments

        non_cash_adjustments_cents = self.non_cash_adjustments_cents

        end_cash_balance = self.end_cash_balance

        end_cash_balance_cents = self.end_cash_balance_cents

        end_non_cash_balance = self.end_non_cash_balance

        end_non_cash_balance_cents = self.end_non_cash_balance_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "currency": currency,
                "flows_factor": flows_factor,
                "balance": balance,
                "balance_cents": balance_cents,
                "start_balance": start_balance,
                "start_balance_cents": start_balance_cents,
                "end_balance": end_balance,
                "end_balance_cents": end_balance_cents,
                "account": account,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if cash_balance is not UNSET:
            field_dict["cash_balance"] = cash_balance
        if cash_balance_cents is not UNSET:
            field_dict["cash_balance_cents"] = cash_balance_cents
        if start_cash_balance is not UNSET:
            field_dict["start_cash_balance"] = start_cash_balance
        if start_cash_balance_cents is not UNSET:
            field_dict["start_cash_balance_cents"] = start_cash_balance_cents
        if start_non_cash_balance is not UNSET:
            field_dict["start_non_cash_balance"] = start_non_cash_balance
        if start_non_cash_balance_cents is not UNSET:
            field_dict["start_non_cash_balance_cents"] = start_non_cash_balance_cents
        if cash_inflows is not UNSET:
            field_dict["cash_inflows"] = cash_inflows
        if cash_inflows_cents is not UNSET:
            field_dict["cash_inflows_cents"] = cash_inflows_cents
        if cash_outflows is not UNSET:
            field_dict["cash_outflows"] = cash_outflows
        if cash_outflows_cents is not UNSET:
            field_dict["cash_outflows_cents"] = cash_outflows_cents
        if non_cash_inflows is not UNSET:
            field_dict["non_cash_inflows"] = non_cash_inflows
        if non_cash_inflows_cents is not UNSET:
            field_dict["non_cash_inflows_cents"] = non_cash_inflows_cents
        if non_cash_outflows is not UNSET:
            field_dict["non_cash_outflows"] = non_cash_outflows
        if non_cash_outflows_cents is not UNSET:
            field_dict["non_cash_outflows_cents"] = non_cash_outflows_cents
        if net_market_flows is not UNSET:
            field_dict["net_market_flows"] = net_market_flows
        if net_market_flows_cents is not UNSET:
            field_dict["net_market_flows_cents"] = net_market_flows_cents
        if cash_adjustments is not UNSET:
            field_dict["cash_adjustments"] = cash_adjustments
        if cash_adjustments_cents is not UNSET:
            field_dict["cash_adjustments_cents"] = cash_adjustments_cents
        if non_cash_adjustments is not UNSET:
            field_dict["non_cash_adjustments"] = non_cash_adjustments
        if non_cash_adjustments_cents is not UNSET:
            field_dict["non_cash_adjustments_cents"] = non_cash_adjustments_cents
        if end_cash_balance is not UNSET:
            field_dict["end_cash_balance"] = end_cash_balance
        if end_cash_balance_cents is not UNSET:
            field_dict["end_cash_balance_cents"] = end_cash_balance_cents
        if end_non_cash_balance is not UNSET:
            field_dict["end_non_cash_balance"] = end_non_cash_balance
        if end_non_cash_balance_cents is not UNSET:
            field_dict["end_non_cash_balance_cents"] = end_non_cash_balance_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.balance_account import BalanceAccount

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        currency = d.pop("currency")

        flows_factor = d.pop("flows_factor")

        balance = d.pop("balance")

        balance_cents = d.pop("balance_cents")

        start_balance = d.pop("start_balance")

        start_balance_cents = d.pop("start_balance_cents")

        end_balance = d.pop("end_balance")

        end_balance_cents = d.pop("end_balance_cents")

        account = BalanceAccount.from_dict(d.pop("account"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_cash_balance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cash_balance = _parse_cash_balance(d.pop("cash_balance", UNSET))

        def _parse_cash_balance_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cash_balance_cents = _parse_cash_balance_cents(d.pop("cash_balance_cents", UNSET))

        start_cash_balance = d.pop("start_cash_balance", UNSET)

        start_cash_balance_cents = d.pop("start_cash_balance_cents", UNSET)

        start_non_cash_balance = d.pop("start_non_cash_balance", UNSET)

        start_non_cash_balance_cents = d.pop("start_non_cash_balance_cents", UNSET)

        cash_inflows = d.pop("cash_inflows", UNSET)

        cash_inflows_cents = d.pop("cash_inflows_cents", UNSET)

        cash_outflows = d.pop("cash_outflows", UNSET)

        cash_outflows_cents = d.pop("cash_outflows_cents", UNSET)

        non_cash_inflows = d.pop("non_cash_inflows", UNSET)

        non_cash_inflows_cents = d.pop("non_cash_inflows_cents", UNSET)

        non_cash_outflows = d.pop("non_cash_outflows", UNSET)

        non_cash_outflows_cents = d.pop("non_cash_outflows_cents", UNSET)

        net_market_flows = d.pop("net_market_flows", UNSET)

        net_market_flows_cents = d.pop("net_market_flows_cents", UNSET)

        cash_adjustments = d.pop("cash_adjustments", UNSET)

        cash_adjustments_cents = d.pop("cash_adjustments_cents", UNSET)

        non_cash_adjustments = d.pop("non_cash_adjustments", UNSET)

        non_cash_adjustments_cents = d.pop("non_cash_adjustments_cents", UNSET)

        end_cash_balance = d.pop("end_cash_balance", UNSET)

        end_cash_balance_cents = d.pop("end_cash_balance_cents", UNSET)

        end_non_cash_balance = d.pop("end_non_cash_balance", UNSET)

        end_non_cash_balance_cents = d.pop("end_non_cash_balance_cents", UNSET)

        balance = cls(
            id=id,
            date=date,
            currency=currency,
            flows_factor=flows_factor,
            balance=balance,
            balance_cents=balance_cents,
            start_balance=start_balance,
            start_balance_cents=start_balance_cents,
            end_balance=end_balance,
            end_balance_cents=end_balance_cents,
            account=account,
            created_at=created_at,
            updated_at=updated_at,
            cash_balance=cash_balance,
            cash_balance_cents=cash_balance_cents,
            start_cash_balance=start_cash_balance,
            start_cash_balance_cents=start_cash_balance_cents,
            start_non_cash_balance=start_non_cash_balance,
            start_non_cash_balance_cents=start_non_cash_balance_cents,
            cash_inflows=cash_inflows,
            cash_inflows_cents=cash_inflows_cents,
            cash_outflows=cash_outflows,
            cash_outflows_cents=cash_outflows_cents,
            non_cash_inflows=non_cash_inflows,
            non_cash_inflows_cents=non_cash_inflows_cents,
            non_cash_outflows=non_cash_outflows,
            non_cash_outflows_cents=non_cash_outflows_cents,
            net_market_flows=net_market_flows,
            net_market_flows_cents=net_market_flows_cents,
            cash_adjustments=cash_adjustments,
            cash_adjustments_cents=cash_adjustments_cents,
            non_cash_adjustments=non_cash_adjustments,
            non_cash_adjustments_cents=non_cash_adjustments_cents,
            end_cash_balance=end_cash_balance,
            end_cash_balance_cents=end_cash_balance_cents,
            end_non_cash_balance=end_non_cash_balance,
            end_non_cash_balance_cents=end_non_cash_balance_cents,
        )

        balance.additional_properties = d
        return balance

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
