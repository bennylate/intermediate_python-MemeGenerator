"""This ingestor parses TXT files for quote verbiage.

References:
https://knowledge.udacity.com/questions/596498
https://knowledge.udacity.com/questions/591224
https://knowledge.udacity.com/questions/441856
https://knowledge.udacity.com/questions/442120
https://www.w3schools.com/python/ref_string_split.asp

"""
from typing import List
from .QuoteModel import QuoteModel
from .ingestor_interface import IngestorInterface

class TXTIngestor(IngestorInterface):
    """Separate strategy object realizing IngestorInterface for TXT."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse TXT file for quotes."""
        if not cls.can_ingest(path):
            raise Exception('TXT File ingestion error')
        
        quotes = []

        try:
            with open(path, "r", encoding="utf-8-sig") as f:
                for line in f.readlines():
                    line = line.strip("\n\r").strip()
                    body, author = line.split(" - ")
                    quotes.append(QuoteModel(f"'{body}'", author))

       	except:
               raise Exception("TXT File ingestion error")

        return quotes
