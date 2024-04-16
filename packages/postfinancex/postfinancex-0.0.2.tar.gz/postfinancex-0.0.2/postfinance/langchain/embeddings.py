from typing import Any, Dict, List, Optional, Sequence

import requests
from langchain_core.embeddings import Embeddings
from langchain_core.pydantic_v1 import BaseModel, SecretStr, root_validator
from langchain_core.utils import convert_to_secret_str, get_from_dict_or_env

JINA_API_URL: str = "https://api.jina.ai/v1/embeddings"


class JinaEmbeddings(BaseModel, Embeddings):
    """Jina embedding models.

    References:
        [1]: https://api.python.langchain.com/en/latest/_modules/langchain_community/embeddings/jina.html
        [2]: https://jina.ai/embeddings/#apiform
    """

    session: Any  #: :meta private:
    model: str = "jina-embeddings-v2-base-en"
    api_key: Optional[SecretStr] = None

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that credentials exist in environment."""
        try:
            api_key = convert_to_secret_str(
                get_from_dict_or_env(values, "api_key", "JINA_API_KEY")
            )
        except ValueError as e:
            raise e
        session = requests.Session()
        session.headers.update(
            {
                "Accept-Encoding": "identity",
                "Content-type": "application/json",
                "Authorization": f"Bearer {api_key.get_secret_value()}",
            }
        )
        values["session"] = session
        return values

    def _embed(self, texts: List[str]) -> List[List[float]]:
        # Call Jina AI's Embedding API
        response = self.session.post(
            JINA_API_URL,
            json={
                "input": texts,
                "model": self.model,
            },
        )

        data = response.json()

        if "data" not in data:
            raise RuntimeError(data["detail"])

        embeddings = data["data"]

        # Sort embeddings by index
        sorted_embeddings = sorted(embeddings, key=lambda e: e["index"])  # type: ignore

        # Return just the embeddings
        return [e["embedding"] for e in sorted_embeddings]

    def embed_documents(self, texts: Sequence[str]) -> List[List[float]]:
        """Call Jina AI's Embedding API.

        Args:
            texts (list[str]): The list of texts to embed.
        Returns:
            List of embeddings, one for each text.
        """
        return self._embed(list(texts))

    def embed_query(self, text: str) -> List[float]:
        """Call Jina AI's Embedding API.

        Args:
            text (str): The text to embed.
        Returns:
            Embeddings for the text.
        """
        return self._embed([text])[0]
