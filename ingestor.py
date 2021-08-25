"""Final Ingestor Class.

A final Ingestor class should realize the IngestorInterface abstract 
base class and encapsulate your helper classes.

References:
https://knowledge.udacity.com/questions/559464

"""
from typing import List
from .QuoteModel import QuoteModel
from .ingestor_interface import IngestorInterface
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DOCXIngestor
from .pdf_ingestor import PDFIngestor
from .text_ingestor import TXTIngestor

class Ingestor(IngestorInterface):
    """Class encapsulating each helper class."""

    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Pasre paths(files) by appropriate ingestor."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
                