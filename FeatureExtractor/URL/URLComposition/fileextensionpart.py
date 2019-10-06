from nltk import ngrams
import numpy as np

from collections import Counter
from math import log, e
import string

class FileExtensionPart:
    def __init__(self, path, url_len, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fx = retrieve_file_extension(path)
        self.file_extension = fx
        self.fx_digit_count = check_digit_count(fx)
        self.fx_distinct_char_count = len(set(fx))
        self.fx_letter_count = check_letter_count(fx)
        self.fx_digit_rate = check_digit_count(fx) / check_letter_count(fx)
        self.fx_unigram_ent = check_unigram_entropy(fx)
        self.fx_brigram_ent = check_bigram_entropy(fx)
        self.fx_trigram_ent = check_trigram_entropy(fx)
        self.fx_executable = fx == 'exe'
        self.fx_len = len(fx)
        self.fx_len_ratio = len(fx) / url_len
        # self.fx_proba = ask miguel about it

def check_letter_count(fragment: str):
    return sum([1 if c in string.ascii_letters else 0 for c in fragment])

def check_digit_count(fragment: str):
    return sum([1 if c in string.digits else 0 for c in fragment])

def retrieve_file_extension(path: str):
    path_frags = path.split('/')
    file_portion = path_frags[-1]
    file_extension = file_portion.split('.')[-1]
    return file_extension

def check_unigram_entropy(file_extension: str):
    unigrams = [c for c in file_extension]
    unigram_counts = Counter(unigrams)
    labels = [count for _, count in unigram_counts.most_common()]
    return entropy(labels)

def check_trigram_entropy(file_extension: str):
    bigrams = [file_extension[i:i+2] for i, _ in enumerate(file_extension[0:len(file_extension)-1])]
    print(f'bigrams: {bigrams}')
    bigram_counts = Counter(bigrams)
    labels = [count for _, count in bigram_counts.most_common()]
    return entropy(labels)

def check_bigram_entropy(file_extension: str):
    trigrams = [file_extension[i:i+3] for i, _ in enumerate(file_extension[0:len(file_extension)-2])]
    trigram_counts = Counter(trigrams)
    labels = [count for _, count in trigram_counts.most_common()]
    return entropy(labels)

def entropy(labels, base=None):
  """ Computes entropy of label distribution. """

  n_labels = len(labels)

  if n_labels <= 1:
    return 0

  value,counts = np.unique(labels, return_counts=True)
  probs = counts / n_labels
  n_classes = np.count_nonzero(probs)

  if n_classes <= 1:
    return 0

  ent = 0.

  # Compute entropy
  base = e if base is None else base
  for i in probs:
    ent -= i * log(i, base)

  return ent