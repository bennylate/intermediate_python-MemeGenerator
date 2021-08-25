"""This ingestor parses CSV files for quote verbiage.

References:
Added Try/Catch blocks per instructions
https://www.w3schools.com/python/python_try_except.asp
https://knowledge.udacity.com/questions/596498
https://knowledge.udacity.com/questions/591224
https://knowledge.udacity.com/questions/441856

"""
from typing import List
from .QuoteModel import QuoteModel
from .ingestor_interface import IngestorInterface
import pandas


class CSVIngestor(IngestorInterface):
    """Separate strategy object realizing IngestorInterface for CSV."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV file for quotes."""
        if not cls.can_ingest(path):
            raise Exception('CSV File ingestion error')
        try:
            quotes = []
            data = pandas.read_csv(path, header=0)
            for index, row in data.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                
        except:
            raise Exception("CSV File ingestion error")

        return quotes
