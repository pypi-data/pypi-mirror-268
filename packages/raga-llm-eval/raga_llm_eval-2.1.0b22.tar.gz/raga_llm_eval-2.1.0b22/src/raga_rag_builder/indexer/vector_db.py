import os

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


class VectorDB:
    def __init__(self, db_path="./db", db_type="chroma", embedding_function=None):
        self.db_path = db_path
        self.db_type = db_type
        self.vectordb = None
        if embedding_function is None:
            self.embedding_function = OpenAIEmbeddings()
        else:
            self.embedding_function = embedding_function

    def get_similar_documents(self, query, k=5):
        if self.vectordb is None:
            print(
                "DB is not loaded or created. Please load or create the database first."
            )
            return []
        similar_docs = self.vectordb.similarity_search(query, k)
        return similar_docs

    def create_db(self, tokenized_chunks):
        raise NotImplementedError("create_db method must be implemented in subclasses.")

    def load_db(self):
        raise NotImplementedError("load_db method must be implemented in subclasses.")


class ChromaVectorDB(VectorDB):
    def create_db(self, tokenized_chunks):
        if tokenized_chunks is None:
            print("No documents found to create DB.")
            return self
        print("Creating Chroma DB")

        # Check if the db_path exists, in that case inform the user that db already exists
        if os.path.exists(self.db_path):
            print(f"DB already exists at {self.db_path}. Loading existing DB.")

            self.vectordb = Chroma(
                persist_directory=self.db_path,
                embedding_function=self.embedding_function,
            )
            return self
        else:
            self.vectordb = Chroma.from_documents(
                documents=tokenized_chunks,
                embedding=self.embedding_function,
                persist_directory=self.db_path,
            )
            return self

    def load_db(self):
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(
                f"DB does not exist at {self.db_path}. Please create DB first."
            )

        print("Loading Chroma DB...")
        self.vectordb = Chroma(
            persist_directory=self.db_path, embedding_function=self.embedding_function
        )
        return self
