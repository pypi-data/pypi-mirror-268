from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_role_access_body import PatchRoleAccessBody
from ...models.success import Success
from ...types import Response


def _get_kwargs(
    role_id: str,
    account_id: str,
    *,
    json_body: PatchRoleAccessBody,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/v2/roles/{role_id}/access/{account_id}".format(
            role_id=role_id,
            account_id=account_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Success]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Success.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Success]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchRoleAccessBody,
) -> Response[Success]:
    """Patch Role Access By Id

     Patch role access by ID

    Args:
        role_id (str):
        account_id (str):
        json_body (PatchRoleAccessBody): Which RoleAccess fields to include in request bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        account_id=account_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchRoleAccessBody,
) -> Optional[Success]:
    """Patch Role Access By Id

     Patch role access by ID

    Args:
        role_id (str):
        account_id (str):
        json_body (PatchRoleAccessBody): Which RoleAccess fields to include in request bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return sync_detailed(
        role_id=role_id,
        account_id=account_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchRoleAccessBody,
) -> Response[Success]:
    """Patch Role Access By Id

     Patch role access by ID

    Args:
        role_id (str):
        account_id (str):
        json_body (PatchRoleAccessBody): Which RoleAccess fields to include in request bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        account_id=account_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchRoleAccessBody,
) -> Optional[Success]:
    """Patch Role Access By Id

     Patch role access by ID

    Args:
        role_id (str):
        account_id (str):
        json_body (PatchRoleAccessBody): Which RoleAccess fields to include in request bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            account_id=account_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
