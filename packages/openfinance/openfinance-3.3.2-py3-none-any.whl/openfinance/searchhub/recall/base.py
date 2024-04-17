from typing import  Callable, Any, Dict, List, Union, Tuple
from pydantic import BaseModel

class IndexManager():
    def __init__(
        self, 
        config=None
    ):
        self.index_name_to_index = {}

    def register(
        self, 
        channel: dict, 
        index : Any
    ) -> None:
        try:
            if channel not in self.index_name_to_index.keys():
                self.index_name_to_index.update({channel: index})
        except:
            raise "No Channel config Found"

    def get(
        self, 
        index_name: str
    ):
        if index_name in self.index_name_to_index.keys():
            return self.index_name_to_index[index_name]
        return None
    
    def search(
        self, 
        index_name: str, 
        query: str
    ):
         if index_name in self.index_name_to_index.keys():
            return self.index_name_to_index[index_name].similarity_search(query)