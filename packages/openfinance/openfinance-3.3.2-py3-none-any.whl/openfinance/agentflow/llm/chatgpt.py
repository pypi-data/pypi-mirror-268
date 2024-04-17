import asyncio
from typing import (
    Any,
    Callable,
    Dict,
    Optional
)

from openai import AsyncOpenAI
from pydantic import BaseModel, root_validator

from openfinance.agentflow.llm.base import BaseLLM, Message


class ChatGPT(BaseLLM):
    name = "ChatGPT"
    api_key: str
    base_url: str

    @root_validator(pre=True)
    def initialize_variables(cls, values):
        values['client'] = AsyncOpenAI(
            base_url=values['base_url'],
            api_key=values['api_key'],
        )
        return values

    async def acall(
        self,
        content,
        mode: Optional[str] = None  # 可以是"json_object"
    ) -> Dict[str, str]:
        print(content)
        if isinstance(content, str):
            content = [
                {
                    "role": "user",
                    "content": content,
                }
            ]
        if mode:
            chat_completion = await self.client.chat.completions.create(
                messages=content,
                temperature=self.temperature,
                model=self.model,
                response_format={"type": mode}
            )
        else:
            chat_completion = await self.client.chat.completions.create(
                messages=content,
                temperature=self.temperature,
                model=self.model
            )
        content = chat_completion.choices[0].message.content
        #print(content)
        return Message("assistant", content)


if __name__ == "__main__":
    model = ChatGPT(
        model="gpt-3.5-turbo",
        api_key="",
        base_url=""
    )

    result = asyncio.run(model._acall("who are you"))
    print(result)
