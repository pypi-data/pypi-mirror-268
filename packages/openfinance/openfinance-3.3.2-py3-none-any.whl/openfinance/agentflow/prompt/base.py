from typing import (
    Any,
    Callable,
    Dict,
    Union,
    List
)
from pydantic import BaseModel


class PromptTemplate(BaseModel):
    prompt: str
    variables: List[str]

    def get_variables(
        self
    ) -> List[str]:
        return self.variables

    def prepare(
        self,
        inputs: Dict[str, str]        
    ):
        return self.prompt.format(**inputs)

    def __add__(
        self,
        strs: str
    ):
        self.prompt += strs

    def __iadd__(
        self,
        strs: str
    ):
        self.prompt += strs
        return self