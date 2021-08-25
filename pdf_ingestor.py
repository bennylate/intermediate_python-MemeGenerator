"""This ingestor parses PDF files for quote verbiage.

References:
https://knowledge.udacity.com/questions/572306
https://knowledge.udacity.com/questions/562654
https://knowledge.udacity.com/questions/633566
https://knowledge.udacity.com/questions/632977
https://classroom.udacity.com/nanodegrees/nd303-ent/parts/651c7c4b-d7aa-4c62-84b5-55dfd7e722cd/modules/9d895a88-2cc2-4c0c-897e-48c34865f236/lessons/23d0e4df-ccfd-48c5-bd39-eeab5cc54ba3/concepts/9f0f990d-2ea5-4880-b3b9-e39a3e5c4587

"""
from typing import List
from .QuoteModel import QuoteModel
from .ingestor_interface import IngestorInterface
import subprocess
import random
import os


class PDFIngestor(IngestorInterface):
    """Separate strategy object realizing IngestorInterface for PDF."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF file for quotes."""
        if not cls.can_ingest(path):
            raise Exception('PDF File ingestion error')
        
        quotes = []
	
        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])
        infile = open(tmp, "r")
        for line in infile.readlines():
            line = line.strip('\n\r').strip()
            body, author = line.split('-')
            quote = QuoteModel(body, author)
            quotes.append(quote)

        infile.close()
        os.remove(tmp)

        return quotes
