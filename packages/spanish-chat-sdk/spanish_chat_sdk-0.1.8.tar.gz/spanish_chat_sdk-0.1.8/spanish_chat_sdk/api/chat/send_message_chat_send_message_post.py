from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.send_message_chat_send_message_post_response_send_message_chat_send_message_post import (
    SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    message: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["message"] = message

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/chat/send-message",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    message: str,
) -> Response[Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]]:
    """Send Message

    Args:
        message (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]]
    """

    kwargs = _get_kwargs(
        message=message,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    message: str,
) -> Optional[Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]]:
    """Send Message

    Args:
        message (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]
    """

    return sync_detailed(
        client=client,
        message=message,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    message: str,
) -> Response[Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]]:
    """Send Message

    Args:
        message (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]]
    """

    kwargs = _get_kwargs(
        message=message,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    message: str,
) -> Optional[Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]]:
    """Send Message

    Args:
        message (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, SendMessageChatSendMessagePostResponseSendMessageChatSendMessagePost]
    """

    return (
        await asyncio_detailed(
            client=client,
            message=message,
        )
    ).parsed
