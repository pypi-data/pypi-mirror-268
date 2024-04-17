# flake8: noqa
PREFIX = """Answer the following questions as best you can"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should think which tool you should use
Action: the action to take , must be exactly {tool_names}
Action Input: the input to the Action, should be one of {strategy_names}
"""

SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""