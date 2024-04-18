from flask import Flask, request, render_template, jsonify
import os
import toml
from flask_ngrok3 import run_with_ngrok
from .rag_builder import RAGBuilder

app = Flask(__name__)
run_with_ngrok(app)

# Load configuration
config_path = os.getenv("RAGA_RAG_CONFIG_PATH")
if not config_path:
    raise ValueError("Configuration file path not set.")

with open(config_path, "r") as config_file:
    config = toml.load(config_file)


# Initialize RAGBuilder
def initialize_rag_builder(config):
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


rag_builder = initialize_rag_builder(config)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/query", methods=["POST"])
def query():
    data = request.json
    query = data["query"]

    # context retrieval
    rag_builder.get_similar_documents(query=query, k=10)

    # re-ranking
    rag_builder.get_reranked_documents(query=query, k=5)

    # check if api_base is set
    if config.get("api_base", None) is None:
        response = rag_builder.query_llm(
            model_name=config["llm_model_name"],
            final_prompt=rag_builder.create_prompt(
                query=query, template_name=config["template_name"]
            ),
        )
    else:
        response = rag_builder.query_llm(
            model_name=config["llm_model_name"],
            final_prompt=rag_builder.create_prompt(
                query=query, template_name=config["template_name"]
            ),
            api_base=config["api_base"],
        )
    return jsonify({"response": response.choices[0].message.content})


def main():
    app.run()


if __name__ == "__main__":
    main()
