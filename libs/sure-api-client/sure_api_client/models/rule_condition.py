from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleCondition")


@_attrs_define
class RuleCondition:
    """
    Attributes:
        id (UUID):
        condition_type (str):
        operator (str):
        sub_conditions (list[RuleCondition]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        value (None | str | Unset):
    """

    id: UUID
    condition_type: str
    operator: str
    sub_conditions: list[RuleCondition]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        condition_type = self.condition_type

        operator = self.operator

        sub_conditions = []
        for sub_conditions_item_data in self.sub_conditions:
            sub_conditions_item = sub_conditions_item_data.to_dict()
            sub_conditions.append(sub_conditions_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "condition_type": condition_type,
                "operator": operator,
                "sub_conditions": sub_conditions,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        condition_type = d.pop("condition_type")

        operator = d.pop("operator")

        sub_conditions = []
        _sub_conditions = d.pop("sub_conditions")
        for sub_conditions_item_data in _sub_conditions:
            sub_conditions_item = RuleCondition.from_dict(sub_conditions_item_data)

            sub_conditions.append(sub_conditions_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        rule_condition = cls(
            id=id,
            condition_type=condition_type,
            operator=operator,
            sub_conditions=sub_conditions,
            created_at=created_at,
            updated_at=updated_at,
            value=value,
        )

        rule_condition.additional_properties = d
        return rule_condition

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
