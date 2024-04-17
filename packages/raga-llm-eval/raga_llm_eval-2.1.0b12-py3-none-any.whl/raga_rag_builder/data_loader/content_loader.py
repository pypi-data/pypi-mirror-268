import os

from langchain_community.document_loaders import (CSVLoader, Docx2txtLoader,
                                                  JSONLoader, PyPDFLoader,
                                                  TextLoader,
                                                  UnstructuredEPubLoader)


class ContentLoader:
    def __init__(self, data_path):
        self.data_path = data_path
        # Define loader configurations
        self.loader_configs = {
            ".pdf": {"loader_class": PyPDFLoader, "init_args": {}, "init_kwargs": {}},
            ".docx": {
                "loader_class": Docx2txtLoader,
                "init_args": [],
                "init_kwargs": {},
            },
            ".json": {
                "loader_class": JSONLoader,
                "init_args": [],
                "init_kwargs": {"jq_schema": ".", "text_content": False},
            },
            ".csv": {"loader_class": CSVLoader, "init_args": [], "init_kwargs": {}},
            ".epub": {
                "loader_class": UnstructuredEPubLoader,
                "init_args": [],
                "init_kwargs": {},
            },
            ".txt": {
                "loader_class": TextLoader,
                "init_args": [],
                "init_kwargs": {},
            },
        }

    def get_content(self, specific_file_type=None):
        files = os.listdir(self.data_path)
        files = [
            f"{self.data_path}/{file}" for file in files if not file.startswith(".")
        ]
        results = {}

        for file_type, config in self.loader_configs.items():
            if specific_file_type and file_type != specific_file_type:
                continue  # Skip if we're only interested in a specific file type

            specific_files = [file for file in files if file.endswith(file_type)]
            if specific_files:
                content = self._load_files_content(specific_files, **config)
                results[file_type.lstrip(".")] = content

        return results

    def _load_files_content(self, files, loader_class, init_args=[], init_kwargs={}):
        content = []
        for file_name in files:
            full_path = os.path.join(self.data_path, file_name)
            loader = loader_class(full_path, *init_args, **init_kwargs)
            loaded_content = loader.load()
            content.append(loaded_content)
        return content
