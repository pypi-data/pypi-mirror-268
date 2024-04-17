from openfinance.utils.embeddings.base import Embeddings
from pydantic import BaseModel, Extra, root_validator

class OpenAIEmbeddings(BaseModel, Embeddings):
    ## todo
    src = "openai"