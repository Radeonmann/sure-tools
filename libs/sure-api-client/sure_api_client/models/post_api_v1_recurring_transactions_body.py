from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiV1RecurringTransactionsBody")


@_attrs_define
class PostApiV1RecurringTransactionsBody:
    """
    Attributes:
        recurring_transaction (Any):
    """

    recurring_transaction: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recurring_transaction: Any
        recurring_transaction = self.recurring_transaction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recurring_transaction": recurring_transaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_recurring_transaction(data: object) -> Any:
            return cast(Any, data)

        recurring_transaction = _parse_recurring_transaction(d.pop("recurring_transaction"))

        post_api_v1_recurring_transactions_body = cls(
            recurring_transaction=recurring_transaction,
        )

        post_api_v1_recurring_transactions_body.additional_properties = d
        return post_api_v1_recurring_transactions_body

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
