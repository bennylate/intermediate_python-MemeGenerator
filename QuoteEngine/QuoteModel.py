"""QuoteModel Class Creation.

References:
https://knowledge.udacity.com/questions/643985
Project 1 class layouts in template code
"""

class QuoteModel():
    def __init__(self, body='', author=''):
        """Initiaties the object."""
        self.body = body
        self.author = author

    def __str__(self):
        """Returns a string version of the object."""
        return f'{self.body} - {self.author}'

    def __repr__(self):
        """Returns a readable version of the object."""
        return f'{self.body} - {self.author}'
