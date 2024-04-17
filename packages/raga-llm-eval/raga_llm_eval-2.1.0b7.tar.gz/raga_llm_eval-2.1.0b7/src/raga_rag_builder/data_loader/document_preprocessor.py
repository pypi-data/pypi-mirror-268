from langchain.text_splitter import RecursiveCharacterTextSplitter

# We use a hierarchical list of separators specifically tailored for splitting Markdown documents
# This list is taken from LangChain's MarkdownTextSplitter class.
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


class DocumentPreprocessor:
    def __init__(self, docs, chunk_size=512):
        self.raw_docs = docs
        self.chunk_size = chunk_size

    def split_text(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # the maximum number of characters in a chunk: we selected this value arbitrarily
            chunk_overlap=100,  # the number of characters to overlap between chunks
            add_start_index=True,  # If `True`, includes chunk's start index in metadata
            strip_whitespace=True,  # If `True`, strips whitespace from the start and end of every document
            # separators=MARKDOWN_SEPARATORS,
        )

        docs_processed = []
        for doc in self.raw_docs:
            docs_processed += text_splitter.split_documents([doc])

        return docs_processed
