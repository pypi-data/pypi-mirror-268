# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate

plan_prompt_template_v1 ="""
Question: {content}
```
{document}
```
Try you best to answer reasonable and helpfully in Chinese, think step by step.
"""

plan_prompt_template_v2 ="""
Goal: analyze factor by factor to answer concretly and explicately
Restriction: you already have enough information, only use them to answer
Question: {content}
Factors:
```
{document}
```
Begin to answer in Chinese!
"""

PROMPT = PromptTemplate(
    prompt=plan_prompt_template_v2, variables=["content", "document"])