import re
import json

from typing import Dict

from openfinance.agentflow.base_parser import BaseParser

class TaskOutputParser(BaseParser):
    def parse(
        self, 
        text: str
    ) -> Dict[str, str]:
        print("percept: ", text)
        try:
            return json.loads(text)
        except:
            result = {}
            vret = text.split("Result:")
            if len(vret) == 2:
                result = vret[1].replace("`", "")
                if result.endswith((",", ".")):
                    result = result[:-1]
                try:
                    result = json.loads(result)
                except:
                    return {}
            return result