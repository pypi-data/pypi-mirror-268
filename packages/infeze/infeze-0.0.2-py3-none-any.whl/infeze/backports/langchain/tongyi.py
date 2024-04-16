# flake8: noqa
# isort: skip_file
# fmt: off

from __future__ import annotations

from langchain.callbacks.manager import (CallbackManagerForLLMRun, AsyncCallbackManagerForLLMRun)
from langchain.llms.base import create_base_retry_decorator
from langchain.llms.base import BaseLLM
from langchain.chat_models.base import BaseChatModel
from http import HTTPStatus
import asyncio

import logging

from typing import Optional, Union, Callable, Any, AsyncGenerator

logger = logging.getLogger(__name__)


def completion_with_retry(
    llm_model: BaseLLM | BaseChatModel,
    run_manager: Optional[CallbackManagerForLLMRun] = None,
    **kwargs: Any
) -> Any:
    """Use tenacity to retry the completion call."""
    retry_decorator = _create_retry_decorator(llm_model, run_manager=run_manager)

    @retry_decorator
    def _completion_with_retry(**_kwargs: Any) -> Any:
        # print("#" * 60)
        # print("kwargs: ", _kwargs)

        resp = llm_model.client.call(**_kwargs)
        return resp

    return _completion_with_retry(**kwargs)


# 注意 该函数返回的类型为 <async_generator>
# 仅用在 streaming 调用的 async for 循环中
async def acompletion_with_retry(
    llm_model: BaseLLM | BaseChatModel,
    run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
    **kwargs: Any
) -> AsyncGenerator:
    """Use tenacity to retry the completion call."""
    retry_decorator = _create_retry_decorator(llm_model, run_manager=run_manager)

    @retry_decorator
    async def _completion_with_retry(**_kwargs: Any) -> AsyncGenerator:
        print("#" * 60)
        print("kwargs: ", _kwargs)
        resp = llm_model.client.call(**kwargs)
        print("<<- async resp: ", resp)
        return async_generator(resp)

    return await _completion_with_retry(**kwargs)


async def async_generator(normal_generator):
    for v in normal_generator:
        if v.status_code == HTTPStatus.OK:
            await asyncio.sleep(0)
            yield v
        else:
            print("async_generator HTTP-Err: ", v)
            raise SystemError("http response Error: ", v.status_code)


def _create_retry_decorator(
    llm_model: BaseLLM | BaseChatModel,
    run_manager: Optional[
        Union[AsyncCallbackManagerForLLMRun, CallbackManagerForLLMRun]
    ] = None,
) -> Callable[[Any], Any]:
    import dashscope

    errors = [
        # TODO: add more errors
        dashscope.common.error.RequestFailure,
        dashscope.common.error.InvalidInput,
        dashscope.common.error.ModelRequired,
    ]

    return create_base_retry_decorator(
        error_types=errors, max_retries=llm_model.max_retries, run_manager=run_manager
    )


def response_text_format(stream_resp, cursor):
    text = stream_resp["output"]["choices"][0]["message"]["content"]
    text = text[cursor:]
    cursor += len(text)
    stream_resp["output"]["choices"][0]["message"]["content"] = text
    return stream_resp, cursor


def response_handler(response):
    if response.status_code == HTTPStatus.BAD_REQUEST and "contain inappropriate content" in response.message:
        response.status_code = HTTPStatus.OK
        response.output = {
            "choices": [{"finish_reason": "stop", "message": {
                "role": "assistant", "content": "Input data may contain inappropriate content.🐶"}}]
        }
        response.usage = {"output_tokens": 0, "input_tokens": 0}
    elif response.status_code != HTTPStatus.OK:
        raise ValueError(f"http request failed, code: {response.status_code}")
    return response


from typing import Any, Dict, List, Optional, Iterator, AsyncIterator, Set
import logging

