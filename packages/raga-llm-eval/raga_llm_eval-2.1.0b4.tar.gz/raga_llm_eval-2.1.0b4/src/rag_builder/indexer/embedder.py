from langchain_community.embeddings import HuggingFaceEmbeddings


class EmbeddingGenerator:
    def __init__(self):
        self.embedding_model_name = "thenlper/gte-small"

    def intialize_embedder(self, embedding_model=None):
        if embedding_model is not None:
            return embedding_model
        else:
            print("Embedding model not provided. Initializing default model.")
            embedding_model = HuggingFaceEmbeddings(
                model_name=self.embedding_model_name,
                multi_process=False,
                model_kwargs={"device": "cpu"},
                encode_kwargs={
                    "normalize_embeddings": True
                },  # set True for cosine similarity
            )
            return embedding_model
