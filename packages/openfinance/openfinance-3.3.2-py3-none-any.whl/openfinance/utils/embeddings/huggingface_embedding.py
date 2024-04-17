from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Extra, root_validator
from huggingface_hub.inference_api import InferenceApi

from openfinance.utils.embeddings.base import Embeddings

class HuggingFaceHubEmbeddings(BaseModel, Embeddings):
    """HuggingFaceHub embedding models.
    """
    src = "huggingface"    
    client: Any  #: :meta private:
    repo_id: str = "sentence-transformers/all-MiniLM-L12-v2"
    """Model name to use."""
    task: Optional[str] = "feature-extraction"
    """Task to call the model with."""
    model_kwargs: Optional[dict] = None
    """Key word arguments to pass to the model."""

    huggingfacehub_api_token: Optional[str] = "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"

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        repo_id = values["repo_id"]
        client = InferenceApi(
            repo_id=repo_id,
            token=huggingfacehub_api_token,
            task=values.get("task"),
        )
        values["client"] = client
        return values

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Call out to HuggingFaceHub's embedding endpoint for embedding search docs.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        # replace newlines, which can negatively affect performance.
        texts = [text.replace("\n", " ") for text in texts]
        _model_kwargs = self.model_kwargs or {}
        responses = self.client(inputs=texts, params=_model_kwargs)
        return responses

    def embed_query(self, text: str) -> List[float]:
        """Call out to HuggingFaceHub's embedding endpoint for embedding query text.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        response = self.embed_documents([text])[0]
        return response