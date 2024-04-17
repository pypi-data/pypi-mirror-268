import redis

class RedisManager:
    def __init__(self, config):
        self.name_to_client = {}
        for k, v in config.get("redis")["db"].items():
            self.name_to_client[k] = redis.Redis(
                host=config.get("redis")["host"], 
                port=6379, 
                db=v
            )
    @classmethod
    def create_client(cls, config):
        return redis.Redis(
            host=config.get("redis")["host"], 
            port=6379, 
            db=0
        )
    
    def get(self, name: str):
        if name in self.name_to_client:
            return self.name_to_client[name]
        return None