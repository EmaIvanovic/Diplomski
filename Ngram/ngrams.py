import pprint
import random
from nltk.corpus import brown
import nltk
import datetime

FILEPATH = "C:\\Users\\emilija.ivanovic\\Desktop\Diplomski\\tekstovi\\stara-grcka.txt"
NGRAM_LENGTH = 12


class MarkovChain:
    def __init__(self):
        self.model = []

    def learn(self, tokens, n):
        self.model = [tuple(tokens[i:(i + n)]) for i in range(0, len(tokens) - n + 1)]

    def learn_from_file(self, path, length):
        with open(path, 'r') as f:
            text = f.read()
            tokens = text.split(" ")
            self.learn(tokens, length)

    def estimate_probabilities(self):
        for ngram in self.model:
            
if __name__ == '__main__':
    m = MarkovChain()
    m.learn_from_file(FILEPATH, NGRAM_LENGTH)
    print(str(len(m.model)))

