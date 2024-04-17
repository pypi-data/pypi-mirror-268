import random
import json
from typing import Any, Dict, List
from openfinance.searchhub.page_manage.base import BaseElement
from openfinance.agents.role.prompts import roles_prompts

class Role(BaseElement):
    stype: str = "Role"

class RoleManager:
    type_to_ele: Dict[str, Role] = {}

    def register(
        self, 
        name: str,
        base: Role
    ) -> None:
        if name not in self.type_to_ele:
            self.type_to_ele[name] = base

    def get(
        self, 
        name: str
    ) -> Role:
        return self.type_to_ele.get(name, None)

    # will be moved to db later
    def get_details(
        self, 
        role: str
    ) -> Dict[str, Any]:
        return {
            "role": role,
            "icon": "",
            "id": "",
            "desc": "大佬",
        }

    def get_homepage(
        self, 
        num: int
    ) -> Dict[str, Any]:
        result = []
        for d in roles_prompts.keys():
            result.append(self.get_details(d))
        print(result)
        return result