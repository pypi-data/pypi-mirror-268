from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CreateProjectBody")


@_attrs_define
class CreateProjectBody:
    """Create project body

    Attributes:
        name (str): Name of the project
        description (Union[Unset, str]): Description of the project
        is_delete_protected (Union[Unset, bool]): Must be false before the project can be deleted
        tags (Union[Unset, List[str]]): List of tags on this project
        reset_token_expire_hours (Union[Unset, int]): Number of hours reset tokens are valid
        access_token_expire_hours (Union[Unset, int]): Number of hours access tokens are valid
        refresh_token_expire_hours (Union[Unset, int]): Number of hours refresh tokens are valid
        session_expire_mins (Union[Unset, int]): Number of mins sessions are valid
        default_locale (Union[Unset, str]): Default locale for the organization Default: 'en-US'.
        default_from_address (Union[Unset, str]): Default from address Default: 'noreply@cyphermed.cloud'.
        allowed_login_fields (Union[Unset, List[str]]): Allowed login fields
    """

    name: str
    description: Union[Unset, str] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    reset_token_expire_hours: Union[Unset, int] = UNSET
    access_token_expire_hours: Union[Unset, int] = UNSET
    refresh_token_expire_hours: Union[Unset, int] = UNSET
    session_expire_mins: Union[Unset, int] = UNSET
    default_locale: Union[Unset, str] = "en-US"
    default_from_address: Union[Unset, str] = "noreply@cyphermed.cloud"
    allowed_login_fields: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        is_delete_protected = self.is_delete_protected

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        reset_token_expire_hours = self.reset_token_expire_hours

        access_token_expire_hours = self.access_token_expire_hours

        refresh_token_expire_hours = self.refresh_token_expire_hours

        session_expire_mins = self.session_expire_mins

        default_locale = self.default_locale

        default_from_address = self.default_from_address

        allowed_login_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_login_fields, Unset):
            allowed_login_fields = self.allowed_login_fields

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if reset_token_expire_hours is not UNSET:
            field_dict["reset_token_expire_hours"] = reset_token_expire_hours
        if access_token_expire_hours is not UNSET:
            field_dict["access_token_expire_hours"] = access_token_expire_hours
        if refresh_token_expire_hours is not UNSET:
            field_dict["refresh_token_expire_hours"] = refresh_token_expire_hours
        if session_expire_mins is not UNSET:
            field_dict["session_expire_mins"] = session_expire_mins
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if default_from_address is not UNSET:
            field_dict["default_from_address"] = default_from_address
        if allowed_login_fields is not UNSET:
            field_dict["allowed_login_fields"] = allowed_login_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        reset_token_expire_hours = d.pop("reset_token_expire_hours", UNSET)

        access_token_expire_hours = d.pop("access_token_expire_hours", UNSET)

        refresh_token_expire_hours = d.pop("refresh_token_expire_hours", UNSET)

        session_expire_mins = d.pop("session_expire_mins", UNSET)

        default_locale = d.pop("default_locale", UNSET)

        default_from_address = d.pop("default_from_address", UNSET)

        allowed_login_fields = cast(List[str], d.pop("allowed_login_fields", UNSET))

        create_project_body = cls(
            name=name,
            description=description,
            is_delete_protected=is_delete_protected,
            tags=tags,
            reset_token_expire_hours=reset_token_expire_hours,
            access_token_expire_hours=access_token_expire_hours,
            refresh_token_expire_hours=refresh_token_expire_hours,
            session_expire_mins=session_expire_mins,
            default_locale=default_locale,
            default_from_address=default_from_address,
            allowed_login_fields=allowed_login_fields,
        )

        create_project_body.additional_properties = d
        return create_project_body

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
