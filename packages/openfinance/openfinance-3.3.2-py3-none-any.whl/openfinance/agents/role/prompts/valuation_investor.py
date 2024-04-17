# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate
from openfinance.agents.role.prompts.base import build_from_name

valuation_PROMPT = PromptTemplate(
    prompt=build_from_name("Value investor") + "\n{content}\m", variables=["content"])