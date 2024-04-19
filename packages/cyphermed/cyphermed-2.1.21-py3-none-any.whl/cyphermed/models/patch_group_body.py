from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchGroupBody")


@_attrs_define
class PatchGroupBody:
    """Which Group fields to include in PATCH request bodies

    Attributes:
        name (Union[Unset, str]): Name of the group
        is_active (Union[Unset, bool]): Whether this group is active
        is_delete_protected (Union[Unset, bool]): This must be set false before the group can be deleted
        tags (Union[Unset, List[str]]): List of tags on this group
        project_id (Union[Unset, str]): ID of the project this group belongs to, if any
    """

    name: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    project_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        is_active = self.is_active

        is_delete_protected = self.is_delete_protected

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        project_id = d.pop("project_id", UNSET)

        patch_group_body = cls(
            name=name,
            is_active=is_active,
            is_delete_protected=is_delete_protected,
            tags=tags,
            project_id=project_id,
        )

        patch_group_body.additional_properties = d
        return patch_group_body

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
