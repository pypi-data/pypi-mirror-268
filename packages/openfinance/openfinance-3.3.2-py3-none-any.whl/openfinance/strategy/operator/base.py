from typing import (
    List,
    Any,
    Dict,
    Union
)
import json
from abc import ABC, abstractmethod
from pydantic import BaseModel, root_validator

from openfinance.utils.singleton import singleton

class Operator(ABC, BaseModel):
    name: str
    def __call__(
        self,
        data,
        **kwargs        
    ):
        return self.run(
            data,
            **kwargs
        )

    @abstractmethod
    def run(
        self,
        data,
        **kwargs
    ):
        """
            Function to evaluate specific stocks
        """
        pass

@singleton
class OperatorManager:
    name_to_operators: Dict[str, Operator] = {}

    def _add(
        self, 
        operator: Operator 
    ) -> None:
        try:
            if operator.name not in self.name_to_operators:
                self.name_to_operators.update({operator.name: operator})
        except Exception as e:
            raise e

    def register(
        self, 
        operator : Union[List[Operator], Operator]
    ) -> None:
        if isinstance(operator, list):
            for i in operator:
                self._add(i())
        else:
            self._add(operator())

    def get(
        self, 
        name: str
    ):
        return self.name_to_operators.get(name, None)