import numpy as np


class Tokenizer:
    def __init__(self, num_words=None):
        self.num_words = num_words
        self.word_index = {}
        self.filters = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'

    def fit_on_texts(self, texts):
        from collections import Counter

        counts = Counter()
        for text in texts:
            counts.update(self._tokens(text))
        limit = None if not self.num_words else self.num_words - 1
        words = [word for word, _ in counts.most_common(limit)]
        self.word_index = {word: index + 1 for index, word in enumerate(words)}

    def texts_to_sequences(self, texts):
        return [
            [self.word_index[token] for token in self._tokens(text) if token in self.word_index]
            for text in texts
        ]

    def _tokens(self, text):
        for char in self.filters:
            text = text.replace(char, " ")
        return text.lower().split()


def pad_sequences(sequences, maxlen):
    padded = np.zeros((len(sequences), maxlen), dtype="int32")
    for index, sequence in enumerate(sequences):
        if not sequence:
            continue
        trimmed = sequence[-maxlen:]
        padded[index, -len(trimmed) :] = trimmed
    return padded


def _demo():
    tokenizer = Tokenizer(num_words=3)
    tokenizer.fit_on_texts(["Hello world", "hello there"])
    padded = pad_sequences(tokenizer.texts_to_sequences(["hello world there"]), maxlen=4)
    assert padded.shape == (1, 4)
    assert list(padded[0]) == [0, 0, 1, 2]


if __name__ == "__main__":
    _demo()
