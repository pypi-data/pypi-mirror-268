from openfinance.config import Config
from openfinance.agentflow.llm.manager import ModelManager 
from openfinance.searchhub.query_understand.base import SearchIntentChain

from openfinance.searchhub.task.qa_search.stock.base import StockInfoChain
from openfinance.searchhub.task.qa_search.macro.base import StockMacroChain
from openfinance.searchhub.task.qa_search.strategy.base import StockStrategyChain
from openfinance.searchhub.task.qa_search.base import IntentChainFactory

from openfinance.datacenter.database.source.eastmoney.tool import (
    fundamental_tools,
    macro_tools
)
from openfinance.datacenter.database.source.strategy.tool import (
    strategy_tools
)

config = Config()
model_manager = ModelManager(config=config)
llm = model_manager.get_model("claude")
    
def qa(query):

    chain = SearchIntentChain.from_llm(llm)
    result = chain.run({"query": query})
    
    intent_factory = IntentChainFactory()
    intent_factory.register_class(StockInfoChain.from_chains(llm, fundamental_tools))
    intent_factory.register_class(StockMacroChain.from_chains(llm, macro_tools))
    intent_factory.register_class(StockStrategyChain.from_chains(llm, strategy_tools))

    if result in intent_factory.get_all_classes():
        result = intent_factory.get_class(result).run({"input": query})
        
    return result.to_string()