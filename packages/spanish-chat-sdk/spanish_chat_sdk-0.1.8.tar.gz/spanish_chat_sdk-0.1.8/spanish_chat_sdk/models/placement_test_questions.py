from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.placement_test_question import PlacementTestQuestion


T = TypeVar("T", bound="PlacementTestQuestions")


@_attrs_define
class PlacementTestQuestions:
    """
    Attributes:
        questions (List['PlacementTestQuestion']):
    """

    questions: List["PlacementTestQuestion"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        questions = []
        for questions_item_data in self.questions:
            questions_item = questions_item_data.to_dict()
            questions.append(questions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "questions": questions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.placement_test_question import PlacementTestQuestion

        d = src_dict.copy()
        questions = []
        _questions = d.pop("questions")
        for questions_item_data in _questions:
            questions_item = PlacementTestQuestion.from_dict(questions_item_data)

            questions.append(questions_item)

        placement_test_questions = cls(
            questions=questions,
        )

        placement_test_questions.additional_properties = d
        return placement_test_questions

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
