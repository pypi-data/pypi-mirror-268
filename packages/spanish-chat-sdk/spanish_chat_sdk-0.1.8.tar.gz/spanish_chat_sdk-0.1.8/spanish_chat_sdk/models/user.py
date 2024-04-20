import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (int):
        creation_date (datetime.datetime):
        username (str):
        first_name (str):
        last_name (str):
        cefr_level (str):
        disabled (bool):
    """

    id: int
    creation_date: datetime.datetime
    username: str
    first_name: str
    last_name: str
    cefr_level: str
    disabled: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        creation_date = self.creation_date.isoformat()

        username = self.username

        first_name = self.first_name

        last_name = self.last_name

        cefr_level = self.cefr_level

        disabled = self.disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "creation_date": creation_date,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "cefr_level": cefr_level,
                "disabled": disabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        creation_date = isoparse(d.pop("creation_date"))

        username = d.pop("username")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        cefr_level = d.pop("cefr_level")

        disabled = d.pop("disabled")

        user = cls(
            id=id,
            creation_date=creation_date,
            username=username,
            first_name=first_name,
            last_name=last_name,
            cefr_level=cefr_level,
            disabled=disabled,
        )

        user.additional_properties = d
        return user

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
