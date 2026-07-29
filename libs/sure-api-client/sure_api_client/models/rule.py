from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rule_resource_type import RuleResourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_action import RuleAction
    from ..models.rule_condition import RuleCondition


T = TypeVar("T", bound="Rule")


@_attrs_define
class Rule:
    """
    Attributes:
        id (UUID):
        resource_type (RuleResourceType):
        active (bool):
        conditions (list[RuleCondition]):
        actions (list[RuleAction]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (None | str | Unset):
        effective_date (datetime.date | None | Unset):
    """

    id: UUID
    resource_type: RuleResourceType
    active: bool
    conditions: list[RuleCondition]
    actions: list[RuleAction]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: None | str | Unset = UNSET
    effective_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        resource_type = self.resource_type.value

        active = self.active

        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item = conditions_item_data.to_dict()
            conditions.append(conditions_item)

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        effective_date: None | str | Unset
        if isinstance(self.effective_date, Unset):
            effective_date = UNSET
        elif isinstance(self.effective_date, datetime.date):
            effective_date = self.effective_date.isoformat()
        else:
            effective_date = self.effective_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "resource_type": resource_type,
                "active": active,
                "conditions": conditions,
                "actions": actions,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_action import RuleAction
        from ..models.rule_condition import RuleCondition

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        resource_type = RuleResourceType(d.pop("resource_type"))

        active = d.pop("active")

        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:
            conditions_item = RuleCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = RuleAction.from_dict(actions_item_data)

            actions.append(actions_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_effective_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_date_type_0 = datetime.date.fromisoformat(data)

                return effective_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        effective_date = _parse_effective_date(d.pop("effective_date", UNSET))

        rule = cls(
            id=id,
            resource_type=resource_type,
            active=active,
            conditions=conditions,
            actions=actions,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            effective_date=effective_date,
        )

        rule.additional_properties = d
        return rule

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
