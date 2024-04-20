from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.grammar_error import GrammarError


T = TypeVar("T", bound="GrammarErrors")


@_attrs_define
class GrammarErrors:
    """
    Attributes:
        edits (List['GrammarError']):
    """

    edits: List["GrammarError"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edits = []
        for edits_item_data in self.edits:
            edits_item = edits_item_data.to_dict()
            edits.append(edits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edits": edits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.grammar_error import GrammarError

        d = src_dict.copy()
        edits = []
        _edits = d.pop("edits")
        for edits_item_data in _edits:
            edits_item = GrammarError.from_dict(edits_item_data)

            edits.append(edits_item)

        grammar_errors = cls(
            edits=edits,
        )

        grammar_errors.additional_properties = d
        return grammar_errors

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
