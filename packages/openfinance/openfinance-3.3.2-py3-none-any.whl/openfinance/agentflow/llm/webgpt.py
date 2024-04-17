import asyncio
import aiohttp
import json

from typing import (
    Any,
    Callable,
    Dict,
    Optional
)
from pydantic import BaseModel, root_validator

from openfinance.agentflow.llm.base import BaseLLM, Message

class WebGPT(BaseLLM):
    name = "WebGPT"
    api_key: str
    base_url: str

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
        async with aiohttp.ClientSession() as session:
            async with session.post(
                self.base_url,
                data = json.dumps(content),
                headers= {
                    "access-user": self.api_key,
                    'Content-Type': 'application/json',
                }
            ) as response:
                resp = await response.text()
        #print(resp)
        resp = json.loads(resp)
        content = resp["data"][0]["message"]["content"]
        return Message("assistant", content)

if __name__ == "__main__":
    model = WebGPT(
        model="gpt4",
        api_key="",
        base_url=""
    )

    result = asyncio.run(model._acall("what is your name"))
    print(result)
