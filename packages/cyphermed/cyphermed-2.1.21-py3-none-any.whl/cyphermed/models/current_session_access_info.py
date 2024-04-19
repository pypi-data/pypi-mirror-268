from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.org_access_schema import OrgAccessSchema
    from ..models.project_access_schema import ProjectAccessSchema


T = TypeVar("T", bound="CurrentSessionAccessInfo")


@_attrs_define
class CurrentSessionAccessInfo:
    """Current session access info

    Attributes:
        org_access (OrgAccessSchema): Access for an organization
        project_access (Union[Unset, ProjectAccessSchema]): Which Project fields to include in response bodies
    """

    org_access: "OrgAccessSchema"
    project_access: Union[Unset, "ProjectAccessSchema"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        org_access = self.org_access.to_dict()

        project_access: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_access, Unset):
            project_access = self.project_access.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_access": org_access,
            }
        )
        if project_access is not UNSET:
            field_dict["project_access"] = project_access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.org_access_schema import OrgAccessSchema
        from ..models.project_access_schema import ProjectAccessSchema

        d = src_dict.copy()
        org_access = OrgAccessSchema.from_dict(d.pop("org_access"))

        _project_access = d.pop("project_access", UNSET)
        project_access: Union[Unset, ProjectAccessSchema]
        if isinstance(_project_access, Unset):
            project_access = UNSET
        else:
            project_access = ProjectAccessSchema.from_dict(_project_access)

        current_session_access_info = cls(
            org_access=org_access,
            project_access=project_access,
        )

        current_session_access_info.additional_properties = d
        return current_session_access_info

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
