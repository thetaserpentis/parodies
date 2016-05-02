import glob
import os

from nltk.tokenize import word_tokenize


class TextCorpus:
    def __init__(self, directory: str):
        self.directory = directory

    def __iter__(self):
        path = os.path.join(self.directory, '*.txt')
        for filename in glob.glob(path):
            with open(filename, 'r', encoding='utf-8') as text_file:
                yield word_tokenize(text_file.read().lower())
