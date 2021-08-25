"""File to declare the 'regular package' module.

Access to modules without making paths over and over.
Reference for more info:
https://stackoverflow.com/questions/448271/what-is-init-py-for
https://knowledge.udacity.com/questions/561609
https://knowledge.udacity.com/questions/518614
"""
from .QuoteModel import QuoteModel
from .ingestor import Ingestor
from .ingestor_interface import IngestorInterface
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DOCXIngestor
from .pdf_ingestor import PDFIngestor
from .text_ingestor import TXTIngestor

