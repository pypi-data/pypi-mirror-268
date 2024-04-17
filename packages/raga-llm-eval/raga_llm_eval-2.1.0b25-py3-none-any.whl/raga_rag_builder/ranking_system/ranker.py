from ragatouille import RAGPretrainedModel


class ReRanker:
    def __init__(self):

        # ColBERT is a fast and accurate retrieval model, enabling scalable BERT-based search
        # over large text collections in tens of milliseconds.
        self.RERANKER = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")

    def rerank_documents(self, query, documents, top_k=3):
        # print("Reranking documents...")
        # Rerank the documents
        relevant_docs = [doc.page_content for doc in documents]
        rerank_relevant_docs = self.RERANKER.rerank(query, relevant_docs, k=top_k)
        reranked_docs = [doc["content"] for doc in rerank_relevant_docs]
        return reranked_docs
