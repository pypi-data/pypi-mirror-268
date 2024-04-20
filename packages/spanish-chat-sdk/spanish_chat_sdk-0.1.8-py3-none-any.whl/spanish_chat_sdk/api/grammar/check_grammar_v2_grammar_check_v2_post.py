from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.grammar_errors_v2 import GrammarErrorsV2
from ...models.http_validation_error import HTTPValidationError
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
        "url": "/grammar/check_v2",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GrammarErrorsV2, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GrammarErrorsV2.from_dict(response.json())

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
) -> Response[Union[Any, GrammarErrorsV2, HTTPValidationError]]:
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
) -> Response[Union[Any, GrammarErrorsV2, HTTPValidationError]]:
    """Check Grammar V2

    Args:
        message (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GrammarErrorsV2, HTTPValidationError]]
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
) -> Optional[Union[Any, GrammarErrorsV2, HTTPValidationError]]:
    """Check Grammar V2

    Args:
        message (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GrammarErrorsV2, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        message=message,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    message: str,
) -> Response[Union[Any, GrammarErrorsV2, HTTPValidationError]]:
    """Check Grammar V2

    Args:
        message (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GrammarErrorsV2, HTTPValidationError]]
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
) -> Optional[Union[Any, GrammarErrorsV2, HTTPValidationError]]:
    """Check Grammar V2

    Args:
        message (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GrammarErrorsV2, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            message=message,
        )
    ).parsed
