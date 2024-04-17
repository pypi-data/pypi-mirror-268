import json
from openfinance.utils.singleton import singleton

@singleton
class Config:
    def __init__(
        self, 
        filename="openfinance/config/config.json"
    ):
        with open(filename, 'r') as f:
            self.config = json.load(f)
    
    def get(
        self, 
        key
    ):
        return self.config.get(key)
    
    def set(
        self, 
        key, 
        value
    ):
        self.config[key] = value

    def save(
        self, 
        filename
    ):
        with open(filename, 'w') as f:
            json.dump(self.config, f)