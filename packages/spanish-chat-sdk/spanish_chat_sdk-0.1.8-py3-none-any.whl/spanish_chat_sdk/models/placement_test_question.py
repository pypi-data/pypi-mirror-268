from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.placement_test_question_type import PlacementTestQuestionType

if TYPE_CHECKING:
    from ..models.placement_test_answer import PlacementTestAnswer
    from ..models.placement_test_follow_up_question import PlacementTestFollowUpQuestion


T = TypeVar("T", bound="PlacementTestQuestion")


@_attrs_define
class PlacementTestQuestion:
    """
    Attributes:
        cefr_level (str):
        question_type (PlacementTestQuestionType):
        question (str):
        answers (List['PlacementTestAnswer']):
        follow_up_questions (Union[List['PlacementTestFollowUpQuestion'], None]):
    """

    cefr_level: str
    question_type: PlacementTestQuestionType
    question: str
    answers: List["PlacementTestAnswer"]
    follow_up_questions: Union[List["PlacementTestFollowUpQuestion"], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cefr_level = self.cefr_level

        question_type = self.question_type.value

        question = self.question

        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)

        follow_up_questions: Union[List[Dict[str, Any]], None]
        if isinstance(self.follow_up_questions, list):
            follow_up_questions = []
            for follow_up_questions_type_0_item_data in self.follow_up_questions:
                follow_up_questions_type_0_item = follow_up_questions_type_0_item_data.to_dict()
                follow_up_questions.append(follow_up_questions_type_0_item)

        else:
            follow_up_questions = self.follow_up_questions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cefr_level": cefr_level,
                "question_type": question_type,
                "question": question,
                "answers": answers,
                "follow_up_questions": follow_up_questions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.placement_test_answer import PlacementTestAnswer
        from ..models.placement_test_follow_up_question import PlacementTestFollowUpQuestion

        d = src_dict.copy()
        cefr_level = d.pop("cefr_level")

        question_type = PlacementTestQuestionType(d.pop("question_type"))

        question = d.pop("question")

        answers = []
        _answers = d.pop("answers")
        for answers_item_data in _answers:
            answers_item = PlacementTestAnswer.from_dict(answers_item_data)

            answers.append(answers_item)

        def _parse_follow_up_questions(data: object) -> Union[List["PlacementTestFollowUpQuestion"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                follow_up_questions_type_0 = []
                _follow_up_questions_type_0 = data
                for follow_up_questions_type_0_item_data in _follow_up_questions_type_0:
                    follow_up_questions_type_0_item = PlacementTestFollowUpQuestion.from_dict(
                        follow_up_questions_type_0_item_data
                    )

                    follow_up_questions_type_0.append(follow_up_questions_type_0_item)

                return follow_up_questions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PlacementTestFollowUpQuestion"], None], data)

        follow_up_questions = _parse_follow_up_questions(d.pop("follow_up_questions"))

        placement_test_question = cls(
            cefr_level=cefr_level,
            question_type=question_type,
            question=question,
            answers=answers,
            follow_up_questions=follow_up_questions,
        )

        placement_test_question.additional_properties = d
        return placement_test_question

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
