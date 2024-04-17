from openfinance.utils.singleton import singleton
from openfinance.agentflow.llm.chatgpt import ChatGPT
from openfinance.agentflow.llm.webgpt import WebGPT
from openfinance.agentflow.llm.aliyungpt import AliyunGPT
from openfinance.config import Config

@singleton
class ModelManager:
    def __init__(
        self, 
        config
    ):
        self.config = config
        self.models = {}        
        for k, v in self.config.get("models").items():
            if k == "aliyungpt":
                self.register_model(
                    k, AliyunGPT
                )
            elif k == "webgpt":
                self.register_model(
                    k, WebGPT
                )
            elif k == "chatgpt":
                self.register_model(
                    k, ChatGPT
                )                

    def conf(
        self,
        model,
        key
    ):
        return self.config.get("models")[model][key]

    def register_model(
        self, 
        model_name, 
        model_class
    ):
        if not self.config.get("models").get(model_name, ""):
            return
     
        self.models[model_name] = model_class(
             model=self.conf(model_name, "model_name"),
             api_key=self.conf(model_name, "token"),
             base_url=self.conf(model_name, "api_base")
        )
            
    def get_model(
        self, 
        model_name
    ):
        return self.models[model_name]

