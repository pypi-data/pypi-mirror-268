from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success import Success
from ...types import UNSET, Response, Unset


def _get_kwargs(
    role_id: str,
    *,
    permanent: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    params["permanent"] = permanent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": "/v2/roles/{role_id}".format(
            role_id=role_id,
        ),
        "params": params,
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
    *,
    client: AuthenticatedClient,
    permanent: Union[Unset, None, bool] = UNSET,
) -> Response[Success]:
    """Delete Role By Id

     Delete a role by ID

    Args:
        role_id (str):
        permanent (Union[Unset, None, bool]): If true, the role will be permanently deleted

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        permanent=permanent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_id: str,
    *,
    client: AuthenticatedClient,
    permanent: Union[Unset, None, bool] = UNSET,
) -> Optional[Success]:
    """Delete Role By Id

     Delete a role by ID

    Args:
        role_id (str):
        permanent (Union[Unset, None, bool]): If true, the role will be permanently deleted

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
        permanent=permanent,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    *,
    client: AuthenticatedClient,
    permanent: Union[Unset, None, bool] = UNSET,
) -> Response[Success]:
    """Delete Role By Id

     Delete a role by ID

    Args:
        role_id (str):
        permanent (Union[Unset, None, bool]): If true, the role will be permanently deleted

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        permanent=permanent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_id: str,
    *,
    client: AuthenticatedClient,
    permanent: Union[Unset, None, bool] = UNSET,
) -> Optional[Success]:
    """Delete Role By Id

     Delete a role by ID

    Args:
        role_id (str):
        permanent (Union[Unset, None, bool]): If true, the role will be permanently deleted

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
            permanent=permanent,
        )
    ).parsed
