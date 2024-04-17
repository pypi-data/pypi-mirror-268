# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate
from openfinance.agents.role.prompts.base import build_from_name

ELON_MUSK_PROMPT = PromptTemplate(
    prompt=build_from_name("Elon Musk") + "\n{content}\m", variables=["content"])