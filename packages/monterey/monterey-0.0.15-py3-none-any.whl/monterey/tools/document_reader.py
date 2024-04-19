import os
from typing import Optional, List, Tuple
from PyPDF2 import PdfReader
from ebooklib import epub

class DocumentReader:
    def __init__(self):
        """
        A class that reads through a document or a directory of documents, and returns the content of the document(s).

        Example:
        ```python
        from yosemite.data.document_reader import DocumentReader
        doc = DocumentReader()
        content = doc.read("path/to/file.txt")
        ```

        Attributes:
            path: The path to the document or directory.
        """
        self.path = None

    def read(self, path: str = None) -> Optional[str]:
        """
        Reads the content of a document or a directory of documents.

        Example:
        ```python
        from yosemite.data.document_reader import DocumentReader
        doc = DocumentReader()
        content = doc.read("path/to/file.txt")
        ```

        Args:
            path (str): The path to the document or directory.

        Returns:
            str: The content of the document(s).
        """
        if path is None:
            raise ValueError("Path is required.")
        else:
            self.path = path

        if os.path.isfile(self.path):
            return self._read_file(self.path)
        elif os.path.isdir(self.path):
            return self._read_directory(self.path)
        else:
            raise FileNotFoundError(f"Path {self.path} does not exist.")

    def _read_file(self, file_path: str) -> str:
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
        elif file_path.endswith(".pdf"):
            with open(file_path, "rb") as file:
                reader = PdfReader(file)
                content = " ".join(page.extract_text() for page in reader.pages)
        elif file_path.endswith(".epub"):
            book = epub.read_epub(file_path)
            content = " ".join(item.get_content().decode("utf-8") for item in book.get_items_of_type(9))
        else:
            raise ValueError(f"Unsupported file format: {file_path}")
        return content

    def _read_directory(self, directory: str) -> List[Tuple[str, str]]:
        file_contents = []
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                try:
                    content = self._read_file(file_path)
                    file_contents.append((file_name, content))
                except ValueError as e:
                    print(f"Skipping file {file_name}: {str(e)}")
        return file_contents