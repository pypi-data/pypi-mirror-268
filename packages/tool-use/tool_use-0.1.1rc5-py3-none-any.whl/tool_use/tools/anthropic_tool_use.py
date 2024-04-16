import asyncio
import functools
import inspect
import json
import re
import time
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Tuple, TypedDict

from anthropic import (
    AnthropicError,
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AsyncMessageStreamManager,
    AsyncMessageStreamT,
    RateLimitError,
)
from anthropic.types import Message
from anthropic.types.beta.tools import (
    ToolParam,
    ToolsBetaMessage,
    ToolsBetaMessageParam,
)
from anthropic.types.message_param import MessageParam
from promptflow import tool
from promptflow.connections import CustomStrongTypeConnection
from promptflow.contracts.types import PromptTemplate, Secret
from promptflow.exceptions import SystemErrorException, UserErrorException
from promptflow.tools.common import (
    generate_retry_interval,
    render_jinja_template,
    to_bool,
    validate_role,
)
from promptflow.tools.exception import (
    ChatAPIInvalidFunctions,
    ExceedMaxRetryTimes,
    FunctionCallNotSupportedInStreamMode,
    LLMError,
    WrappedOpenAIError,
)

try:
    from anthropic import AsyncAnthropic as AnthropicClient
    from anthropic import AsyncAnthropicBedrock as AnthropicBedrockClient
    from anthropic import AsyncAnthropicVertex as AnthropicVertexClient
except Exception:
    raise Exception(
        "Please set your Anthropic package to version 0.23.1 or later using the command: pip install --upgrade anthropic."
    )

CLAUDE_API_TYPES = Literal["vertex_anthropic", "bedrock_anthropic", "anthropic"]


class AnthropicConnection(CustomStrongTypeConnection):
    """
    Anthropic Custom connection

    :param api_key: The api key.
    :type api_key: Secret
    :param api_base: The api base url.
    :type api_base: str
    :param api_type: The api type (available type: vertex_anthropic, bedrock_anthropic).
    :type api_type: str
    """

    api_key: Secret
    client_key: Secret
    api_base: Secret
    api_type: Secret = "anthropic"


class WrappedAnthropicError(WrappedOpenAIError):
    pass


class ModelEnum(str, Enum):
    CLAUDE_3_OPUS_240229 = "claude-3-opus-20240229"
    CLAUDE_3_SONET_240229 = "claude-3-sonnet-20240229"
    CLAUDE_3_HAIKU_240307 = "claude-3-haiku-20240307"
    CLAUDE_2_1 = "claude-2.1"
    CLAUDE_2_0 = "claude-2.0"
    CLAUDE_INSTANT_1_2 = "claude-instant-1.2"


class ToolFunctionDict(TypedDict):
    parameters: object
    description: str
    name: str


class ToolDict(TypedDict):
    type: str
    function: ToolFunctionDict


class ToolChoiceFunctionDict(TypedDict):
    name: str


class ToolChoiceDict(TypedDict):
    type: str
    function: ToolChoiceFunctionDict


def _normalize_connection_config(connection: AnthropicConnection):
    extra_config = {}
    typ = connection.api_type
    if typ == "anthropic":
        extra_config = {
            "api_key": connection.api_key,
            "base_url": connection.api_base,
        }
    elif typ == "bedrock_anthropic":
        extra_config = {
            "aws_secret_key": connection.api_key,
            "aws_access_key": connection.client_key,
            "aws_region": "ap-northeast-2",
            "base_url": connection.api_base,
        }
    return {
        "max_retries": 0,
        "timeout": None,
        "_strict_response_validation": True,
        **extra_config,
    }


def parse_template(
    template: str, valid_roles: list[str]
) -> Tuple[List[Dict[str, Any]], bool]:
    results = []

    # Regex to extract the whole section content
    separator = r"(?i)^\s*#?\s*(" + "|".join(valid_roles) + r")\s*:\s*\n"
    chunks = re.split(separator, template, flags=re.MULTILINE)
    is_tool_use = False
    for chunk in chunks:
        last_message = results[-1] if len(results) > 0 else None
        if last_message and "role" in last_message and "content" not in last_message:
            parsed_chunk = parse_section(chunk)
            if "text" in parsed_chunk:
                last_message["content"] = {
                    "type": "text",
                    "text": parsed_chunk["text"].strip(),
                }
            else:
                last_message["content"] = parsed_chunk
            # figure out whether there is type called tool_use or tool_result
            is_tool_use |= any(map(lambda x: x["type"] == "tool_use", parsed_chunk))
        else:
            if chunk.strip() == "":
                continue
            role = chunk.strip().lower()
            validate_role(role, valid_roles=valid_roles)
            new_message = dict(role=role)
            results.append(new_message)

    return results, is_tool_use


def parse_section(content: str) -> List[Dict[str, Any]]:
    content_list = []
    # Regex to capture entries by type
    type_entries = re.split(r"\n(?=type:)", content)
    for entry in type_entries:
        if entry.strip():  # Ensure entry is not just whitespace
            entry_data = parse_entry(entry)
            if entry_data["type"] is None:
                entry_data = {"type": "text", "text": content}
            content_list.append(entry_data)
    if not type_entries:
        return
    return content_list


