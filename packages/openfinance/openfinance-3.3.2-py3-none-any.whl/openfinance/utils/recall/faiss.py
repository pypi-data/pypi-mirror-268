from __future__ import annotations

import math
import dill
import faiss
import numpy as np

from pathlib import Path

from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple
from openfinance.utils.recall.base import RecallBase
from openfinance.utils.embeddings.base import Embeddings

class Faiss(RecallBase):
    name="Faiss"
    index: Any
    embedding: Embeddings
    metadatas: List[Any]
    class Config:
        """Configuration for this pydantic object."""
        arbitrary_types_allowed = True

    @classmethod
    def from_embedding(
        cls,
        inputs: Union[Dict[str, Any], List[str]],        
        embedding: Embeddings
    ) -> "Faiss":
        docs = list()
        metadatas = list()
        if isinstance(inputs, dict):
            for k, v in inputs.items():
                docs.append(k)
                metadatas.append(v)
        elif isinstance(inputs, list):
            docs = inputs
            metadatas = inputs

        embeddings = embedding.embed_documents(docs)
        embed_len = len(embeddings[0])
        index = faiss.IndexFlatL2(embed_len)
        vectors = np.array(embeddings, dtype=np.float32)
        index.add(vectors)
        return cls(index=index, embedding=embedding, metadatas=metadatas)

    def save(
        self, 
        folder_path: str, 
        index_name: str = "index"
    ) -> None:
        path = Path(folder_path)
        path.mkdir(exist_ok=True, parents=True)

        faiss.write_index(
            self.index, str(path / "{index_name}.faiss".format(index_name=index_name))
        )

        # save docstore and index_to_docstore_id
        with open(path / "{index_name}.pkl".format(index_name=index_name), "wb") as f:
            dill.dump(self.metadatas, f)

    @classmethod
    def load(
        cls,
        embedding: Embeddings,
        folder_path: str, 
        index_name: str = "index"
    ) -> "Faiss":
        index =faiss.read_index(folder_path + f"/{index_name}.faiss")
        metadatas = dill.load(open(folder_path + f"/{index_name}.pkl", "rb"))
        return cls(embedding=embedding, index=index, metadatas=metadatas)

    def similarity_search(
        self,
        text: str,
        top_k: int = 4,
        **kwargs: Any
    ) -> List[Any]:
        vector = np.array([self.embedding.embed_query(text)], np.float32)
        #print(vector, top_k)
        scores, indices = self.index.search(vector, top_k)
        #print(scores, indices)
        results = [self.metadatas[i] for i in indices[0]]
        return results

    def similarity_search_with_score(
        self,
        text: str,
        top_k: int = 4,
        **kwargs: Any
    ) -> Dict[Any, Any]:
        vector = np.array([self.embedding.embed_query(text)], np.float32)
        #print(vector, top_k)
        scores, indices = self.index.search(vector, top_k)
        #print(scores, indices)
        #results = [self.metadatas[i] for i in indices[0]]
        results = {
            self.metadatas[indices[0][i]]: scores[0][i] for i in range(len(indices[0]))
        }
        return results