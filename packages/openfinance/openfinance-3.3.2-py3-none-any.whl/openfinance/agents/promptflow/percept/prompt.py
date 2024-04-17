# flake8: noqa
# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate

prompt_template_v0 = """
Role: You are a senior Stock Analyst
Goal: Analyze Input and infer helpfully for investing
Input:
{content}
you must respond in following format

Thought:  
- what entity is influenced mainly, entity must be in Chinese
- which level entity belong to, must one of [{types}]
- what financial indicator is influenced mainly, indicator must be in English
- what event is happenning to entity, event must be briefly in Chinese
- what sentiment is event, one of [Positive Negative Neural]
Result:
{{
    "consequence": [
        {{
            "entity": "",
            "event": "",        
            "level": "",
            "indicator": "",
            "sentiment": ""
        }}
    ]
}}

Let's begin! 
"""

prompt_template_online = """
Role: You are a senior Stock Analyst
Goal: 
Extract Company, Product, Concept, Sector, Industry Entity for Financial knowledge graph, 
Analyze helpfully for investing

Input: {content}

you must respond in following format

```
Thought:
- 提到了哪些具体实体？ 按类列出产品、板块、概念、行业、公司、地点、指数等实体, 名称尽量简洁
- 结合Input内容，关键实体是什么？ 必须来自于前面列出的具体实体
- 它的层级是什么，必须来自[{types}]
- 影响它的事件是什么，20字以内总结
- 推测哪一个运营指标会变化？ 如果无法推断，回答无
- 情绪如何？必须来自[Positive, Negative, Neural]
Result:
{{
    "产品": [],
    "板块": [],
    "概念": [],
    "行业": [],
    "公司": [],       
    "main_entity": "",
    "event": "",
    "level": "",
    "indicator": "",
    "sentiment": ""
}}
```
Let's begin! 
"""


OPINION_PROMPT = PromptTemplate(
    prompt=prompt_template_online, variables=["content", "types"])

match_prompt_template = """
Task: 
you must find the most related indicator to {content} from [{indicators}]
you can only reply the indicator name, otherwise None
Answer:
"""

MATCH_PROMPT = PromptTemplate(
    prompt=match_prompt_template, variables=["content", "indicators"])