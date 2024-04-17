import asyncio
import functools
import inspect
import json
import re
import time
from ast import literal_eval
from enum import Enum
from typing import List, Optional, cast

from openai import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    OpenAIError,
    RateLimitError,
)
from openai.types.chat.chat_completion_named_tool_choice_param import (
    ChatCompletionNamedToolChoiceParam,
)
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam
from promptflow import tool
from promptflow.connections import AzureOpenAIConnection, OpenAIConnection
from promptflow.contracts.types import PromptTemplate
from promptflow.exceptions import SystemErrorException, UserErrorException
from promptflow.tools.common import (
    generate_retry_interval,
    normalize_connection_config,
    process_function_call,
    render_jinja_template,
    to_bool,
    to_content_str_or_list,
    try_parse_name_and_content,
    validate_functions,
    validate_role,
)
from promptflow.tools.exception import (
    ChatAPIFunctionRoleInvalidFormat,
    ChatAPIInvalidFunctions,
    ExceedMaxRetryTimes,
    FunctionCallNotSupportedInStreamMode,
    LLMError,
    WrappedOpenAIError,
)

try:
    from openai import AsyncAzureOpenAI as AzureOpenAIClient
    from openai import AsyncOpenAI as OpenAIClient
except Exception:
    raise Exception(
        "Please upgrade your OpenAI package to version 1.0.0 or later using the command: pip install --upgrade openai."
    )


class ModelEnum(str, Enum):
    GPT_35_TURBO_0301 = "gpt-3.5-turbo-0301"
    GPT_35_TURBO_0613 = "gpt-3.5-turbo-0613"
    GPT_35_TURBO_1106 = "gpt-3.5-turbo-1106"
    GPT_35_TURBO_0125 = "gpt-3.5-turbo-0125"
    GPT_35_TURBO_16K_0613 = "gpt-3.5-turbo-16k-0613"
    GPT_35_TURBO_INSTRUCT = "gpt-3.5-turbo-instruct"
    GPT_35_TURBO_INSTRUCT_0914 = "gpt-3.5-turbo-instruct-0914"
    GPT_4_0125_PREVIEW = "gpt-4-0125-preview"
    GPT_4_1106_PREVIEW = "gpt-4-1106-preview"
    GPT_4_1106_VISION_PREVIEW = "gpt-4-1106-vision-preview"
    GPT_4_240409 = "gpt-4-turbo-2024-04-09"
    GPT_4_0613 = "gpt-4-0613"


class CompletionNoneExceptionFlag:
    def __init__(self) -> None:
        self._flag = False

    def set_flag_true(self) -> None:
        self._flag = True

    def get_flag(self) -> bool:
        return self._flag


class CompletionNoneException(Exception):
    """Exception raised when openai completion object is None."""

    def __init__(self) -> None:
        super().__init__("openai completion object is None.")

    def is_first_exception(self, flag: CompletionNoneExceptionFlag) -> bool:
        """
        If flag is false, set flag as true and return true.
        If flag is true, return false.
        """
        if not flag.get_flag():
            flag.set_flag_true()
            return True
        else:
            return False


