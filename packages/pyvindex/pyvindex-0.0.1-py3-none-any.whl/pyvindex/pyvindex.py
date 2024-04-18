"""Embedding file to store VectorIndex class."""
import pickle
from typing import Any
import numpy as np
import sentence_transformers
# from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from scipy.spatial.distance import cdist

# DEFAULT_MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
DEFAULT_MODEL_NAME = "sentence-transformers/msmarco-distilbert-base-tas-b"


class VectorIndex:
    """Class to handle vector index."""
    model_name = DEFAULT_MODEL_NAME

    def __init__(self) -> None:
        self.__vectors: list[list] = []
        self.__datas: list[str] = []
        self.__multi_process = False
        self.show_progress = False
        # self.embedding: Embeddings = embedding()
        self.client = sentence_transformers.SentenceTransformer(
            self.model_name, device="mps", cache_folder="embedding_model_cache")

    def add(self, text: str, metadata: dict = {}):
        """Add text to the db."""
        metadata["__text"] = text
        vec = self.__embed_query(text)
        self.__vectors.append(vec)
        self.__datas.append(metadata)

    def search(self, text: str, k: int = 5):
        """Search db for record"""
        qvec = self.__embed_query(text)
        distances = cdist(np.expand_dims(qvec, axis=0),
                          self.__vectors, 'euclidean')
        indices = np.argsort(distances)[0][:k]
        texts = np.array(self.__datas)[indices]
        return list(zip(texts, distances[0][indices], indices))

    def delete(self, index: int):
        """Delete a record by index from the db."""
        self.__vectors.pop(index)
        self.__datas.pop(index)

    def save(self, filename: str):
        """Save the file"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename: str) -> "VectorIndex":
        """Load the file"""

        with open(filename, "rb") as f:
            obj = pickle.load(f)

        assert isinstance(obj, VectorIndex)
        return obj

    def __embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Compute doc embeddings using a HuggingFace transformer model.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """

        texts = list(map(lambda x: x.replace("\n", " "), texts))
        if self.__multi_process:
            pool = self.client.start_multi_process_pool()
            embeddings = self.client.encode_multi_process(texts, pool)
            sentence_transformers.SentenceTransformer.stop_multi_process_pool(
                pool)
        else:
            embeddings = self.client.encode(
                texts, show_progress_bar=self.show_progress
            )

        return embeddings.tolist()

    def __embed_query(self, text: str) -> list[float]:
        """Compute query embeddings using a HuggingFace transformer model.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        return self.__embed_documents([text])[0]