def parse_entry(entry: str) -> Dict[str, Any]:
    # Initial split to separate type from details
    first_line, *details = entry.split("\n")
    type_match = re.match(r"type:\s*(.*)", first_line)
    type_key = type_match.group(1).strip() if type_match else None
    details = "\n".join(details)
    entry_details = parse_details(details)
    entry_details["type"] = type_key
    return entry_details


def parse_details(details: str) -> Dict[str, Any]:
    details_data = {}
    details_regex = r"(\w+):\s*(.*)"
    for key, value in re.findall(details_regex, details):
        # Try to convert `value` into a dictionary if it starts with `{`
        if value.startswith("{"):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                pass
        details_data[key] = value
    return details_data


def _parse_chat(
    chat_str: str,
) -> Tuple[str | None, list[MessageParam | ToolsBetaMessageParam], bool]:

    valid_roles = ["system", "user", "assistant"]
    messages, is_tool_use = parse_template(chat_str, valid_roles)

    if messages[0]["role"] == "system":
        system = messages[0]["content"][0]["text"]
        chat_list = messages[1:]
    else:
        system = None
        chat_list = messages

    return system, chat_list, is_tool_use


# TODO(2971352): revisit this tries=5 when there is any change to the 10min timeout logic
def handle_anthropic_error(tries: int = 5):
    """
    A decorator function that used to handle Anthropic error.
    Anthropic Error falls into retriable vs non-retriable ones.

    For retriable error, the decorator use below parameters to control its retry activity with exponential backoff:
     `tries` : max times for the function invocation, type is int
     'delay': base delay seconds for exponential delay, type is float
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(tries + 1):
                try:
                    return func(*args, **kwargs)
                except (SystemErrorException, UserErrorException) as e:
                    # Throw inner wrapped exception directly
                    raise e
                except (APIStatusError, APIConnectionError) as e:
                    if (
                        isinstance(e, APIConnectionError)
                        and not isinstance(e, APITimeoutError)
                        and "connection aborted" not in str(e).lower()
                    ):
                        raise WrappedAnthropicError(e)
                    # Retry InternalServerError(>=500), RateLimitError(429)
                    if isinstance(e, APIStatusError):
                        status_code = e.response.status_code
                        if status_code < 500 and status_code not in [429]:
                            raise WrappedAnthropicError(e)
                    if (
                        isinstance(e, RateLimitError)
                        and getattr(e, "type", None) == "insufficient_quota"
                    ):
                        raise WrappedAnthropicError(e)
                    if i == tries:
                        raise ExceedMaxRetryTimes(e)

                    # TODO: Add retry logic here
                    if hasattr(e, "response") and e.response is not None:
                        retry_after_in_header = e.response.headers.get(
                            "retry-after", None
                        )
                    else:
                        retry_after_in_header = None

                    if not retry_after_in_header:
                        retry_after_seconds = generate_retry_interval(i)
                        (
                            f"{type(e).__name__} #{i}, but no Retry-After header, "
                            + f"Back off {retry_after_seconds} seconds for retry."
                        )
                    else:
                        retry_after_seconds = float(retry_after_in_header)
                        (
                            f"{type(e).__name__} #{i}, Retry-After={retry_after_in_header}, "
                            f"Back off {retry_after_seconds} seconds for retry."
                        )
                        # print(msg, file=sys.stderr)
                    time.sleep(retry_after_seconds)
                except AnthropicError as e:
                    raise WrappedAnthropicError(e)
                except Exception as e:
                    error_message = (
                        f"Anthropic API hits exception: {type(e).__name__}: {str(e)}"
                    )
                    raise LLMError(message=error_message)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            for i in range(tries + 1):
                try:
                    return await func(*args, **kwargs)
                except (SystemErrorException, UserErrorException) as e:
                    # Throw inner wrapped exception directly
                    raise e
                except (APIStatusError, APIConnectionError) as e:
                    if (
                        isinstance(e, APIConnectionError)
                        and not isinstance(e, APITimeoutError)
                        and "connection aborted" not in str(e).lower()
                    ):
                        raise WrappedAnthropicError(e)
                    # Retry InternalServerError(>=500), RateLimitError(429), UnprocessableEntityError(422)
                    if isinstance(e, APIStatusError):
                        status_code = e.response.status_code
                        if status_code < 500 and status_code not in [429]:
                            raise WrappedAnthropicError(e)
                    if (
                        isinstance(e, RateLimitError)
                        and getattr(e, "type", None) == "insufficient_quota"
                    ):
                        # Exit retry if this is quota insufficient error
                        # print(
                        #     f"{type(e).__name__} with insufficient quota. Throw user error.",
                        #     file=sys.stderr,
                        # )
                        raise WrappedAnthropicError(e)
                    if i == tries:
                        # Exit retry if max retry reached
                        # print(
                        #     f"{type(e).__name__} reached max retry. Exit retry with user error.",
                        #     file=sys.stderr,
                        # )
                        raise ExceedMaxRetryTimes(e)

                    # TODO: Add retry logic here
                    if hasattr(e, "response") and e.response is not None:
                        retry_after_in_header = e.response.headers.get(
                            "retry-after", None
                        )
                    else:
                        retry_after_in_header = None

                    if not retry_after_in_header:
                        retry_after_seconds = generate_retry_interval(i)
                        (
                            f"{type(e).__name__} #{i}, but no Retry-After header, "
                            + f"Back off {retry_after_seconds} seconds for retry."
                        )
                        # print(msg, file=sys.stderr)
                    else:
                        retry_after_seconds = float(retry_after_in_header)
                        (
                            f"{type(e).__name__} #{i}, Retry-After={retry_after_in_header}, "
                            f"Back off {retry_after_seconds} seconds for retry."
                        )
                        # print(msg, file=sys.stderr)
                    await asyncio.sleep(retry_after_seconds)
                except AnthropicError as e:
                    raise WrappedAnthropicError(e)
                except Exception as e:
                    error_message = (
                        f"Anthropic API hits exception: {type(e).__name__}: {str(e)}"
                    )
                    raise LLMError(message=error_message)

        return wrapper if not inspect.iscoroutinefunction(func) else async_wrapper

    return decorator


def async_post_process_chat_api_response(
    completion: AsyncMessageStreamManager[AsyncMessageStreamT] | Message,
    stream,
    functions,
):
    if stream:
        if functions is not None:
            error_message = (
                "Function calling has not been supported by stream mode yet."
            )
            raise FunctionCallNotSupportedInStreamMode(message=error_message)

        async def generator():
            assert isinstance(
                completion, AsyncMessageStreamManager
            ), "Invalid type. Expected AsyncMessageStreamManager."
            async with completion as stream:
                async for chunk in stream.text_stream:
                    yield chunk

        return generator()
    else:
        assert isinstance(completion, Message) or isinstance(
            completion, ToolsBetaMessage
        ), "Invalid type. Expected Message."
        # When calling function, function_call response will be returned as a field in message, so we need return
        # message directly. Otherwise, we only return content.
        if functions is not None:
            return completion.model_dump()["content"]
        else:
            # chat api may return message with no content.
            return completion.model_dump()["content"]


@tool
@handle_anthropic_error()
async def anthropic_tool_use(
    connection: AnthropicConnection,
    prompt: PromptTemplate,
    model: ModelEnum,
    max_tokens: int,
    temperature: float = 1,
    top_p: float = 1,
    n: int = 1,
    stream: Optional[bool] = False,
    stop: Optional[list] = None,  # type: ignore
    user: Optional[str] = "",
    tools: Optional[list[ToolParam]] = None,  # type: ignore
    extra_headers: Optional[dict] = {},
    is_raw_output: Optional[bool] = False,
    **kwargs,
) -> str | dict | Message | AsyncMessageStreamManager:  # type: ignore
    chat_str = render_jinja_template(
        prompt, trim_blocks=True, keep_trailing_newline=True, **kwargs
    )
    system, messages, is_tool_use = _parse_chat(chat_str)
    # TODO: remove below type conversion after client can pass json rather than string.
    stream = to_bool(stream)
    params = {
        "model": model,
        "messages": messages,
        "system": system,
        "temperature": float(temperature),
        "top_p": float(top_p),
        "top_k": int(n),
        "stop_sequences": stop if stop else None,
        "max_tokens": int(max_tokens)
        if max_tokens is not None and str(max_tokens).lower() != "inf"
        else None,
        "metadata": {"user_id": user},
    }

    if tools is not None:
        for tool_desc in tools:
            if (
                "name" in tool_desc
                and "description" in tool_desc
                and "input_schema" in tool_desc
                and "type" in tool_desc.get("input_schema", {})
                and "properties" in tool_desc.get("input_schema", {})
                and "required" in tool_desc.get("input_schema", {})
            ):
                pass
            else:
                raise ChatAPIInvalidFunctions(
                    message=f"tools parameter is invalid: {tools}"
                )
        params["tools"] = tools
    else:
        assert not is_tool_use, "tools parameter is required for tool use."

    _connection_dict = _normalize_connection_config(connection)
    _client = None
    if connection.api_type == "anthropic":
        _client = AnthropicClient(**_connection_dict)
    elif connection.api_type == "vertex_anthropic":
        _client = AnthropicVertexClient(**_connection_dict)
    elif connection.api_type == "bedrock_anthropic":
        _client = AnthropicBedrockClient(**_connection_dict)

    if tools:
        if stream:
            response = _client.beta.tools.messages.stream(
                **params,
                extra_headers=extra_headers,
            )
        else:
            response = await _client.beta.tools.messages.create(
                **params,
                extra_headers=extra_headers,
            )
    else:
        if stream:
            response = _client.messages.stream(
                **params,
                extra_headers=extra_headers,
            )
        else:
            response = await _client.messages.create(
                **params,
                extra_headers=extra_headers,
            )
    return (
        async_post_process_chat_api_response(response, stream, tools)
        if not is_raw_output
        else response
    )
