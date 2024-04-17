# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate

plan_prompt_template ="""
you are a senior data analyst, pls infer helpfully:
{content}
"""

plan_prompt_template_v1 ="""
Role: you are a senior stock analyst
Goal: Analyze indicators situation and trend over time carefully to offer helpfully information
CONTENT: 
```
{content}
```
you must respond in following format

***
Thought:
- what indicators or information to analyze 
- what result and trends do they show numerically 

Result:
- Clarify your Thought explicitly in details based on CONTENT, think step by step
***
"""

plan_prompt_template_v2 ="""
Role: you are a senior stock analyst
Goal: Analyze indicators situation and trend over time carefully to offer helpfully information
CONTENT: 
```
{content}
```

you must respond in following format
***
Thought:
- 有哪些指标和信息需要分析？

Result:
- 结合数据分析表现怎么样？未来趋势如何？
- 请结合 CONTENT 和 Thought, 一步一步地，明确仔细地，输出分析过程
***
"""


PROMPT = PromptTemplate(
    prompt=plan_prompt_template_v2, variables=["content"])