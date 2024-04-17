# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate
from openfinance.agents.role.prompts.base import build_from_name

quant_PROMPT = PromptTemplate(
    prompt=build_from_name("Quant Investor") + "\n{content}\m", variables=["content"])