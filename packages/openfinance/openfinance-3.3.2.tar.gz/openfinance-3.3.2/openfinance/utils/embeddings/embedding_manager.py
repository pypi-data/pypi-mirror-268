import json
from typing import Any, Dict, List
from openfinance.utils.embeddings.sentence_transformers import RemoteEmbeddings
from openfinance.utils.embeddings.sentence_transformers_cn import ChineseEmbeddings
from openfinance.utils.embeddings.huggingface_embedding import HuggingFaceHubEmbeddings
from openfinance.utils.embeddings.openai_embedding import OpenAIEmbeddings

class EmbeddingManager:
    @classmethod
    def get_embedding(self, config):
        embedding = config.get("faiss", {}).get("embedding", "")
        try:
            if "remote" == embedding:
                return RemoteEmbeddings()
            if "huggingface" == embedding:
                return HuggingFaceHubEmbeddings()
            if "openai"== embedding:
                return OpenAIEmbeddings()
            if "cn" == embedding:
                return ChineseEmbeddings()
        except:
            pass    
        return ChineseEmbeddings()