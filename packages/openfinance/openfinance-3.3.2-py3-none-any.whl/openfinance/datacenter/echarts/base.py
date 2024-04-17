from typing import Any, Dict, List, Optional, Callable
from openfinance.utils.singleton import singleton

@singleton
class ChartManager:
    name = "ChartManager"
    name_to_func: Dict[str, Any] = {}

    def register(
        self,
        name,
        func
    ):
        if name not in self.name_to_func:
            self.name_to_func[name] = func
    
    def get(
        self,
        name
    ):
        if name in self.name_to_func:
            return self.name_to_func[name]
        else:
            return None