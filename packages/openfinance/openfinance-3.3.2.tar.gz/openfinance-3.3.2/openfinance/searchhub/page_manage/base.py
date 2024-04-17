from typing import Any, Dict, List

from pydantic import BaseModel


class BaseElement(BaseModel):
    stype: str = ""
    sData: Dict[str, Any] = {}

class ElementManager:
    type_to_ele: Dict[str, BaseElement] = {}

    def register(
        self, 
        stype: str, 
        base: BaseElement
    ) -> None:
        if stype not in self.type_to_ele:
            self.type_to_ele[stype] = base

    def get(
        self, 
        stype: str
    ) -> BaseElement:
        return self.type_to_ele.get(stype, None)
