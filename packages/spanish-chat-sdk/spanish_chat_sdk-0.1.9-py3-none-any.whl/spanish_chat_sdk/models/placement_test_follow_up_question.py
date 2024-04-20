from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.placement_test_answer import PlacementTestAnswer


T = TypeVar("T", bound="PlacementTestFollowUpQuestion")


@_attrs_define
class PlacementTestFollowUpQuestion:
    """
    Attributes:
        question (str):
        answers (List['PlacementTestAnswer']):
    """

    question: str
    answers: List["PlacementTestAnswer"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        question = self.question

        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "question": question,
                "answers": answers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.placement_test_answer import PlacementTestAnswer

        d = src_dict.copy()
        question = d.pop("question")

        answers = []
        _answers = d.pop("answers")
        for answers_item_data in _answers:
            answers_item = PlacementTestAnswer.from_dict(answers_item_data)

            answers.append(answers_item)

        placement_test_follow_up_question = cls(
            question=question,
            answers=answers,
        )

        placement_test_follow_up_question.additional_properties = d
        return placement_test_follow_up_question

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
