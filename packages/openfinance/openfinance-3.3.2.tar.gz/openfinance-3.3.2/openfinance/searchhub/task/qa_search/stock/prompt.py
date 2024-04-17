# flake8: noqa
PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should think which tool you should use
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the Action must be the company name mentioned in Question
"""

SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""