def _try_parse_tool_message(role_prompt):
    # customer can add ## in front of name/content for markdown highlight.
    # and we still support name/content without ## prefix for backward compatibility.
    pattern = r"\n*#{0,2}\s*tool_call_id:\n+\s*(\S+)\s*\n*#{0,2}\s*content:\n?(.*)"
    match = re.search(pattern, role_prompt, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None


def _try_parse_tool_calls(role_prompt):
    # customer can add ## in front of name/content for markdown highlight.
    # and we still support name/content without ## prefix for backward compatibility.
    pattern = r"\n*#{0,2}\s*tool_calls:\n?(.*)"
    match = re.search(pattern, role_prompt, re.DOTALL)
    if match:
        rendered = literal_eval(match.group(1))
        for v in rendered:
            v["function"]["arguments"] = str(v["function"]["arguments"])
        return rendered
    return None


def _parse_chat(
    chat_str, images: Optional[List] = None, valid_roles: Optional[List[str]] = None
):
    valid_roles = ["system", "user", "assistant", "function", "tool"]

    # openai chat api only supports below roles.
    # customer can add single # in front of role name for markdown highlight.
    # and we still support role name without # prefix for backward compatibility.
    separator = r"(?i)^\s*#?\s*(" + "|".join(valid_roles) + r")\s*:\s*\n"

    images = images or []
    hash2images = {str(x): x for x in images}

    chunks = re.split(separator, chat_str, flags=re.MULTILINE)
    chat_list = []

    for chunk in chunks:
        last_message = chat_list[-1] if len(chat_list) > 0 else None
        if last_message and "role" in last_message and "content" not in last_message:
            parsed_result = None
            if last_message["role"] == "assistant":
                parsed_result = _try_parse_tool_calls(chunk)
            if last_message["role"] == "tool":
                parsed_result = _try_parse_tool_message(chunk)
                if parsed_result is None:
                    raise ChatAPIFunctionRoleInvalidFormat(
                        message="tool message should include tool_call_id, content"
                    )
            if parsed_result is None:
                parsed_result = try_parse_name_and_content(chunk)
            if parsed_result is None:
                # "name" is required if the role is "function"
                if last_message["role"] == "function" or last_message["role"] == "tool":
                    raise ChatAPIFunctionRoleInvalidFormat(
                        message="Failed to parse function role prompt. Please make sure the prompt follows the "
                        "format: 'name:\\nfunction_name\\ncontent:\\nfunction_content'. "
                        "'name' is required if role is function, and it should be the name of the function "
                        "whose response is in the content. May contain a-z, A-Z, 0-9, and underscores, "
                        "with a maximum length of 64 characters. See more details in "
                        "https://platform.openai.com/docs/api-reference/chat/create#chat/create-name "
                        "or view sample 'How to use functions with chat models' in our gallery."
                    )
                # "name" is optional for other role types.
                else:
                    last_message["content"] = to_content_str_or_list(chunk, hash2images)
            else:
                if last_message["role"] == "assistant":
                    if isinstance(parsed_result, list):
                        last_message["tool_calls"] = parsed_result
                        last_message["content"] = None
                        continue
                if last_message["role"] == "tool":
                    assert len(parsed_result) == 2
                    last_message["tool_call_id"] = parsed_result[0]
                    last_message["content"] = to_content_str_or_list(
                        parsed_result[1], hash2images
                    )
                    continue
                last_message["name"] = parsed_result[0]
                last_message["content"] = to_content_str_or_list(
                    parsed_result[1], hash2images
                )
        else:
            if chunk.strip() == "":
                continue
            # Check if prompt follows chat api message format and has valid role.
            # References: https://platform.openai.com/docs/api-reference/chat/create.
            role = chunk.strip().lower()
            validate_role(role, valid_roles=valid_roles)
            new_message = {"role": role}
            chat_list.append(new_message)
    return chat_list


# TODO(2971352): revisit this tries=5 when there is any change to the 10min timeout logic
def handle_openai_error(tries: int = 5):
    """
    A decorator function that used to handle OpenAI error.
    OpenAI Error falls into retriable vs non-retriable ones.

    For retriable error, the decorator use below parameters to control its retry activity with exponential backoff:
     `tries` : max times for the function invocation, type is int
     'delay': base delay seconds for exponential delay, type is float
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            flag = CompletionNoneExceptionFlag()
            for i in range(tries + 1):
                try:
                    return func(*args, **kwargs)
                except (SystemErrorException, UserErrorException) as e:
                    # Throw inner wrapped exception directly
                    raise e
                except (APIStatusError, APIConnectionError) as e:
                    #  Handle retriable exception, please refer to
                    #  https://platform.openai.com/docs/guides/error-codes/api-errors
                    # print(
                    #     f"Exception occurs: {type(e).__name__}: {str(e)}",
                    #     file=sys.stderr,
                    # )
                    if (
                        isinstance(e, APIConnectionError)
                        and not isinstance(e, APITimeoutError)
                        and "connection aborted" not in str(e).lower()
                    ):
                        raise WrappedOpenAIError(e)
                    # Retry InternalServerError(>=500), RateLimitError(429), UnprocessableEntityError(422)
                    if isinstance(e, APIStatusError):
                        status_code = e.response.status_code
                        if status_code < 500 and status_code not in [429]:
                            raise WrappedOpenAIError(e)
                    if (
                        isinstance(e, RateLimitError)
                        and getattr(e, "type", None) == "insufficient_quota"
                    ):
                        # Exit retry if this is quota insufficient error
                        # print(
                        #     f"{type(e).__name__} with insufficient quota. Throw user error.",
                        #     file=sys.stderr,
                        # )
                        raise WrappedOpenAIError(e)
                    if i == tries:
                        # Exit retry if max retry reached
                        # print(
                        #     f"{type(e).__name__} reached max retry. Exit retry with user error.",
                        #     file=sys.stderr,
                        # )
                        raise ExceedMaxRetryTimes(e)

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
                    time.sleep(retry_after_seconds)
                except OpenAIError as e:
                    # For other non-retriable errors from OpenAIError,
                    # For example, AuthenticationError, APIConnectionError, BadRequestError, NotFoundError
                    # Mark UserError for all the non-retriable OpenAIError
                    # print(
                    #     f"Exception occurs: {type(e).__name__}: {str(e)}",
                    #     file=sys.stderr,
                    # )
                    raise WrappedOpenAIError(e)
                except CompletionNoneException as e:
                    if e.is_first_exception(flag=flag):
                        continue
                    else:
                        raise e
                except Exception as e:
                    # print(
                    #     f"Exception occurs: {type(e).__name__}: {str(e)}",
                    #     file=sys.stderr,
                    # )
                    error_message = (
                        f"OpenAI API hits exception: {type(e).__name__}: {str(e)}"
                    )
                    raise LLMError(message=error_message)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            flag = CompletionNoneExceptionFlag()
            for i in range(tries + 1):
                try:
                    return await func(*args, **kwargs)
                except (SystemErrorException, UserErrorException) as e:
                    # Throw inner wrapped exception directly
                    raise e
                except (APIStatusError, APIConnectionError) as e:
                    #  Handle retriable exception, please refer to
                    #  https://platform.openai.com/docs/guides/error-codes/api-errors
                    # print(
                    #     f"Exception occurs: {type(e).__name__}: {str(e)}",
                    #     file=sys.stderr,
                    # )
                    if (
                        isinstance(e, APIConnectionError)
                        and not isinstance(e, APITimeoutError)
                        and "connection aborted" not in str(e).lower()
                    ):
                        raise WrappedOpenAIError(e)
                    # Retry InternalServerError(>=500), RateLimitError(429)
                    if isinstance(e, APIStatusError):
                        status_code = e.response.status_code
                        if status_code < 500 and status_code not in [429]:
                            raise WrappedOpenAIError(e)
                    if (
                        isinstance(e, RateLimitError)
                        and getattr(e, "type", None) == "insufficient_quota"
                    ):
                        # Exit retry if this is quota insufficient error
                        # print(
                        #     f"{type(e).__name__} with insufficient quota. Throw user error.",
                        #     file=sys.stderr,
                        # )
                        raise WrappedOpenAIError(e)
                    if i == tries:
                        # Exit retry if max retry reached
                        # print(
                        #     f"{type(e).__name__} reached max retry. Exit retry with user error.",
                        #     file=sys.stderr,
                        # )
                        raise ExceedMaxRetryTimes(e)

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
                except OpenAIError as e:
                    # For other non-retriable errors from OpenAIError,
                    # For example, AuthenticationError, APIConnectionError, BadRequestError, NotFoundError
                    # Mark UserError for all the non-retriable OpenAIError
                    # print(
                    #     f"Exception occurs: {type(e).__name__}: {str(e)}",
                    #     file=sys.stderr,
                    # )
                    raise WrappedOpenAIError(e)
                except CompletionNoneException as e:
                    if e.is_first_exception(flag=flag):
                        continue
                    else:
                        raise e
                except Exception as e:
                    # print(
                    #     f"Exception occurs: {type(e).__name__}: {str(e)}",
                    #     file=sys.stderr,
                    # )
                    error_message = (
                        f"OpenAI API hits exception: {type(e).__name__}: {str(e)}"
                    )
                    raise LLMError(message=error_message)

        return wrapper if not inspect.iscoroutinefunction(func) else async_wrapper

    return decorator


def async_post_process_chat_api_response(completion, stream, functions):
    if stream:
        if functions is not None:
            error_message = (
                "Function calling has not been supported by stream mode yet."
            )
            raise FunctionCallNotSupportedInStreamMode(message=error_message)

        async def generator():
            async for chunk in completion:
                if chunk.choices:
                    yield chunk.choices[0].delta.content if hasattr(
                        chunk.choices[0].delta, "content"
                    ) and chunk.choices[0].delta.content is not None else ""

        return generator()
    else:
        # When calling function, function_call response will be returned as a field in message, so we need return
        # message directly. Otherwise, we only return content.
        if functions is not None:
            return completion.model_dump()["choices"][0]["message"]
        else:
            # chat api may return message with no content.
            return getattr(completion.choices[0].message, "content", "")


@tool
@handle_openai_error()
async def openai_tool_use(
    connection: OpenAIConnection | AzureOpenAIConnection,
    prompt: PromptTemplate,
    model: ModelEnum,
    temperature: float = 1,
    top_p: float = 1,
    n: int = 1,
    stream: Optional[bool] = False,
    stop: Optional[list] = None,  # type: ignore
    max_tokens: Optional[int] = None,  # type: ignore
    presence_penalty: float = 0,
    frequency_penalty: float = 0,
    logit_bias: dict = {},
    user: Optional[str] = "",
    function_call: Optional[object] = None,
    functions: Optional[list] = None,  # type: ignore
    response_format: object = dict(type="text"),
    tools: Optional[list[ChatCompletionToolParam]] = None,  # type: ignore
    tool_choice: Optional[ChatCompletionNamedToolChoiceParam | str] = None,  # type: ignore
    extra_headers: Optional[dict] = {},
    is_raw_output: Optional[bool] = False,
    **kwargs,
) -> [str, dict]:  # type: ignore
    chat_str = render_jinja_template(
        prompt, trim_blocks=True, keep_trailing_newline=True, **kwargs
    )
    messages = _parse_chat(chat_str)
    # TODO: remove below type conversion after client can pass json rather than string.
    stream = to_bool(stream)
    params = {
        "model": model,
        "messages": messages,
        "temperature": float(temperature),
        "top_p": float(top_p),
        "n": int(n),
        "stream": stream,
        "stop": stop if stop else None,
        "max_tokens": int(max_tokens)
        if max_tokens is not None and str(max_tokens).lower() != "inf"
        else None,
        "presence_penalty": float(presence_penalty),
        "frequency_penalty": float(frequency_penalty),
        "logit_bias": logit_bias,
        "user": user,
        "response_format": response_format,
    }

    if functions is not None:
        validate_functions(functions)
        params["functions"] = functions
        params["function_call"] = process_function_call(function_call)

    if tools is not None:
        functions = []
        for tool_desc in tools:
            tool_desc = cast(ChatCompletionToolParam, tool_desc)
            if "type" in tool_desc and "function" in tool_desc:
                functions.append(tool_desc["function"])
            else:
                raise ChatAPIInvalidFunctions(
                    message=f"tools parameter is invalid: {tools}"
                )
        validate_functions(functions)
        params["tools"] = tools

    if tool_choice is not None:
        if tool_choice in ["none", "auto"]:
            params["tool_choice"] = tool_choice
        else:
            try:
                tool_choice_dict = json.loads(tool_choice)
            except Exception:
                raise ChatAPIInvalidFunctions(
                    message=f"tool_choice parameter is invalid: {tool_choice}"
                )
            tool_choice_dict = cast(
                ChatCompletionNamedToolChoiceParam, tool_choice_dict
            )
            if "type" not in tool_choice_dict or "function" not in tool_choice_dict:
                raise ChatAPIInvalidFunctions(
                    message=f"tool_choice parameter is invalid: {tool_choice_dict}"
                )
            else:
                if "name" not in tool_choice_dict["function"]:
                    raise ChatAPIInvalidFunctions(
                        message=f"tool_choice parameter is invalid: {tool_choice_dict}"
                    )

            params["tool_choice"] = tool_choice_dict["function"]

    _connection_dict = normalize_connection_config(connection)
    _client = (
        OpenAIClient(**_connection_dict)
        if isinstance(connection, OpenAIConnection)
        else AzureOpenAIClient(**_connection_dict)
    )
    completion = await _client.chat.completions.create(
        **params, extra_headers=extra_headers
    )

    if completion is None:
        raise CompletionNoneException()

    return (
        async_post_process_chat_api_response(completion, stream, functions)
        if not is_raw_output
        else completion
    )
