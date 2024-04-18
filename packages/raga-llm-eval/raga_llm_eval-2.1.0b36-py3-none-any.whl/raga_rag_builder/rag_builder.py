import os

import litellm

# from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

from .data_loader import ContentLoader
from .indexer.tokenizer import DocumentTokenizer
from .indexer.vector_db import ChromaVectorDB
from .retrieval_engine import PromptManager


class RAGBuilder:
    def __init__(self, api_keys=None):
        self.data_dir = None
        self.pages = None
        self.tokenized_chunks = None
        self.vector_db = None
        self.similar_docs = None
        self.reranked_docs = None
        self.final_prompt = None
        self.prompt_manager = PromptManager()

        # set the OpenaAI api key as an environment variable
        if api_keys is not None:
            if "OPENAI_API_KEY" in api_keys:
                os.environ["OPENAI_API_KEY"] = api_keys["OPENAI_API_KEY"]

    def load_content(self, data_dir, file_types=None):
        print("Loading content...")
        pages = []
        self.data_dir = data_dir

        if file_types is None:
            content_loader = ContentLoader(data_dir)
            pages.append(content_loader.get_content())
        else:
            if isinstance(file_types) == str:
                file_types = [file_types]

            for file_type in file_types:
                content_loader = ContentLoader(data_dir)
                pages.append(content_loader.get_content(file_type))

        self.pages = pages

        return self

    def tokenize_documents(self, chunk_size=1000, tokenizer_name="thenlper/gte-small"):
        print("Tokenizing documents...")
        tokenized_chunks = DocumentTokenizer(
            chunk_size=chunk_size, tokenizer_name=tokenizer_name
        ).split_documents(self.pages)

        self.tokenized_chunks = tokenized_chunks

        return self

    def create_db(
        self,
        db_path,
        db_type="chroma",
        embedding_model_name="sentence-transformers/all-mpnet-base-v2",
        device="cpu",
        normalise_embeddings=False,
    ):

        print("Creating vector database...")

        model_name = embedding_model_name
        model_kwargs = {"device": device}
        encode_kwargs = {"normalize_embeddings": normalise_embeddings}

        if db_type == "chroma":
            self.vector_db = ChromaVectorDB(
                db_path=db_path,
                db_type=db_type,
                embedding_function=HuggingFaceEmbeddings(
                    model_name=model_name,
                    model_kwargs=model_kwargs,
                    encode_kwargs=encode_kwargs,
                ),
            ).create_db(self.tokenized_chunks)

            return self
        else:
            raise NotImplementedError(
                f"Vector database type '{db_type}' is not currently supported."
            )

    def load_db(self, db_path, db_type="chroma"):
        if db_type == "chroma":
            self.vector_db = ChromaVectorDB(
                db_path=db_path,
                db_type=db_type,
                embedding_function=OpenAIEmbeddings(),
            ).load_db()

            print("Vector database loaded.")

            return self
        else:
            raise NotImplementedError(
                f"Vector database type '{db_type}' is not currently supported."
            )

    def get_similar_documents(self, query, k=5):
        if self.vector_db is None:
            print(
                "DB is not loaded or created. Please load or create the database first."
            )
            return []
        self.similar_docs = self.vector_db.get_similar_documents(query, k)

        return self

    def get_context(self):
        def get_filtered_context(docs):
            return [doc.page_content for doc in docs]

        return {
            "similar": get_filtered_context(self.similar_docs),
            "reranked": get_filtered_context(self.reranked_docs),
        }

    def get_reranked_documents(self, query, k=5):
        if self.vector_db is None:
            print(
                "DB is not loaded or created. Please load or create the database first."
            )
            return []
        self.reranked_docs = self.vector_db.get_similar_documents(query, k)

        return self

    def view_prompt_template(self, template_name):
        self.prompt_manager.view_template(template_name=template_name)
        return self

    def edit_prompt_template(self, template_name, new_template):
        self.prompt_manager.edit_template(
            template_name=template_name, new_template=new_template
        )
        return self

    def add_prompt_template(self, template_name, template_content):
        self.prompt_manager.add_template(
            template_name=template_name, template_content=template_content
        )
        return self

    def create_prompt(self, query, template_name, **kwargs):
        if self.reranked_docs is not None:
            context = self.reranked_docs
        elif self.similar_docs is not None:
            context = self.similar_docs
        else:
            print(
                "No similar or reranked documents found. Please retrieve documents first."
            )
            return self

        self.final_prompt = self.prompt_manager.create_prompt(
            context=context, query=query, template_name=template_name, **kwargs
        )

        return self.final_prompt

    def query_llm(self, model_name, final_prompt, api_base=None):
        """
        Executes a query to the language model using the provided model name and messages.

        Parameters:
            self: The object instance.
            model_name (str): The name of the language model.

        Returns:
            The response from the language model.
        """
        messages = [{"content": final_prompt, "role": "user"}]
        litellm.verbose = True
        if api_base is None:
            response = litellm.completion(model=model_name, messages=messages)
        else:
            response = litellm.completion(
                model=model_name, messages=messages, api_base=api_base
            )

        return response

    def get_final_prompt(self):
        if self.final_prompt is None:
            print(
                "No prompt created. Please use the RAG Builder to create a RAG pipeline."
            )
            return None
        else:
            return self.final_prompt


