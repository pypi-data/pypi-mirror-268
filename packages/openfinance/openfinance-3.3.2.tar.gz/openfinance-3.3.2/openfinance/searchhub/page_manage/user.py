import random
import json
from typing import Any, Dict, List
from openfinance.searchhub.page_manage.base import BaseElement
from openfinance.utils.redis.redis_tools import RedisManager


class User(BaseElement):
    stype: str = "User"

class UserManager:
    def __init__(
        self, 
        config
    ):
        self.type_to_ele: Dict[str, User] = {}
        self.redis_manager = RedisManager(config=config)

    def register(
        self, 
        name: str, 
        base: User
    ) -> None:
        if name not in self.type_to_ele:
            self.type_to_ele[name] = base

    def get(
        self, 
        name: str
    ) -> User:
        return self.type_to_ele.get(name, None)

    def get_history(
        self, 
        session_id: str
    ) -> Dict[str, Any]:
        """
            For chat front message
        """
        result = []
        #return self.redis_manager.get("session").lrange(session_id, 0, -1).decode('utf-8')

        for d in self.redis_manager.get("session").lrange(session_id, 0, -1):
            result.append(
                json.loads(d)
            )
        return result

    def get(
        self, 
        name: str
    ) -> User:
        return self.type_to_ele.get(name, None)

    def get_llm_history(
        self, 
        session_id: str,
        limit = 2
    ) -> Dict[str, Any]:
        """
            For chat front message
        """
        result = ""
        for d in self.redis_manager.get("session").lrange(session_id, -1-limit, -1):
            d = json.loads(d)
            result += "Human: " + str(d.get("input", "")) + "\n"
            result += "Assitant: " + str(d.get("output", "")) + "\n"
        if result:
            return result + "Human: "
        else:
            return ""

    def insert_history(
        self, 
        session_id, 
        json_data
    ):
        #print(session_id, json_data)        
        self.redis_manager.get("session").rpush(session_id, json_data)  

    def get_snapshot(
        self, 
        user: str
    ) -> Dict[str, Any]:
        result = []
        try:
            return [json.loads(a.decode('utf8')) for a in self.redis_manager.get("chatshot").lrange(user, 0, -1)]
        except:
            return result

    def insert_snapshot(
        self, 
        user: str, 
        session_id: str, 
        query: str
    ):
        print(user, session_id, query)
        if not self.redis_manager.get("session").exists(session_id):
            self.redis_manager.get("chatshot").rpush(user, json.dumps({
                "session_id": session_id,
                "desc": query
            }))