import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


T = TypeVar("T", bound="GroupSchema")


@_attrs_define
class GroupSchema:
    """Which Group fields to include in response bodies

    Attributes:
        id (str): ID of the group
        is_delete_protected (bool): This must be set false before the group can be deleted
        is_active (bool): If false, all group operations are disabled
        created_date (datetime.datetime): Date and time the group was created
        last_updated_by (str): ID of the account that last updated the group
        tags (List[str]): List of tags on this group
        name (str): Name of the group
        num_history (int): Number of history entries to keep on rolling list attributes
        role_delete_protection_on_by_default (bool): If true, new roles attached to this group will have delete
            protection enabled if not specified at creation
        project_id (Union[Unset, str]): ID of the project this group belongs to, if any
        last_updated_date (Union[Unset, datetime.datetime]): Date and time the group was last updated
        created_by (Union[Unset, str]): ID of the account that created the group
    """

    id: str
    is_delete_protected: bool
    is_active: bool
    created_date: datetime.datetime
    last_updated_by: str
    tags: List[str]
    name: str
    num_history: int
    role_delete_protection_on_by_default: bool
    project_id: Union[Unset, str] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        is_delete_protected = self.is_delete_protected

        is_active = self.is_active

        created_date = self.created_date.isoformat()

        last_updated_by = self.last_updated_by

        tags = self.tags

        name = self.name

        num_history = self.num_history

        role_delete_protection_on_by_default = self.role_delete_protection_on_by_default

        project_id = self.project_id

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        created_by = self.created_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "is_delete_protected": is_delete_protected,
                "is_active": is_active,
                "created_date": created_date,
                "last_updated_by": last_updated_by,
                "tags": tags,
                "name": name,
                "num_history": num_history,
                "role_delete_protection_on_by_default": role_delete_protection_on_by_default,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        is_delete_protected = d.pop("is_delete_protected")

        is_active = d.pop("is_active")

        created_date = isoparse(d.pop("created_date"))

        last_updated_by = d.pop("last_updated_by")

        tags = cast(List[str], d.pop("tags"))

        name = d.pop("name")

        num_history = d.pop("num_history")

        role_delete_protection_on_by_default = d.pop("role_delete_protection_on_by_default")

        project_id = d.pop("project_id", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        created_by = d.pop("created_by", UNSET)

        group_schema = cls(
            id=id,
            is_delete_protected=is_delete_protected,
            is_active=is_active,
            created_date=created_date,
            last_updated_by=last_updated_by,
            tags=tags,
            name=name,
            num_history=num_history,
            role_delete_protection_on_by_default=role_delete_protection_on_by_default,
            project_id=project_id,
            last_updated_date=last_updated_date,
            created_by=created_by,
        )

        group_schema.additional_properties = d
        return group_schema

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
