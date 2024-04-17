# flake8: noqa
from openfinance.agentflow.prompt.base import PromptTemplate


PREFIX = """Answer the following questions. """

FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should think which function to use and only choose one
Function: the function to choose
Function Input: the input parameters to the function"""

SUFFIX = """
You should find tool for each question. Begin!
"""