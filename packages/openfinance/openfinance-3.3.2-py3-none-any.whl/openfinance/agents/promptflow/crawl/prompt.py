# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate

plan_prompt_template_v2 = """

urls : 
```
{content}
```
headers: 
```
{headers}
```
Based on the urls and headers, write a python function to get response data. the get or post method should have params and headers 
"""

PLAN_PROMPT = PromptTemplate(
    prompt=plan_prompt_template_v2, variables=["content", "headers"])