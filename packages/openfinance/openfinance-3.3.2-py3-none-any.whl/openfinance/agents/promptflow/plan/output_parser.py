import re
import json

from typing import Dict

from openfinance.agentflow.base_parser import BaseParser

class TaskOutputParser(BaseParser):
    def parse(
        self, 
        text: str
    ) -> Dict[str, str]:
        result = {}
        vret = text.split("Subtasks:")
        # sometimes it generate more subtasks format
        if len(vret) > 1:
            content = vret[-1].replace("`", "")
            if content.endswith((",", ".")):
                content = content[:-1]
            try:
                result = json.loads(content)
            except:
                # parse manuelly sometimes not in valid json
                temp_key = ""
                for line in content.split("\n"):
                    if len(line) <= 1 or len(line) > 50:
                        continue
                    if line.startswith(" "):
                        result[temp_key].append(line.replace("-", "").strip())
                    else:
                        temp_key = line.strip()
                        result.update({temp_key: []})
        return result