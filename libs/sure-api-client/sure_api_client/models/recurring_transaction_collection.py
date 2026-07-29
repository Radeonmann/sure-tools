from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.recurring_transaction import RecurringTransaction


T = TypeVar("T", bound="RecurringTransactionCollection")


@_attrs_define
class RecurringTransactionCollection:
    """
    Attributes:
        recurring_transactions (list[RecurringTransaction]):
        pagination (Pagination):
    """

    recurring_transactions: list[RecurringTransaction]
    pagination: Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recurring_transactions = []
        for recurring_transactions_item_data in self.recurring_transactions:
            recurring_transactions_item = recurring_transactions_item_data.to_dict()
            recurring_transactions.append(recurring_transactions_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recurring_transactions": recurring_transactions,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.recurring_transaction import RecurringTransaction

        d = dict(src_dict)
        recurring_transactions = []
        _recurring_transactions = d.pop("recurring_transactions")
        for recurring_transactions_item_data in _recurring_transactions:
            recurring_transactions_item = RecurringTransaction.from_dict(recurring_transactions_item_data)

            recurring_transactions.append(recurring_transactions_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        recurring_transaction_collection = cls(
            recurring_transactions=recurring_transactions,
            pagination=pagination,
        )

        recurring_transaction_collection.additional_properties = d
        return recurring_transaction_collection

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
