import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.conversation import Conversation


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        id (int):
        timestamp (datetime.datetime):
        message (str):
        is_system (bool):
        conversation_id (int):
        conversation (Conversation):
    """

    id: int
    timestamp: datetime.datetime
    message: str
    is_system: bool
    conversation_id: int
    conversation: "Conversation"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        timestamp = self.timestamp.isoformat()

        message = self.message

        is_system = self.is_system

        conversation_id = self.conversation_id

        conversation = self.conversation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "timestamp": timestamp,
                "message": message,
                "is_system": is_system,
                "conversation_id": conversation_id,
                "conversation": conversation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.conversation import Conversation

        d = src_dict.copy()
        id = d.pop("id")

        timestamp = isoparse(d.pop("timestamp"))

        message = d.pop("message")

        is_system = d.pop("is_system")

        conversation_id = d.pop("conversation_id")

        conversation = Conversation.from_dict(d.pop("conversation"))

        message = cls(
            id=id,
            timestamp=timestamp,
            message=message,
            is_system=is_system,
            conversation_id=conversation_id,
            conversation=conversation,
        )

        message.additional_properties = d
        return message

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
