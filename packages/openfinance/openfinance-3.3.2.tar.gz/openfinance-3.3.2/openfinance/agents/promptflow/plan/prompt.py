# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate

plan_prompt_template ="""
Only use you stock analysis framework to analyze as accurately as possible.

Answer in this format:
```
Task: input task to solve
Thought: You only need to list all the factors to solve the task comprehensively and thoroughly. You should not list contents for the factors.
Subtasks: You only need to list all indicators to evaluate each factor and You should not list contents for the indicator. you must be in valid JSON format.
```
Let's begin! the input task is {content}.
"""

plan_prompt_template_v2 = """
you are a stock analysis, you need to find out possible factors about Task.

Task : {content}

Answer in this format:
```
Task: input task to solve in English
Thought: list associated factor names that you need to solve the task thoroughly.
Subtasks: list all indicator names to evaluate each factor and you must be in valid JSON format.
```
Let's begin!
"""

PLAN_PROMPT = PromptTemplate(
    prompt=plan_prompt_template_v2, variables=["content"])