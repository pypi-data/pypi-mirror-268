# flake8: noqa
# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate

prompt_template_cot = """
Goal: extract market entity of Company, Product, Concept, Sector, Industry helpful for Financial knowledge graph
Content:
```
{content}
```
Answer in format:
Result:
{{
    "Product": [],
    "Sector": [],
    "Concept": [],
    "Industry": [],
    "Company": []
}}

Let's begin! 
"""

OPINION_PROMPT = PromptTemplate(
    prompt=prompt_template_cot, variables=["content"])