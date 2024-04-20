from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GrammarError")


@_attrs_define
class GrammarError:
    """
    Attributes:
        end (int):
        error_type (str):
        general_error_type (str):
        id (str):
        replacement (str):
        sentence (str):
        sentence_start (int):
        start (int):
        formatted_error_type (Union[None, Unset, str]):
    """

    end: int
    error_type: str
    general_error_type: str
    id: str
    replacement: str
    sentence: str
    sentence_start: int
    start: int
    formatted_error_type: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end = self.end

        error_type = self.error_type

        general_error_type = self.general_error_type

        id = self.id

        replacement = self.replacement

        sentence = self.sentence

        sentence_start = self.sentence_start

        start = self.start

        formatted_error_type: Union[None, Unset, str]
        if isinstance(self.formatted_error_type, Unset):
            formatted_error_type = UNSET
        else:
            formatted_error_type = self.formatted_error_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "error_type": error_type,
                "general_error_type": general_error_type,
                "id": id,
                "replacement": replacement,
                "sentence": sentence,
                "sentence_start": sentence_start,
                "start": start,
            }
        )
        if formatted_error_type is not UNSET:
            field_dict["formatted_error_type"] = formatted_error_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end = d.pop("end")

        error_type = d.pop("error_type")

        general_error_type = d.pop("general_error_type")

        id = d.pop("id")

        replacement = d.pop("replacement")

        sentence = d.pop("sentence")

        sentence_start = d.pop("sentence_start")

        start = d.pop("start")

        def _parse_formatted_error_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        formatted_error_type = _parse_formatted_error_type(d.pop("formatted_error_type", UNSET))

        grammar_error = cls(
            end=end,
            error_type=error_type,
            general_error_type=general_error_type,
            id=id,
            replacement=replacement,
            sentence=sentence,
            sentence_start=sentence_start,
            start=start,
            formatted_error_type=formatted_error_type,
        )

        grammar_error.additional_properties = d
        return grammar_error

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
