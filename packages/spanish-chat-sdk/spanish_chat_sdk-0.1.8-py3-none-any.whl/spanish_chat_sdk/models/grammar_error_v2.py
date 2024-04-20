from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GrammarErrorV2")


@_attrs_define
class GrammarErrorV2:
    """
    Attributes:
        type (str):
        start_position (int):
        end_position (int):
        replacement (str):
        explanation (str):
        sentence (str):
    """

    type: str
    start_position: int
    end_position: int
    replacement: str
    explanation: str
    sentence: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        start_position = self.start_position

        end_position = self.end_position

        replacement = self.replacement

        explanation = self.explanation

        sentence = self.sentence

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "start_position": start_position,
                "end_position": end_position,
                "replacement": replacement,
                "explanation": explanation,
                "sentence": sentence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        start_position = d.pop("start_position")

        end_position = d.pop("end_position")

        replacement = d.pop("replacement")

        explanation = d.pop("explanation")

        sentence = d.pop("sentence")

        grammar_error_v2 = cls(
            type=type,
            start_position=start_position,
            end_position=end_position,
            replacement=replacement,
            explanation=explanation,
            sentence=sentence,
        )

        grammar_error_v2.additional_properties = d
        return grammar_error_v2

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