from langchain.llms.base import BaseLLM
from langchain.pydantic_v1 import Field, root_validator
from langchain.schema import Generation, LLMResult
from langchain.utils import get_from_dict_or_env
from langchain.schema.output import GenerationChunk
from langchain.callbacks.manager import (CallbackManagerForLLMRun, AsyncCallbackManagerForLLMRun)
from http import HTTPStatus

logger = logging.getLogger(__name__)


def update_token_usage(
    keys: Set[str], response: Dict[str, Any], token_usage: Dict[str, Any]
) -> None:
    """Update token usage."""
    _keys_to_use = keys.intersection(response["usage"])
    for _key in _keys_to_use:
        if _key not in token_usage:
            token_usage[_key] = response["usage"][_key]
        else:
            token_usage[_key] += response["usage"][_key]


def _stream_response_to_generation_chunk(
    stream_response: Dict[str, Any],
) -> GenerationChunk:
    """Convert a stream response to a generation chunk."""
    return GenerationChunk(
        text=stream_response["output"]["choices"][0]["message"]["content"],
        generation_info=dict(
            finish_reason=stream_response["output"]["choices"][0].get("finish_reason", None),
        ),
    )


class BaseDashScope(BaseLLM):
    """Base DashScope large language model class."""
    @property
    def lc_secrets(self) -> Dict[str, str]:
        return {"dashscope_api_key": "DASHSCOPE_API_KEY"}

    @property
    def lc_serializable(self) -> bool:
        return True

    client: Any = None

    model_name: str = Field(default="qwen-turbo", alias="model")
    """Model name to use."""
    temperature: float = 0.7
    """What sampling temperature to use."""
    result_format: str = "message"
    """openai-compatible messages format"""
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Holds any model parameters valid for `create` call not explicitly specified."""
    top_p: float = 0.8
    """Total probability mass of tokens to consider at each step."""
    n: int = 1
    """How many completions to generate for each prompt."""
    dashscope_api_key: Optional[str] = None
    """Dashscope api key provide by alicloud."""
    streaming: bool = False
    """Whether to stream the results or not."""
    max_retries: int = 3
    """Maximum number of retries to make when generating."""
    prefix_messages: List = Field(default_factory=list)
    """Series of messages for Chat input."""

    def __new__(cls, **data: Any) -> BaseDashScope:
        return super().__new__(cls)

    class Config:
        """Configuration for this pydantic object."""

        allow_population_by_field_name = True

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        get_from_dict_or_env(values, "dashscope_api_key", "DASHSCOPE_API_KEY")
        try:
            import dashscope
        except ImportError:
            raise ImportError(
                "Could not import dashscope python package. "
                "Please install it with `pip install dashscope`."
            )
        try:
            values["client"] = dashscope.Generation
        except AttributeError:
            raise ValueError(
                "`dashscope` has no `Generation` attribute, this is likely "
                "due to an old version of the dashscope package. Try upgrading it "
                "with `pip install --upgrade dashscope`."
            )

        return values

    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the default parameters for calling OpenAI API."""
        normal_params = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "n": self.n,
            "result_format": self.result_format,
        }

        return {**normal_params, **self.model_kwargs}

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "qwen"
        
    def _stream(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[GenerationChunk]:
        params: Dict[str, Any] = {
            **self._default_params,
            **kwargs,
            "model": self.model_name,
            "stream": True,
        }

        text_cursor = 0
        for stream_resp in completion_with_retry(self, prompt=prompt, run_manager=run_manager, **params):
            if stream_resp.status_code == HTTPStatus.OK:
                stream_resp, text_cursor = response_text_format(stream_resp, text_cursor)
                chunk = _stream_response_to_generation_chunk(stream_resp)
                yield chunk
                if run_manager:
                    run_manager.on_llm_new_token(
                        chunk.text,
                        chunk=chunk,
                        verbose=self.verbose,
                    )
            else:
                logger.warning("http request failed: code: %s", stream_resp.status_code)

    async def _astream(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> AsyncIterator[GenerationChunk]:
        params: Dict[str, Any] = {
            # **{"model": self.model_name},
            **self._default_params,
            **kwargs,
            "model": self.model_name,
            "stream": True
        }

        text_cursor = 0

        try:
            async for stream_resp in await acompletion_with_retry(
                self, prompt=prompt, run_manager=run_manager, **params
            ):
                if stream_resp.status_code == HTTPStatus.OK:
                    # print("stream_resp: ", stream_resp)
                    stream_resp, text_cursor = response_text_format(stream_resp, text_cursor)
                    chunk = _stream_response_to_generation_chunk(stream_resp)
                    yield chunk
                    if run_manager:
                        await run_manager.on_llm_new_token(
                            chunk.text,
                            chunk=chunk,
                            verbose=self.verbose,
                        )
                else:
                    logger.warning("http request failed: code: %s", stream_resp.status_code)
        except Exception as e:
            print("_astream exception: ", e)
            # raise e
            return
        finally:
            print("_astream: over111")

    def _generate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> LLMResult:
        choices = []
        token_usage: Dict[str, int] = {}
        _keys = {"input_tokens", "output_tokens"}
        params: Dict[str, Any] = {
            **{"model": self.model_name},
            **self._default_params,
            **kwargs,
        }
        if self.streaming:
            if len(prompts) > 1:
                raise ValueError("Cannot stream results with multiple prompts.")
            generation: Optional[GenerationChunk] = None
            for chunk in self._stream(prompts[0], stop, run_manager, **params):
                if generation is None:
                    generation = chunk
                else:
                    generation += chunk
            assert generation is not None
            choices.append(
                {
                    "text": generation.text,
                    "finish_reason": generation.generation_info.get("finish_reason")
                }
            )
        else:
            response = completion_with_retry(
                self,
                prompt=prompts[0],
                run_manager=run_manager,
                **params,
            )

            response = response_handler(response)

            for v in response["output"]["choices"]:
                choices.append({
                    "text": v["message"]["content"],
                    "finish_reason": v["finish_reason"]
                })
            update_token_usage(_keys, response, token_usage)
        return self.create_llm_result(choices, prompts, token_usage)
    
    async def _agenerate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> LLMResult:
        """Run the LLM on the given prompts."""
        choices = []
        token_usage: Dict[str, int] = {}
        _keys = {"input_tokens", "output_tokens"}
        params: Dict[str, Any] = {
            **{"model": self.model_name},
            **self._default_params,
            **kwargs,
        }
        if self.streaming:
            if len(prompts) > 1:
                raise ValueError("Cannot stream results with multiple prompts.")
            generation: Optional[GenerationChunk] = None
            async for chunk in self._astream(prompts[0], stop, run_manager, **params):
                if generation is None:
                    generation = chunk
                else:
                    generation += chunk
            assert generation is not None
            choices.append(
                {
                    "text": generation.text,
                    "finish_reason": generation.generation_info.get("finish_reason")
                }
            )
        else:
            # _agenerate 已经是 async 函数了，这里走同步逻辑
            response = completion_with_retry(
                self,
                prompt=prompts[0],
                run_manager=run_manager,
                **params,
            )

            response = response_handler(response)

            for v in response["output"]["choices"]:
                choices.append({
                    "text": v["message"]["content"],
                    "finish_reason": v["finish_reason"]
                })
            update_token_usage(_keys, response, token_usage)
        result = self.create_llm_result(choices, prompts, token_usage)
        return result

    def create_llm_result(
        self, choices: Any, prompts: List[str], token_usage: Dict[str, int]
    ) -> LLMResult:
        """Create the LLMResult from the choices and prompts."""
        generations = []
        for i, _ in enumerate(prompts):
            sub_choices = choices[i * self.n: (i + 1) * self.n]
            # print(choices)
            # print(sub_choices)
            
            generations.append(
                [
                    Generation(
                        text=choice["text"],
                        generation_info=dict(
                            finish_reason=choice.get("finish_reason"),
                        ),
                    )
                    for choice in sub_choices
                ]
            )
        llm_output = {"token_usage": token_usage, "model_name": self.model_name}
        return LLMResult(generations=generations, llm_output=llm_output)


class Tongyi(BaseDashScope):
    def __new__(cls, **data: Any) -> Tongyi:
        return super().__new__(cls, **data)


# chat -----------------------------------------------------------------------
from http import HTTPStatus
import logging

from langchain.chat_models.base import BaseChatModel
from langchain.pydantic_v1 import Field, root_validator
from langchain.callbacks.manager import (
    CallbackManagerForLLMRun, AsyncCallbackManagerForLLMRun
)
from langchain.utils import get_from_dict_or_env
from langchain.schema import ChatResult, ChatGeneration
from langchain.schema.output import ChatGenerationChunk
from langchain.schema.messages import (
    BaseMessage,
    AIMessageChunk,
    ChatMessageChunk,
    SystemMessageChunk,
    HumanMessageChunk,
)
from langchain.adapters.openai import (convert_dict_to_message, convert_message_to_dict)

import asyncio
from functools import partial

from typing import (Dict, Any, Optional, List,
                    Iterator, Tuple, Mapping, AsyncIterator)

logger = logging.getLogger(__name__)


def _stream_response_to_chat_generation_chunk(
    stream_response: Dict[str, Any],
) -> ChatGenerationChunk:
    """Convert a stream response to a chat generation chunk."""
    msg = stream_response["output"]["choices"][0]["message"]
    role = msg["role"]
    text = msg["content"]

    msg_chunk = None

    if role == "user":
        msg_chunk = HumanMessageChunk(content=text)
    elif role == "assistant":
        msg_chunk = AIMessageChunk(content=text)
    elif role == "system":
        msg_chunk = SystemMessageChunk(content=text)
    else:
        msg_chunk = ChatMessageChunk(content=text, role=role)

    return ChatGenerationChunk(
        message=msg_chunk,
        generation_info=dict(
            finish_reason=stream_response["output"]["choices"][0].get("finish_reason", None),
        ),
    )


class ChatTongyi(BaseChatModel):
    @property
    def lc_secrets(self) -> Dict[str, str]:
        return {"dashscope_api_key": "DASHSCOPE_API_KEY"}

    @property
    def lc_serializable(self) -> bool:
        return True

    client: Any = None
    model_name: str = Field(default="qwen-turbo", alias="model")
    """Model name to use."""
    temperature: float = 0.7
    """What sampling temperature to use."""
    result_format: str = "message"
    """openai-compatible messages format"""
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Holds any model parameters valid for `create` call not explicitly specified."""
    top_p: float = 0.8
    """Total probability mass of tokens to consider at each step."""
    n: int = 1
    """How many completions to generate for each prompt."""
    dashscope_api_key: Optional[str] = None
    """Dashscope api key provide by alicloud."""
    streaming: bool = False
    """Whether to stream the results or not."""
    max_retries: int = 3
    """Maximum number of retries to make when generating."""
    prefix_messages: List = Field(default_factory=list)
    """Series of messages for Chat input."""

    class Config:
        """Configuration for this pydantic object."""

        allow_population_by_field_name = True

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        get_from_dict_or_env(values, "dashscope_api_key", "DASHSCOPE_API_KEY")
        try:
            import dashscope
        except ImportError:
            raise ImportError(
                "Could not import dashscope python package. "
                "Please install it with `pip install dashscope`."
            )
        try:
            values["client"] = dashscope.Generation
        except AttributeError:
            raise ValueError(
                "`dashscope` has no `Generation` attribute, this is likely "
                "due to an old version of the dashscope package. Try upgrading it "
                "with `pip install --upgrade dashscope`."
            )

        return values

    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the default parameters for calling OpenAI API."""
        normal_params = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "n": self.n,
            "result_format": self.result_format,
        }

        return {**normal_params, **self.model_kwargs}

    def _combine_llm_outputs(self, llm_outputs: List[Optional[dict]]) -> dict:
        overall_token_usage: dict = {}
        for output in llm_outputs:
            if output is None:
                # Happens in streaming
                continue
            token_usage = output.get("token_usage", {})
            for k, v in token_usage.items():
                if k in overall_token_usage:
                    overall_token_usage[k] += v
                else:
                    overall_token_usage[k] = v
        return {"token_usage": overall_token_usage, "model_name": self.model_name}

    def _stream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[ChatGenerationChunk]:
        message_dicts = self._create_message_dicts(messages, stop)
        params: Dict[str, Any] = {
            **self._default_params,
            **kwargs,
            "stream": True,
            "model": self.model_name,
        }
        text_cursor = 0
        for stream_resp in completion_with_retry(self, messages=message_dicts, run_manager=run_manager, **params):
            if stream_resp.status_code == HTTPStatus.OK:
                if stream_resp["output"]["choices"] and len(stream_resp["output"]["choices"]) == 0:
                    continue

                stream_resp, text_cursor = response_text_format(stream_resp, text_cursor)
                chat_chunk = _stream_response_to_chat_generation_chunk(stream_resp)
                yield chat_chunk
                if run_manager:
                    run_manager.on_llm_new_token(chat_chunk.message.content, chunk=chat_chunk.message)
            else:
                logger.warning("http request failed: code: %s", stream_resp.status_code)

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Top Level call"""
        # print("_generate... message: ", messages)
        params: Dict[str, Any] = {
            **self._default_params,
            **kwargs,
            "model": self.model_name,
        }

        if self.streaming:
            generation: Optional[ChatGenerationChunk] = None
            for chunk in self._stream(messages, stop, run_manager, **params):
                if generation is None:
                    generation = chunk
                else:
                    generation += chunk
            assert generation is not None
            return ChatResult(generations=[generation])
        else:
            message_dicts = self._create_message_dicts(messages, stop)

            response = completion_with_retry(
                self, messages=message_dicts, run_manager=run_manager, **params
            )

            response = response_handler(response)
            return self._create_chat_result(response)

    def _astream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> AsyncIterator[ChatGenerationChunk]:
        # TODO: Implement later
        raise NotImplementedError()

    async def _agenerate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Top Level call"""
        # TODO: Implement later
        return await asyncio.get_running_loop().run_in_executor(
            None,
            partial(self._generate, **kwargs),
            messages,
            stop,
            run_manager
        )

    def _create_message_dicts(
        self, messages: List[BaseMessage], stop: Optional[List[str]]
    ) -> Tuple[List[Dict[str, Any]]]:
        message_dicts = [convert_message_to_dict(m) for m in messages]
        return message_dicts

    def _create_chat_result(self, response: Mapping[str, Any]) -> ChatResult:
        generations = []
        llm_output = {}
        if response.status_code == HTTPStatus.OK:
            for res in response["output"]["choices"]:
                message = convert_dict_to_message(res["message"])
                gen = ChatGeneration(
                    message=message,
                    generation_info=dict(finish_reason=res.get("finish_reason")),
                )
                generations.append(gen)
            token_usage = response.get("usage", {})
            llm_output = {"token_usage": token_usage, "model_name": self.model_name}
        else:
            # TODO: error handling
            failed_msg = {"role": "assistant", "content": "Sorry, I don't know how to answer that."}
            message = convert_dict_to_message(failed_msg)
            gen = ChatGeneration(
                message=message,
                generation_info=dict({"finish_reason": "stop"}),
            )
            generations.append(gen)
            # logger.error("resp status err: ", response.status_code)
            llm_output = {"token_usage": {"input_tokens": 0, "output_tokens": 0}, "model_name": self.model_name}
        return ChatResult(generations=generations, llm_output=llm_output)

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Get the identifying parameters."""
        return {**{"model_name": self.model_name}, **self._default_params}

    def _get_invocation_params(
        self, stop: Optional[List[str]] = None, **kwargs: Any
    ) -> Dict[str, Any]:
        """Get the parameters used to invoke the model."""
        return {
            "model": self.model_name,
            **super()._get_invocation_params(stop=stop),
            **self._default_params,
            **kwargs,
        }

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "qwen-chat"
