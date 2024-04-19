import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.project_schema_allowed_login_fields import (
        ProjectSchemaAllowedLoginFields,
    )
    from ..models.project_schema_custom_settings import ProjectSchemaCustomSettings


T = TypeVar("T", bound="ProjectSchema")


@_attrs_define
class ProjectSchema:
    """Which Project fields to include in response bodies

    Attributes:
        name (str):
        created_date (datetime.datetime):
        id (str): ID of the project
        tags (List[str]): List of tags on this project
        description (Union[Unset, str]):  Default: ''.
        allowed_login_fields (Union[Unset, ProjectSchemaAllowedLoginFields]):
        custom_settings (Union[Unset, ProjectSchemaCustomSettings]):
        device_owners_have_admin_access (Union[Unset, bool]):  Default: False.
        device_owners_can_tunnel (Union[Unset, bool]):  Default: False.
        device_creators_are_owners_by_default (Union[Unset, bool]):  Default: False.
        group_delete_protection_on_by_default (Union[Unset, bool]):  Default: False.
        role_delete_protection_on_by_default (Union[Unset, bool]):  Default: False.
        is_delete_protected (Union[Unset, bool]):  Default: False.
        is_active (Union[Unset, bool]):  Default: True.
        last_updated_date (Union[Unset, datetime.datetime]):
        default_locale (Union[Unset, str]):
        default_from_address (Union[Unset, str]):
        reset_token_expire_hours (Union[Unset, int]):  Default: 24.
        access_token_expire_hours (Union[Unset, int]):  Default: 1.
        refresh_token_expire_hours (Union[Unset, int]):  Default: 24.
        session_expire_mins (Union[Unset, int]):  Default: 15.
        pii_admin_only (Union[Unset, bool]):  Default: False.
    """

    name: str
    created_date: datetime.datetime
    id: str
    tags: List[str]
    description: Union[Unset, str] = ""
    allowed_login_fields: Union[Unset, "ProjectSchemaAllowedLoginFields"] = UNSET
    custom_settings: Union[Unset, "ProjectSchemaCustomSettings"] = UNSET
    device_owners_have_admin_access: Union[Unset, bool] = False
    device_owners_can_tunnel: Union[Unset, bool] = False
    device_creators_are_owners_by_default: Union[Unset, bool] = False
    group_delete_protection_on_by_default: Union[Unset, bool] = False
    role_delete_protection_on_by_default: Union[Unset, bool] = False
    is_delete_protected: Union[Unset, bool] = False
    is_active: Union[Unset, bool] = True
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    default_locale: Union[Unset, str] = UNSET
    default_from_address: Union[Unset, str] = UNSET
    reset_token_expire_hours: Union[Unset, int] = 24
    access_token_expire_hours: Union[Unset, int] = 1
    refresh_token_expire_hours: Union[Unset, int] = 24
    session_expire_mins: Union[Unset, int] = 15
    pii_admin_only: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        created_date = self.created_date.isoformat()

        id = self.id

        tags = self.tags

        description = self.description

        allowed_login_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allowed_login_fields, Unset):
            allowed_login_fields = self.allowed_login_fields.to_dict()

        custom_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_settings, Unset):
            custom_settings = self.custom_settings.to_dict()

        device_owners_have_admin_access = self.device_owners_have_admin_access

        device_owners_can_tunnel = self.device_owners_can_tunnel

        device_creators_are_owners_by_default = self.device_creators_are_owners_by_default

        group_delete_protection_on_by_default = self.group_delete_protection_on_by_default

        role_delete_protection_on_by_default = self.role_delete_protection_on_by_default

        is_delete_protected = self.is_delete_protected

        is_active = self.is_active

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        default_locale = self.default_locale

        default_from_address = self.default_from_address

        reset_token_expire_hours = self.reset_token_expire_hours

        access_token_expire_hours = self.access_token_expire_hours

        refresh_token_expire_hours = self.refresh_token_expire_hours

        session_expire_mins = self.session_expire_mins

        pii_admin_only = self.pii_admin_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_date": created_date,
                "id": id,
                "tags": tags,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if allowed_login_fields is not UNSET:
            field_dict["allowed_login_fields"] = allowed_login_fields
        if custom_settings is not UNSET:
            field_dict["custom_settings"] = custom_settings
        if device_owners_have_admin_access is not UNSET:
            field_dict["device_owners_have_admin_access"] = device_owners_have_admin_access
        if device_owners_can_tunnel is not UNSET:
            field_dict["device_owners_can_tunnel"] = device_owners_can_tunnel
        if device_creators_are_owners_by_default is not UNSET:
            field_dict["device_creators_are_owners_by_default"] = (
                device_creators_are_owners_by_default
            )
        if group_delete_protection_on_by_default is not UNSET:
            field_dict["group_delete_protection_on_by_default"] = (
                group_delete_protection_on_by_default
            )
        if role_delete_protection_on_by_default is not UNSET:
            field_dict["role_delete_protection_on_by_default"] = (
                role_delete_protection_on_by_default
            )
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if default_from_address is not UNSET:
            field_dict["default_from_address"] = default_from_address
        if reset_token_expire_hours is not UNSET:
            field_dict["reset_token_expire_hours"] = reset_token_expire_hours
        if access_token_expire_hours is not UNSET:
            field_dict["access_token_expire_hours"] = access_token_expire_hours
        if refresh_token_expire_hours is not UNSET:
            field_dict["refresh_token_expire_hours"] = refresh_token_expire_hours
        if session_expire_mins is not UNSET:
            field_dict["session_expire_mins"] = session_expire_mins
        if pii_admin_only is not UNSET:
            field_dict["pii_admin_only"] = pii_admin_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_schema_allowed_login_fields import (
            ProjectSchemaAllowedLoginFields,
        )
        from ..models.project_schema_custom_settings import ProjectSchemaCustomSettings

        d = src_dict.copy()
        name = d.pop("name")

        created_date = isoparse(d.pop("created_date"))

        id = d.pop("id")

        tags = cast(List[str], d.pop("tags"))

        description = d.pop("description", UNSET)

        _allowed_login_fields = d.pop("allowed_login_fields", UNSET)
        allowed_login_fields: Union[Unset, ProjectSchemaAllowedLoginFields]
        if isinstance(_allowed_login_fields, Unset):
            allowed_login_fields = UNSET
        else:
            allowed_login_fields = ProjectSchemaAllowedLoginFields.from_dict(_allowed_login_fields)

        _custom_settings = d.pop("custom_settings", UNSET)
        custom_settings: Union[Unset, ProjectSchemaCustomSettings]
        if isinstance(_custom_settings, Unset):
            custom_settings = UNSET
        else:
            custom_settings = ProjectSchemaCustomSettings.from_dict(_custom_settings)

        device_owners_have_admin_access = d.pop("device_owners_have_admin_access", UNSET)

        device_owners_can_tunnel = d.pop("device_owners_can_tunnel", UNSET)

        device_creators_are_owners_by_default = d.pop(
            "device_creators_are_owners_by_default", UNSET
        )

        group_delete_protection_on_by_default = d.pop(
            "group_delete_protection_on_by_default", UNSET
        )

        role_delete_protection_on_by_default = d.pop("role_delete_protection_on_by_default", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        is_active = d.pop("is_active", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        default_locale = d.pop("default_locale", UNSET)

        default_from_address = d.pop("default_from_address", UNSET)

        reset_token_expire_hours = d.pop("reset_token_expire_hours", UNSET)

        access_token_expire_hours = d.pop("access_token_expire_hours", UNSET)

        refresh_token_expire_hours = d.pop("refresh_token_expire_hours", UNSET)

        session_expire_mins = d.pop("session_expire_mins", UNSET)

        pii_admin_only = d.pop("pii_admin_only", UNSET)

        project_schema = cls(
            name=name,
            created_date=created_date,
            id=id,
            tags=tags,
            description=description,
            allowed_login_fields=allowed_login_fields,
            custom_settings=custom_settings,
            device_owners_have_admin_access=device_owners_have_admin_access,
            device_owners_can_tunnel=device_owners_can_tunnel,
            device_creators_are_owners_by_default=device_creators_are_owners_by_default,
            group_delete_protection_on_by_default=group_delete_protection_on_by_default,
            role_delete_protection_on_by_default=role_delete_protection_on_by_default,
            is_delete_protected=is_delete_protected,
            is_active=is_active,
            last_updated_date=last_updated_date,
            default_locale=default_locale,
            default_from_address=default_from_address,
            reset_token_expire_hours=reset_token_expire_hours,
            access_token_expire_hours=access_token_expire_hours,
            refresh_token_expire_hours=refresh_token_expire_hours,
            session_expire_mins=session_expire_mins,
            pii_admin_only=pii_admin_only,
        )

        project_schema.additional_properties = d
        return project_schema

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
