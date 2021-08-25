"""Defines common function/methods to be used by ingestors.

The IngestorInterface defines the common functionalities (methods)
that need to be implemented by the Interface classes. The purpose of the Interface
is to define the common methods without the logic i.e. they don't have body of the
function.

References:
https://knowledge.udacity.com/questions/441018
https://knowledge.udacity.com/questions/440965
"""

from typing import List
from abc import abstractmethod
from .QuoteModel import QuoteModel

class IngestorInterface:
    """Abstract Base Class."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check against allowed extensions."""
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Method to parse a path."""
        pass
