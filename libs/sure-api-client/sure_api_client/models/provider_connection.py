from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.provider_connection_accounts import ProviderConnectionAccounts
    from ..models.provider_connection_institution import ProviderConnectionInstitution
    from ..models.provider_connection_sync import ProviderConnectionSync


T = TypeVar("T", bound="ProviderConnection")


@_attrs_define
class ProviderConnection:
    """
    Attributes:
        id (UUID):
        provider (str):
        provider_type (str):
        name (str):
        status (None | str):
        requires_update (bool | None): False when the provider item does not expose this status.
        credentials_configured (bool | None): False when credential readiness is unknown.
        scheduled_for_deletion (bool | None): False when the provider item does not expose this status.
        pending_account_setup (bool | None): False when account setup state is unknown.
        institution (ProviderConnectionInstitution):
        accounts (ProviderConnectionAccounts):
        sync (ProviderConnectionSync):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    provider: str
    provider_type: str
    name: str
    status: None | str
    requires_update: bool | None
    credentials_configured: bool | None
    scheduled_for_deletion: bool | None
    pending_account_setup: bool | None
    institution: ProviderConnectionInstitution
    accounts: ProviderConnectionAccounts
    sync: ProviderConnectionSync
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        provider = self.provider

        provider_type = self.provider_type

        name = self.name

        status: None | str
        status = self.status

        requires_update: bool | None
        requires_update = self.requires_update

        credentials_configured: bool | None
        credentials_configured = self.credentials_configured

        scheduled_for_deletion: bool | None
        scheduled_for_deletion = self.scheduled_for_deletion

        pending_account_setup: bool | None
        pending_account_setup = self.pending_account_setup

        institution = self.institution.to_dict()

        accounts = self.accounts.to_dict()

        sync = self.sync.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "provider": provider,
                "provider_type": provider_type,
                "name": name,
                "status": status,
                "requires_update": requires_update,
                "credentials_configured": credentials_configured,
                "scheduled_for_deletion": scheduled_for_deletion,
                "pending_account_setup": pending_account_setup,
                "institution": institution,
                "accounts": accounts,
                "sync": sync,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_connection_accounts import ProviderConnectionAccounts
        from ..models.provider_connection_institution import ProviderConnectionInstitution
        from ..models.provider_connection_sync import ProviderConnectionSync

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        provider = d.pop("provider")

        provider_type = d.pop("provider_type")

        name = d.pop("name")

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        def _parse_requires_update(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        requires_update = _parse_requires_update(d.pop("requires_update"))

        def _parse_credentials_configured(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        credentials_configured = _parse_credentials_configured(d.pop("credentials_configured"))

        def _parse_scheduled_for_deletion(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        scheduled_for_deletion = _parse_scheduled_for_deletion(d.pop("scheduled_for_deletion"))

        def _parse_pending_account_setup(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        pending_account_setup = _parse_pending_account_setup(d.pop("pending_account_setup"))

        institution = ProviderConnectionInstitution.from_dict(d.pop("institution"))

        accounts = ProviderConnectionAccounts.from_dict(d.pop("accounts"))

        sync = ProviderConnectionSync.from_dict(d.pop("sync"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        provider_connection = cls(
            id=id,
            provider=provider,
            provider_type=provider_type,
            name=name,
            status=status,
            requires_update=requires_update,
            credentials_configured=credentials_configured,
            scheduled_for_deletion=scheduled_for_deletion,
            pending_account_setup=pending_account_setup,
            institution=institution,
            accounts=accounts,
            sync=sync,
            created_at=created_at,
            updated_at=updated_at,
        )

        provider_connection.additional_properties = d
        return provider_connection

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
