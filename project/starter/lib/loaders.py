from typing import List

try:
    import pdfplumber
except ImportError:  # pragma: no cover
    pdfplumber = None

from lib.documents import Corpus, Document


class PDFLoader:
    """Document loader for extracting text content from PDF files.

    This loader is optional. If `pdfplumber` is not installed, it will raise a
    clear error only when attempting to load a PDF.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def load(self) -> Document:
        if pdfplumber is None:
            raise ImportError(
                "pdfplumber is not installed. Install it with `pip install pdfplumber` "
                "to use PDFLoader."
            )

        corpus = Corpus()
        with pdfplumber.open(self.pdf_path) as pdf:
            for num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if text:
                    corpus.append(
                        Document(
                            id=str(num),
                            content=text
                        )
                    )
        return corpus
