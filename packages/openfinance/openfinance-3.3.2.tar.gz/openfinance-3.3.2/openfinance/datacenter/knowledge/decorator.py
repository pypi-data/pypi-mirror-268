from functools import wraps
from openfinance.datacenter.knowledge.executor import ExecutorManager
from openfinance.datacenter.knowledge.entity_graph import EntityGraph

def register(name, description, signature="default", graph_node=True, **extend):
    #print("register")
    def call(func):
        #print("call")
        ExecutorManager().register(
            name = name,
            func = func,
            description = description,
            signature = signature,
            graph_node = graph_node,
            **extend
        )
        @wraps(func)
        def wrapper(*args, **kwargs):
            # update entity_type based on graph call
            # print(kwargs)
            if "executor" in kwargs:
                entity_type = EntityGraph().get_type_from_graph_path(
                    kwargs['executor']
                )
                if entity_type:
                    kwargs['entity_type'] = entity_type
            # print(kwargs)
            return func(*args, **kwargs)
        return wrapper    
    return call