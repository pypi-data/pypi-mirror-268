# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate


PREFIX = """Answer the following questions. You have access to the following functions:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should think which function to use and only choose one
Function: the function to choose, should be one of [{tool_names}]
Function Input: the input parameters to the function"""

SUFFIX = """
You can only think one step forward. Begin!

Question: {content}
Thought:"""


ROLE = """you are a senior stock analyst, pls infer data helpfully: 
{content}
"""

ROLE_PROMPT = PromptTemplate(
    prompt=ROLE, variables=["content"])