import random
from collections import defaultdict, Counter
from table import ProbabilityTable
from corpus import TextCorpus


class ParodyGenerator:
    STOP_WORD = 'STOP_WORD'
    STOP_SENTENCE = {'!', '?', '.', '...'}

    def __init__(self, table=None):
        self.table = table

    def build(self, corpus: TextCorpus):
        word1 = self.STOP_WORD
        word2 = self.STOP_WORD

        table = defaultdict(Counter)

        for text in corpus:
            for word in text:
                table[word1, word2][word] += 1
                word1, word2 = word2, word

        table[word1, word2][self.STOP_WORD] += 1

        self.table = {words: ProbabilityTable(counts)
                      for words, counts in table.items()}

    def generate(self, max_sentences=7):
        word1 = self.STOP_WORD
        word2 = self.STOP_WORD

        sentence_count = 0
        sentence = []

        while sentence_count < max_sentences:
            new_word = self._get_next_word(word1, word2)
            if new_word == self.STOP_WORD:
                return

            sentence.append(new_word)
            if new_word in self.STOP_SENTENCE:
                yield ' '.join(sentence)
                sentence_count += 1
                sentence = []

            word1, word2 = word2, new_word

    def _get_next_word(self, *words):
        return self.table[words][random.uniform(0, 1)]
