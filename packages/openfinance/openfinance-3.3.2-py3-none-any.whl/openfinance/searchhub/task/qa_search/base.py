import os
from typing import Any, Dict, List, Optional
from pydantic import BaseModel

from langchain.agents.agent import AgentExecutor
from langchain.agents.tools import Tool

class IntentExecutor(AgentExecutor):
    intent_name: str = ""

class IntentChainFactory:
    classes: Dict[str, IntentExecutor] = {}

    @classmethod
    def register_class(cls, base_class: IntentExecutor):
        cls.classes[base_class.intent_name] = base_class

    @classmethod
    def get_class(cls, name: str) -> IntentExecutor:
        return cls.classes[name]

    @classmethod
    def get_all_classes(cls) -> Dict[str, IntentExecutor]:
        return cls.classes