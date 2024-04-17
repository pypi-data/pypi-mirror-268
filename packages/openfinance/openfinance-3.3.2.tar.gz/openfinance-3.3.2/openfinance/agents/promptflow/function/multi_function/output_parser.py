import re
from typing import Union, Dict

from openfinance.agentflow.base_parser import BaseParser
from openfinance.agentflow.tool.base import Action


class FunctionOutParser(BaseParser):
    def parse(
        self, 
        text: str
    ) -> str:
        print("text", text)
        # \s matches against tab/newline/whitespace
        regex = (
            r"Function\s*\d*\s*:[\s]*(.*?)[\s]*Function\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
        )
        match = re.search(regex, text, re.DOTALL)
        #print(match)
        if not match:
            raise OutputParserException(f"Could not parse LLM output: `{text}`")
        
        action = match.group(1).strip().replace("\\", "")
        action_input = re.sub(r'\([^)]*\)', '', match.group(2)).replace('"', "").strip(" ") # delete parathese and its contents
        #print(action, "\n", action_input)
        return Action(name=action, action_input=action_input)