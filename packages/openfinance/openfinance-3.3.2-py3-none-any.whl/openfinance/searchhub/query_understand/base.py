import json
import copy
from typing import Any, Dict, List, Optional, Callable, Union
from openfinance.datacenter.knowledge.entity_graph import EntityGraph

class QueryUnderstand:
    @classmethod
    def parse(
        cls,
        query: str
    ) -> Dict[str, Any]:
        entity = EntityGraph().extract_entity(query)
        if entity:
            return {
                "query": query,
                "company": entity
            }
        else:
            return {"query": query}

class IntentFactory:
    intents = {}
    @classmethod
    def register(cls, intent_name):
        def decorator(intent_class):
            cls.intents[intent_name] = intent_class
            return intent_class
        return decorator
    
    @classmethod
    def create(cls, intent_name, *args, **kwargs):
        if intent_name not in cls.intents:
            raise ValueError(f'Intent {intent_name} is not registered.')
        return cls.intents[intent_name](*args, **kwargs)

    @classmethod
    def get_intent_interface(cls, intent_name):
        intent_class = cls.intents.get(intent_name)
        if intent_class is None:
            raise ValueError(f'Intent {intent_name} is not registered.')            
        return intent_class