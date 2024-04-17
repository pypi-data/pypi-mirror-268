import asyncio
import logging
import math
import warnings
from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
)

class Document:
    doc_id: str

class RecallBase(BaseModel):
    name: str

    def similarity_search(
        self,
        text,
        **kwargs: Any
    ) -> List[Any]:
        pass

    def save(
        self,
        path: str,
        **kwargs: Any        
    ):
        pass

    def load(
        self,
        path: str,        
        **kwargs: Any        
    ):
        pass