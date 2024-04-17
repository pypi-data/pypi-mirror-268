# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate
from openfinance.agents.role.prompts.base import build_from_name

Ray_Dalio_PROMPT = PromptTemplate(
    prompt=build_from_name("Ray Dalio") + "\n{content}\m", variables=["content"])