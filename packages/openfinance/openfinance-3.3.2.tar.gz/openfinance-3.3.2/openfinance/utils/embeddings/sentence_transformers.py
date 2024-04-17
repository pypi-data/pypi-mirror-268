"""Wrapper around HuggingFace Hub embedding models."""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from openfinance.utils.embeddings.base import Embeddings

import requests
import aiohttp

import json

class RemoteEmbeddings(BaseModel, Embeddings):
    """Wrapper around RemoteEmbeddings embedding models.   
    """
    src = "remote"
    url: str = "http://114.132.71.128:5008/predict" 
    # all-MiniLM-L12-v2
    """Model name to use."""
    task: Optional[str] = "semantic"
    """Task to call the model with."""
    model_kwargs: Optional[dict] = None
    """Key word arguments to pass to the model."""

    def prepare_input(self, text) -> str:
        data_json = '{"header":{"req_id":"123"},"texts":"' + text + '"}'
        return data_json.encode('utf-8')

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Call out to RemoteEmbeddings's embedding endpoint for embedding search docs.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        responses = []
        for text in texts:
            responses.append(self.embed_query(text))

        return responses

    def embed_query(self, text: str) -> List[float]:
        """Call out to RemoteEmbeddings's embedding endpoint for embedding query text.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        response = requests.post(url=self.url, 
                                  data=self.prepare_input(text), 
                                  timeout=3)

        return json.loads(response.text)["embedding"]
        """
        return [1.0, 1.0, 1.0]
        """

    async def aembed_query(
        self,
        text: str
    ) -> List[float]:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                self.url,
                data = self.prepare_input(text),
                headers= {
                    'Content-Type': 'application/json',
                }
            ) as response:
                resp = await response.text()
        return json.loads(resp)["embedding"]