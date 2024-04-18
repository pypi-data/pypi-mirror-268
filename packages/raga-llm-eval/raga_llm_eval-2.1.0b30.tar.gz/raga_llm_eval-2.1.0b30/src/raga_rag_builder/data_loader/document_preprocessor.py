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
    def __init__(
        self,
        docs,
        chunk_size=512,
        overlap=100,
        add_start_index=True,
        strip_whitespace=True,
    ):
        self.raw_docs = docs
        self.chunk_size = chunk_size
        self.chunk_overlap = overlap
        self.add_start_index = add_start_index
        self.strip_whitespace = strip_whitespace

    def split_text(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            add_start_index=self.add_start_index,
            strip_whitespace=self.strip_whitespace,
            separators=MARKDOWN_SEPARATORS,
        )

        docs_processed = []
        for doc in self.raw_docs:
            docs_processed += text_splitter.split_documents([doc])

        return docs_processed
