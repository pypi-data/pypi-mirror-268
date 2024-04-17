import re
from typing import Union, Dict

from openfinance.agentflow.base_parser import BaseParser
from openfinance.agentflow.tool.base import Action

FINAL_ANSWER_ACTION = "Final Answer"
class SingleActionParser(BaseParser):
    def parse(
        self, 
        text: str
    ) -> str:
        print("TEXT\n", text)
        # \s matches against tab/newline/whitespace
        regex = (
            r"Action\s*\d*\s*:[\s]*(.*?)[\s]*Action\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
        )
        
        action_match = re.search(regex, text, re.DOTALL)
        if action_match:
            action = action_match.group(1).strip()
            action_input = action_match.group(2)
            tool_input = action_input.split("Observation")[0].strip() # delete obs
            tool_input = tool_input.replace('"', "")

            return Action(name=action, action_input=tool_input)
        elif FINAL_ANSWER_ACTION in text:
            return Action(name="Final", action_input=text.split(FINAL_ANSWER_ACTION)[-1].strip())
        
        raise OutputParserException(f"Could not parse LLM output: `{text}`")
