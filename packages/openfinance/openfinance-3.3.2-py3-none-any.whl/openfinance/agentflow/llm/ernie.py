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

class ERNIE(BaseLLM):
    name = "ERNIE"
    api_key: str
    sec_key: str
    base_url: str

    async def acall(
        self,
        content,
        mode: Optional[str] = None  # 可以是"json_object"
    ) -> Dict[str, str]:
        print(content)
        def get_access_token():
            url = "https://aip.baidubce.com/oauth/2.0/token"
            params = {"grant_type": "client_credentials", "client_id": self.api_key, "client_secret": self.sec_key}
            return str(requests.post(url, params=params).json().get("access_token"))

        payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "temperature": self.temperature,
            "top_p": self.top_p            
        })
        headers = {
            'Content-Type': 'application/json'
        }
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
                data = payload,
                headers= {'Content-Type': 'application/json'}
            ) as response:
                resp = await response.text()

        print(resp)
        resp = json.loads(resp)
        content = resp["data"][0]["message"]["content"]
        return Message("assistant", content)

if __name__ == "__main__":
    model = ERNIE(
        model="gpt4",
        api_key="UipquWMBwcPYwbgMNZsaGc0u",
        sec_key="wU3jeD93VurD8hWlh81GbGytGTOxMDHG",
        base_url="https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token="
    )

    result = asyncio.run(model._acall("what is your name"))
    print(result)