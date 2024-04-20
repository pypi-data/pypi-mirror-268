import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """
    Attributes:
        id (int):
        creation_date (datetime.datetime):
        topic (Union[None, str]):
        active (Union[None, bool]):
        user_id (int):
        user (User):
    """

    id: int
    creation_date: datetime.datetime
    topic: Union[None, str]
    active: Union[None, bool]
    user_id: int
    user: "User"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        creation_date = self.creation_date.isoformat()

        topic: Union[None, str]
        topic = self.topic

        active: Union[None, bool]
        active = self.active

        user_id = self.user_id

        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "creation_date": creation_date,
                "topic": topic,
                "active": active,
                "user_id": user_id,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user import User

        d = src_dict.copy()
        id = d.pop("id")

        creation_date = isoparse(d.pop("creation_date"))

        def _parse_topic(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        topic = _parse_topic(d.pop("topic"))

        def _parse_active(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        active = _parse_active(d.pop("active"))

        user_id = d.pop("user_id")

        user = User.from_dict(d.pop("user"))

        conversation = cls(
            id=id,
            creation_date=creation_date,
            topic=topic,
            active=active,
            user_id=user_id,
            user=user,
        )

        conversation.additional_properties = d
        return conversation

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