# sample usage
if __name__ == "__main__":
    # from rag_builder import RAGBuilder
    import os

    from dotenv import load_dotenv

    load_dotenv()

    # Create an instance of RAGBuilder
    builder = RAGBuilder()

    # Load content from a directory
    builder.load_content(
        data_dir="/Users/kiran-raga/RagaAI/llm-package/raga-llm-eval/tests/test_data"
    )

    # Tokenize the loaded documents
    builder.tokenize_documents(chunk_size=500)

    # Create a vector database
    builder.create_db(
        db_path="/Users/kiran-raga/RagaAI/llm-package/raga-llm-eval/tests/test_db",
        db_type="chroma",
        embedding_model_name="sentence-transformers/all-mpnet-base-v2",
        device="cpu",
        normalise_embeddings=False,
    )

    # Retrieve similar documents based on a query
    query = "What is GoD?"
    builder.get_similar_documents(query=query, k=10)

    # Retrieve reranked documents based on a query
    builder.get_reranked_documents(query=query, k=5)

    # View a prompt template
    builder.view_prompt_template(template_name="default")

    # # Edit a prompt template
    # new_template = "Answer the following question based on the provided context:\n\nContext: {context}\n\nQuestion: {query}\n\nAnswer:"
    # builder.edit_prompt_template(template_name="default", new_template=new_template)

    # # Add a new prompt template
    # template_name = "custom_template"
    # template_content = "Provide a detailed explanation for the following query based on the given context:\n\nContext: {context}\n\nQuery: {query}\n\nExplanation:"
    # builder.add_prompt_template(
    #     template_name=template_name, template_content=template_content
    # )

    # Create a prompt based on a query and a template
    final_prompt = builder.create_prompt(query=query, template_name="default")

    # Query the language model
    response = builder.query_llm(
        model_name="ollama/llama2",
        final_prompt=final_prompt,
        api_base="http://localhost:11434",
    )
    print(response)


# # sample usage 2
# from rag_builder import RAGBuilder

# query = "What is the meaning of life?"

# builder = (
#     RAGBuilder(api_keys={"OPENAI_API_KEY": "your_openai_api_key"})
#     .load_content(data_dir="path/to/your/data")
#     .tokenize_documents(chunk_size=500)
#     .create_db.create_db(
#         db_path="/Users/kiran-raga/RagaAI/llm-package/raga-llm-eval/tests/test_db",
#         db_type="chroma",
#     )
#     .get_similar_documents(query=query, k=3)
#     .get_reranked_documents(query=query, k=3)
#     # .view_prompt_template(template_name="default")
#     # .edit_prompt_template(
#     #     template_name="default",
#     #     new_template="Answer the following question based on the provided context:\n\nContext: {context}\n\nQuestion: {query}\n\nAnswer:",
#     # )
#     # .add_prompt_template(
#     #     template_name="custom_template",
#     #     template_content="Provide a detailed explanation for the following query based on the given context:\n\nContext: {context}\n\nQuery: {query}\n\nExplanation:",
#     # )
# )

# final_prompt = builder.create_prompt(query=query, template_name="default")

# # Query the language model
# response = builder.query_llm(
#     model_name="ollama/llama2",
#     final_prompt=final_prompt,
#     api_base="http://localhost:11434",
# )
# print(response)


# # sample usage 3
# from rag_builder import RAGBuilder

# query = "What is the meaning of life?"


# def get_rag_response(query, config):

#     rag_builder = RAGBuilder(
#         api_keys={"OPENAI_API_KEY": st.session_state["openai_api_key"]}
#     )

#     if not os.path.exists(config["data_dir"]):
#         rag_builder = (
#             rag_builder.load_content(data_dir=config["data_dir"])
#             .tokenize_documents(chunk_size=config["chunk_size"])
#             .create_db()
#         )
#     else:
#         rag_builder = rag_builder.load_db()

#     final_prompt = (
#         rag_builder.get_similar_documents(query=query, k=config["similarity_k"])
#         .get_reranked_documents(query=query, k=config["reranking_k"])
#         .create_prompt(query=query, template_name="default")
#         .get_final_prompt()
#     )

#     response = rag_builder.query_llm(model_name="gpt-3.5-turbo", prompt=final_prompt)

#     return response


# print(get_rag_response(query=query))
