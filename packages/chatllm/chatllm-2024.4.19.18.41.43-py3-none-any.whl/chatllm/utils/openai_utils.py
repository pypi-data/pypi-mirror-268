#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : ppu_utils
# @Time         : 2024/1/8 16:46
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 按次计费
import time

import openai
from openai import OpenAI

from meutils.pipe import *
from chatllm.schemas.openai_types import completion_keys
from chatllm.schemas.openai_api_protocol import ChatCompletionRequest

from openai.types.chat import ChatCompletion, ChatCompletionChunk


def to_openai_completion_params(
    request: Union[dict, ChatCompletionRequest],
    redirect_model: Optional[str] = None
) -> dict:
    data = copy.deepcopy(request)
    if isinstance(request, ChatCompletionRequest):
        data = request.model_dump()

    extra_body = {}
    for key in list(data):
        if key not in completion_keys:
            extra_body.setdefault(key, data.pop(key))

    data['extra_body'] = extra_body  # 拓展字段
    data['model'] = redirect_model or data['model']

    return data


# @background_task
def per_create(api_key: Optional[str] = None, base_url: Optional[str] = None, model: str = 'per'):
    openai = OpenAI(
        api_key=api_key,
        base_url=base_url or "https://api.chatllm.vip/v1",
        http_client=httpx.Client(follow_redirects=True)
    )
    return openai.chat.completions.create(model=model, messages=[{"role": "user", "content": "hi"}])


def openai_response2sse(response, redirect_model: Optional[str] = None, n: float = 1.2):
    """

    :param response:
    :param redirect_model: request.model
    :param n:
    :return:
    """
    from sse_starlette import EventSourceResponse

    # logger.debug(type(response))

    if isinstance(response, ChatCompletion):
        response.model = redirect_model or response.model

        response.usage.prompt_tokens = int(response.usage.prompt_tokens * n)
        completion_tokens = response.usage.completion_tokens or len(response.choices[0].message.content)
        response.usage.completion_tokens = int(completion_tokens * n)
        response.usage.total_tokens = response.usage.prompt_tokens + response.usage.completion_tokens

        return response

    def do_chunk(chunk):
        chunk: ChatCompletionChunk
        chunk.model = redirect_model or chunk.model

        # logger.debug(chunk.choices)

        if chunk.choices and chunk.choices[0].delta.content:  # 跳过首行空值
            if chunk.choices[0].finish_reason == "stop":
                chunk.choices[0].delta.content = ""  # "delta":{} "delta":{"content":""}
                yield chunk.model_dump_json()
                # yield "[DONE]"  # 兼容标准格式
                return
            else:
                yield chunk.model_dump_json()


    if inspect.isasyncgen(response) or isinstance(response, openai.AsyncStream):
        async def gen():
            async for chunk in response:
                for chunk in do_chunk(chunk):
                    yield chunk
            yield "[DONE]"  # 兼容标准格式

    else:
        def gen():
            for chunk in response:
                for chunk in do_chunk(chunk):
                    yield chunk
            yield "[DONE]"  # 兼容标准格式

    return EventSourceResponse(gen(), ping=10000)  # sse_response


if __name__ == '__main__':
    print(per_create())
