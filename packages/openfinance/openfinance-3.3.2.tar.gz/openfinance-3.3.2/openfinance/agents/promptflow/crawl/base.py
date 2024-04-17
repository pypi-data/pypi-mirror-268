import asyncio
from typing import (
    Any,
    Callable,
    Dict,
    Union,
    List
)
from openfinance.agentflow.flow.base import BaseFlow
from openfinance.agentflow.llm.chatgpt import ChatGPT
from openfinance.agentflow.llm.base import BaseLLM
from openfinance.agentflow.base_parser import BaseParser
from openfinance.agentflow.prompt.base import PromptTemplate

from openfinance.agents.promptflow.crawl.prompt import PLAN_PROMPT

class CrawFlow(BaseFlow):
    name = "CrawFlow"
    inputs: List[str] = ["content", "headers"]
    prompt: PromptTemplate = PLAN_PROMPT

    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_llm(
        cls,
        llm: BaseLLM,
        **kwargs: Any        
    ) -> 'CrawFlow':
        return cls(llm=llm, **kwargs)

    async def acall(
        self,
        content: str,
        **kwargs: Any        
    ) -> Dict[str, str]:
        inputs = {"content": content}
        for i in self.inputs:
            if i != "content":
                inputs[i] = kwargs[i]
        resp = await self.llm.acall(self.prompt.prepare(inputs))
        # print(resp)
        return {self.output: resp.content}

if __name__ == "__main__":
    from openfinance.config import Config
    from openfinance.agentflow.llm.manager import ModelManager
    llm = ModelManager(Config()).get_model("aliyungpt")
    flow = CrawFlow.from_llm(llm)
    result = asyncio.run(flow._acall(
        content="https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery11230885902819389405_1703572892543&sortColumns=PE_TTM&sortTypes=1&pageSize=50&pageNumber=1&reportName=RPT_VALUEINDUSTRY_DET&columns=ALL&quoteColumns=&source=WEB&client=WEB&filter=(TRADE_DATE%3D%272023-12-25%27)", 
        headers="""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
                Accept-Encoding: gzip, deflate, br
                Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
                Cache-Control: max-age=0
                Connection: keep-alive
                Cookie: qgqp_b_id=164c76d2ed75802b814949a81b3b6191; websitepoptg_show_time=1703145371497; HAList=ty-1-601360-%u4E09%u516D%u96F6%2Cty-0-300949-%u5965%u96C5%u80A1%u4EFD%2Cty-106-BLK-%u8D1D%u83B1%u5FB7%2Cty-105-AAPL-%u82F9%u679C%2Cty-106-PG-%u5B9D%u6D01%2Cty-100-DJIA-%u9053%u743C%u65AF%2Cty-106-MS-%u6469%u6839%u58EB%u4E39%u5229%2Cty-106-BRK_A-%u4F2F%u514B%u5E0C%u5C14%u54C8%u6492%u97E6-A%2Cty-106-GME-%u6E38%u620F%u9A7F%u7AD9; st_si=93775926910693; st_asi=delete; st_pvi=54709136970065; st_sp=2023-12-19%2015%3A13%3A28; st_inirUrl=http%3A%2F%2Fquote.eastmoney.com%2Fcenter%2Fgridlist.html; st_sn=2; st_psi=20231226144155291-113300303065-2004315192; JSESSIONID=931248717DA1D240295441B47CD58FA4
                Host: datacenter-web.eastmoney.com
                Sec-Fetch-Dest: document
                Sec-Fetch-Mode: navigate
                Sec-Fetch-Site: none
                Sec-Fetch-User: ?1
                Upgrade-Insecure-Requests: 1
                User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
                sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"
                sec-ch-ua-mobile: ?0
                sec-ch-ua-platform: "macOS" """
        ))
    print(result["output"])