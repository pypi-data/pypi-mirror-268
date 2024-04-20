from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.message import Message
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    only_user: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["only_user"] = only_user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/conversations/active-messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, List["Message"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Message.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, List["Message"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    only_user: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, List["Message"]]]:
    """Get Current Conversation Messages

    Args:
        only_user (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['Message']]]
    """

    kwargs = _get_kwargs(
        only_user=only_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    only_user: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, List["Message"]]]:
    """Get Current Conversation Messages

    Args:
        only_user (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, List['Message']]
    """

    return sync_detailed(
        client=client,
        only_user=only_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    only_user: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError, List["Message"]]]:
    """Get Current Conversation Messages

    Args:
        only_user (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['Message']]]
    """

    kwargs = _get_kwargs(
        only_user=only_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    only_user: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError, List["Message"]]]:
    """Get Current Conversation Messages

    Args:
        only_user (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, List['Message']]
    """

    return (
        await asyncio_detailed(
            client=client,
            only_user=only_user,
        )
    ).parsed
