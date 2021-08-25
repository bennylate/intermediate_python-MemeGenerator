"""This ingestor parses DOCX files for quote verbiage.

References:
https://knowledge.udacity.com/questions/596498
https://knowledge.udacity.com/questions/591224
https://knowledge.udacity.com/questions/441856

"""
from docx import Document
from typing import List
from .QuoteModel import QuoteModel
from .ingestor_interface import IngestorInterface
import pandas


class DOCXIngestor(IngestorInterface):
    """Separate strategy object realizing IngestorInterface for DOCX."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse DOCX file for quotes."""
        if not cls.can_ingest(path):
            raise Exception('DOCX File ingestion error')

        try:
            quotes = []
            doc = docx.Document(path)
            for paragraph in doc.paragraphs:
                if paragraph.text != "":
                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)

        except Exception as e:
            raise Exception("DOCX File ingestion error")

        return quotes
