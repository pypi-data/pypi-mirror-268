# Autotokenizer
from typing import Dict, List, Optional

import pandas as pd
from langchain.docstore.document import Document as LangchainDocument
from langchain.text_splitter import RecursiveCharacterTextSplitter
from tqdm import tqdm
from transformers import AutoTokenizer

EMBEDDING_MODEL_NAME = "thenlper/gte-small"

MARKDOWN_SEPARATORS = [
    "\n#{1,6} ",
    "```\n",
    "\n\\*\\*\\*+\n",
    "\n---+\n",
    "\n___+\n",
    "\n\n",
    "\n",
    " ",
    "",
]


class DocumentTokenizer:
    def __init__(
        self, chunk_size: int, tokenizer_name: Optional[str] = EMBEDDING_MODEL_NAME
    ):
        self.chunk_size = chunk_size
        self.tokenizer_name = tokenizer_name

    def split_documents(self, documents_types) -> List[LangchainDocument]:
        text_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
            AutoTokenizer.from_pretrained(self.tokenizer_name),
            chunk_size=self.chunk_size,
            chunk_overlap=int(self.chunk_size / 10),
            add_start_index=True,
            strip_whitespace=True,
            separators=MARKDOWN_SEPARATORS,
        )

        # import pdb

        # pdb.set_trace()

        knowledge_base = []
        for documents in documents_types:
            for key, document in documents.items():
                for items in document:
                    knowledge_base.append(items)

        docs_processed = []
        for doc in knowledge_base:
            for sub_doc in doc:
                docs_processed += text_splitter.split_documents([sub_doc])

        # Remove duplicates
        unique_texts = {}
        docs_processed_unique = []
        for doc in docs_processed:
            if doc.page_content not in unique_texts:
                unique_texts[doc.page_content] = True
                docs_processed_unique.append(doc)

        # tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL_NAME)
        # lengths = [len(tokenizer.encode(doc.page_content)) for doc in tqdm(docs_processed)]
        # fig = pd.Series(lengths).hist()
        # plt.title("Distribution of document lengths in the knowledge base (in count of tokens)")
        # plt.show()

        return docs_processed_unique
