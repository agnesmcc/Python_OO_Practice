"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    A WordFinder finds random words from a dictionary.
    """
    def __init__(self, filename):
        self.filename = filename
        self.lines = []
        self.read_file()


    def read_file(self):
        with open(self.filename, 'r') as f:
            self.lines = f.readlines()

    def random(self):
        return random.choice(self.lines).strip()


class SpecialWordFinder(WordFinder):
    """
    SpecialWordFinder ignores empty lines and comments.
    """
    def __init__(self, filename):
        super().__init__(filename)

    def random(self):
        word = ""
        while word.startswith('#') or word == "":
            word = random.choice(self.lines).strip()
        return word
