import base64
import os

import streamlit as st
import toml

from raga_rag_builder import RAGBuilder


@st.cache_resource
def get_raga_rag_builder(config):
    # Setup the RAG Builder
    builder = RAGBuilder()
    builder.load_content(data_dir=config["data_dir"])
    builder.tokenize_documents(chunk_size=config["chunk_size"])
    builder.create_db(
        db_path=config["db_path"],
        db_type=config["db_type"],
        embedding_model_name=config["embedding_model_name"],
        device=config["device"],
        normalise_embeddings=config["normalise_embeddings"],
    )
    return builder


class LLMChatBot:
    @staticmethod
    def get_image(RagaAI_logo_url, RagaAI_webpage_url):
        # with open(RagaAI_logo_url, "rb") as f:
        #     image_data = f.read()
        #     encoded_image = base64.b64encode(image_data).decode()
        # image_with_link = f'<a href="{RagaAI_webpage_url}" target="_blank"><img src="data:image/png;base64,{encoded_image}" alt="Image"></a>'
        image_with_link = f'<a href="{RagaAI_webpage_url}" target="_blank"><img src="{RagaAI_logo_url}" alt="Image"></a>'
        st.sidebar.markdown(image_with_link, unsafe_allow_html=True)

    @staticmethod
    def launch_UI():
        # Get the path of the TOML file from an environment variable
        config_path = os.getenv("RAGA_RAG_CONFIG_PATH")
        if not config_path:
            st.error(
                "Configuration file path not set. Please set the RAGA_CONFIG_PATH environment variable."
            )
            st.stop()

        # Load the configuration from TOML file
        with open(config_path, "r") as config_file:
            config = toml.load(config_file)

            # streamlit config
            RagaAI_logo_url = (
                "https://ragakibalti.s3.ap-south-1.amazonaws.com/RagaAI_logo.png"
            )
            RagaAI_webpage_url = "https://www.raga.ai/"

            builder = get_raga_rag_builder(config)

        def get_rag_response(query, config):
            # Retrieve similar documents based on a query
            builder.get_similar_documents(query=query, k=config["k_similar"])

            # Retrieve reranked documents based on a query
            builder.get_reranked_documents(query=query, k=config["k_reranked"])

            # Create a prompt based on a query and a template
            final_prompt = builder.create_prompt(
                query=query, template_name=config["template_name"]
            )

            # Query the language model
            response = builder.query_llm(
                model_name=config["llm_model_name"],
                final_prompt=final_prompt,
                api_base=config["api_base"],
            )

            return response

        st.title("RagaAI LLM Chat App")
        LLMChatBot.get_image(RagaAI_logo_url, RagaAI_webpage_url)
        OPENAI_API_KEY = st.sidebar.text_input(
            "Enter OpenAI API key here", type="password"
        )

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if query := st.chat_input():
            st.session_state.messages.append({"role": "user", "content": query})
            with st.chat_message("user"):
                st.markdown(query)

            with st.chat_message("assistant"):
                response = get_rag_response(query=query, config=config)
                response_msg = response.choices[0].message.content
                st.write(response_msg)

            st.session_state.messages.append(
                {"role": "assistant", "content": response_msg}
            )


if __name__ == "__main__":
    LLMChatBot.launch_UI()
