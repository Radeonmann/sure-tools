from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResetStatusResponseCounts")


@_attrs_define
class ResetStatusResponseCounts:
    """
    Attributes:
        account_statements (int):
        family_exports (int):
        imports (int):
        import_sessions (int):
        import_source_mappings (int):
        import_rows (int):
        import_mappings (int):
        accounts (int):
        account_shares (int):
        account_providers (int):
        entries (int):
        transactions (int):
        transfers (int):
        rejected_transfers (int):
        valuations (int):
        trades (int):
        holdings (int):
        balances (int):
        recurring_transactions (int):
        rules (int):
        rule_actions (int):
        rule_conditions (int):
        rule_runs (int):
        budgets (int):
        budget_categories (int):
        categories (int):
        tags (int):
        taggings (int):
        merchants (int):
        family_merchant_associations (int):
        provider_items (int):
        active_storage_attachments (int):
        plaid_items (int):
    """

    account_statements: int
    family_exports: int
    imports: int
    import_sessions: int
    import_source_mappings: int
    import_rows: int
    import_mappings: int
    accounts: int
    account_shares: int
    account_providers: int
    entries: int
    transactions: int
    transfers: int
    rejected_transfers: int
    valuations: int
    trades: int
    holdings: int
    balances: int
    recurring_transactions: int
    rules: int
    rule_actions: int
    rule_conditions: int
    rule_runs: int
    budgets: int
    budget_categories: int
    categories: int
    tags: int
    taggings: int
    merchants: int
    family_merchant_associations: int
    provider_items: int
    active_storage_attachments: int
    plaid_items: int
    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_statements = self.account_statements

        family_exports = self.family_exports

        imports = self.imports

        import_sessions = self.import_sessions

        import_source_mappings = self.import_source_mappings

        import_rows = self.import_rows

        import_mappings = self.import_mappings

        accounts = self.accounts

        account_shares = self.account_shares

        account_providers = self.account_providers

        entries = self.entries

        transactions = self.transactions

        transfers = self.transfers

        rejected_transfers = self.rejected_transfers

        valuations = self.valuations

        trades = self.trades

        holdings = self.holdings

        balances = self.balances

        recurring_transactions = self.recurring_transactions

        rules = self.rules

        rule_actions = self.rule_actions

        rule_conditions = self.rule_conditions

        rule_runs = self.rule_runs

        budgets = self.budgets

        budget_categories = self.budget_categories

        categories = self.categories

        tags = self.tags

        taggings = self.taggings

        merchants = self.merchants

        family_merchant_associations = self.family_merchant_associations

        provider_items = self.provider_items

        active_storage_attachments = self.active_storage_attachments

        plaid_items = self.plaid_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_statements": account_statements,
                "family_exports": family_exports,
                "imports": imports,
                "import_sessions": import_sessions,
                "import_source_mappings": import_source_mappings,
                "import_rows": import_rows,
                "import_mappings": import_mappings,
                "accounts": accounts,
                "account_shares": account_shares,
                "account_providers": account_providers,
                "entries": entries,
                "transactions": transactions,
                "transfers": transfers,
                "rejected_transfers": rejected_transfers,
                "valuations": valuations,
                "trades": trades,
                "holdings": holdings,
                "balances": balances,
                "recurring_transactions": recurring_transactions,
                "rules": rules,
                "rule_actions": rule_actions,
                "rule_conditions": rule_conditions,
                "rule_runs": rule_runs,
                "budgets": budgets,
                "budget_categories": budget_categories,
                "categories": categories,
                "tags": tags,
                "taggings": taggings,
                "merchants": merchants,
                "family_merchant_associations": family_merchant_associations,
                "provider_items": provider_items,
                "active_storage_attachments": active_storage_attachments,
                "plaid_items": plaid_items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_statements = d.pop("account_statements")

        family_exports = d.pop("family_exports")

        imports = d.pop("imports")

        import_sessions = d.pop("import_sessions")

        import_source_mappings = d.pop("import_source_mappings")

        import_rows = d.pop("import_rows")

        import_mappings = d.pop("import_mappings")

        accounts = d.pop("accounts")

        account_shares = d.pop("account_shares")

        account_providers = d.pop("account_providers")

        entries = d.pop("entries")

        transactions = d.pop("transactions")

        transfers = d.pop("transfers")

        rejected_transfers = d.pop("rejected_transfers")

        valuations = d.pop("valuations")

        trades = d.pop("trades")

        holdings = d.pop("holdings")

        balances = d.pop("balances")

        recurring_transactions = d.pop("recurring_transactions")

        rules = d.pop("rules")

        rule_actions = d.pop("rule_actions")

        rule_conditions = d.pop("rule_conditions")

        rule_runs = d.pop("rule_runs")

        budgets = d.pop("budgets")

        budget_categories = d.pop("budget_categories")

        categories = d.pop("categories")

        tags = d.pop("tags")

        taggings = d.pop("taggings")

        merchants = d.pop("merchants")

        family_merchant_associations = d.pop("family_merchant_associations")

        provider_items = d.pop("provider_items")

        active_storage_attachments = d.pop("active_storage_attachments")

        plaid_items = d.pop("plaid_items")

        reset_status_response_counts = cls(
            account_statements=account_statements,
            family_exports=family_exports,
            imports=imports,
            import_sessions=import_sessions,
            import_source_mappings=import_source_mappings,
            import_rows=import_rows,
            import_mappings=import_mappings,
            accounts=accounts,
            account_shares=account_shares,
            account_providers=account_providers,
            entries=entries,
            transactions=transactions,
            transfers=transfers,
            rejected_transfers=rejected_transfers,
            valuations=valuations,
            trades=trades,
            holdings=holdings,
            balances=balances,
            recurring_transactions=recurring_transactions,
            rules=rules,
            rule_actions=rule_actions,
            rule_conditions=rule_conditions,
            rule_runs=rule_runs,
            budgets=budgets,
            budget_categories=budget_categories,
            categories=categories,
            tags=tags,
            taggings=taggings,
            merchants=merchants,
            family_merchant_associations=family_merchant_associations,
            provider_items=provider_items,
            active_storage_attachments=active_storage_attachments,
            plaid_items=plaid_items,
        )

        reset_status_response_counts.additional_properties = d
        return reset_status_response_counts

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
