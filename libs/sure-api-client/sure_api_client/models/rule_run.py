from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rule_run_execution_type import RuleRunExecutionType
from ..models.rule_run_status import RuleRunStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_run_rule_type_0 import RuleRunRuleType0


T = TypeVar("T", bound="RuleRun")


@_attrs_define
class RuleRun:
    """
    Attributes:
        id (UUID):
        rule_id (UUID):
        rule_name (None | str):
        execution_type (RuleRunExecutionType):
        status (RuleRunStatus):
        transactions_queued (int):
        transactions_processed (int):
        transactions_modified (int):
        pending_jobs_count (int):
        executed_at (datetime.datetime):
        rule (None | RuleRunRuleType0):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        error_message (None | str | Unset):
    """

    id: UUID
    rule_id: UUID
    rule_name: None | str
    execution_type: RuleRunExecutionType
    status: RuleRunStatus
    transactions_queued: int
    transactions_processed: int
    transactions_modified: int
    pending_jobs_count: int
    executed_at: datetime.datetime
    rule: None | RuleRunRuleType0
    created_at: datetime.datetime
    updated_at: datetime.datetime
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rule_run_rule_type_0 import RuleRunRuleType0

        id = str(self.id)

        rule_id = str(self.rule_id)

        rule_name: None | str
        rule_name = self.rule_name

        execution_type = self.execution_type.value

        status = self.status.value

        transactions_queued = self.transactions_queued

        transactions_processed = self.transactions_processed

        transactions_modified = self.transactions_modified

        pending_jobs_count = self.pending_jobs_count

        executed_at = self.executed_at.isoformat()

        rule: dict[str, Any] | None
        if isinstance(self.rule, RuleRunRuleType0):
            rule = self.rule.to_dict()
        else:
            rule = self.rule

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rule_id": rule_id,
                "rule_name": rule_name,
                "execution_type": execution_type,
                "status": status,
                "transactions_queued": transactions_queued,
                "transactions_processed": transactions_processed,
                "transactions_modified": transactions_modified,
                "pending_jobs_count": pending_jobs_count,
                "executed_at": executed_at,
                "rule": rule,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_run_rule_type_0 import RuleRunRuleType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        rule_id = UUID(d.pop("rule_id"))

        def _parse_rule_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rule_name = _parse_rule_name(d.pop("rule_name"))

        execution_type = RuleRunExecutionType(d.pop("execution_type"))

        status = RuleRunStatus(d.pop("status"))

        transactions_queued = d.pop("transactions_queued")

        transactions_processed = d.pop("transactions_processed")

        transactions_modified = d.pop("transactions_modified")

        pending_jobs_count = d.pop("pending_jobs_count")

        executed_at = datetime.datetime.fromisoformat(d.pop("executed_at"))

        def _parse_rule(data: object) -> None | RuleRunRuleType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rule_type_0 = RuleRunRuleType0.from_dict(data)

                return rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RuleRunRuleType0, data)

        rule = _parse_rule(d.pop("rule"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        rule_run = cls(
            id=id,
            rule_id=rule_id,
            rule_name=rule_name,
            execution_type=execution_type,
            status=status,
            transactions_queued=transactions_queued,
            transactions_processed=transactions_processed,
            transactions_modified=transactions_modified,
            pending_jobs_count=pending_jobs_count,
            executed_at=executed_at,
            rule=rule,
            created_at=created_at,
            updated_at=updated_at,
            error_message=error_message,
        )

        rule_run.additional_properties = d
        return rule_run

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
