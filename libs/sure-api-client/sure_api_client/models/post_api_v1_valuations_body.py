from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_v1_valuations_body_valuation import PostApiV1ValuationsBodyValuation


T = TypeVar("T", bound="PostApiV1ValuationsBody")


@_attrs_define
class PostApiV1ValuationsBody:
    """
    Attributes:
        valuation (PostApiV1ValuationsBodyValuation):
        upsert (bool | Unset): Response-status signal only. When true and a same-account same-date valuation exists
            before the request, the endpoint returns 200 OK instead of 201 Created. The underlying reconciliation write path
            is unchanged; this flag does not add duplicate-prevention or safe-retry guarantees beyond existing same-date
            reconciliation behavior.
    """

    valuation: PostApiV1ValuationsBodyValuation
    upsert: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valuation = self.valuation.to_dict()

        upsert = self.upsert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valuation": valuation,
            }
        )
        if upsert is not UNSET:
            field_dict["upsert"] = upsert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_v1_valuations_body_valuation import PostApiV1ValuationsBodyValuation

        d = dict(src_dict)
        valuation = PostApiV1ValuationsBodyValuation.from_dict(d.pop("valuation"))

        upsert = d.pop("upsert", UNSET)

        post_api_v1_valuations_body = cls(
            valuation=valuation,
            upsert=upsert,
        )

        post_api_v1_valuations_body.additional_properties = d
        return post_api_v1_valuations_body

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
