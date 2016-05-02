from collections import namedtuple, Counter


def get_frequencies(counter):
    count_sum = sum(counter.values())
    return {word: count / count_sum for word, count in counter.items()}


def get_probabilities(frequencies):
    upper_bound = 0
    probabilities = []
    for word, frequency in frequencies.items():
        upper_bound += frequency
        probabilities.append(Element(word, upper_bound))
    return probabilities


Element = namedtuple('Element', ['item', 'upper_bound'])


class ProbabilityTable:
    def __init__(self, counts: Counter):
        self._probabilities = get_probabilities(get_frequencies(counts))

    def __getitem__(self, probability: float):
        first = 0
        last = len(self._probabilities) - 1

        while first <= last:
            mid = (first + last) // 2
            if mid == 0:
                return self._probabilities[0].item
            elif self._probabilities[mid].upper_bound < probability:
                if probability <= self._probabilities[mid + 1].upper_bound:
                    return self._probabilities[mid + 1].item
                first = mid
            elif self._probabilities[mid - 1].upper_bound < probability:
                return self._probabilities[mid].item
            else:
                last = mid
