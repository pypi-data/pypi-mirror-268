from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.translation_usage_example import TranslationUsageExample


T = TypeVar("T", bound="WordTranslation")


@_attrs_define
class WordTranslation:
    """
    Attributes:
        translation (str):
        usage_examples (List['TranslationUsageExample']):
    """

    translation: str
    usage_examples: List["TranslationUsageExample"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        translation = self.translation

        usage_examples = []
        for usage_examples_item_data in self.usage_examples:
            usage_examples_item = usage_examples_item_data.to_dict()
            usage_examples.append(usage_examples_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "translation": translation,
                "usage_examples": usage_examples,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.translation_usage_example import TranslationUsageExample

        d = src_dict.copy()
        translation = d.pop("translation")

        usage_examples = []
        _usage_examples = d.pop("usage_examples")
        for usage_examples_item_data in _usage_examples:
            usage_examples_item = TranslationUsageExample.from_dict(usage_examples_item_data)

            usage_examples.append(usage_examples_item)

        word_translation = cls(
            translation=translation,
            usage_examples=usage_examples,
        )

        word_translation.additional_properties = d
        return word_translation

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
