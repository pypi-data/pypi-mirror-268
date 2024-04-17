# flake8: noqa
PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should think which tool you should use
Action: the action to take, should be one of [{tool_names}]
Action Input: the country if mentioned in Question, if not, Use China by default
"""

SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""