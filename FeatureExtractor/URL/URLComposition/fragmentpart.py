from nltk import ngrams
import numpy as np

from collections import Counter
from math import log, e
import string


class FragmentPart:
    def __init__(self, fragment: str, url_len, *args, **kwargs):
        self.fragment = fragment

        if not fragment:
            self.frag_digit_count = 0
            self.frag_letter_count = 0
            self.frag_digit_rate = 0
            self.frag_len_ratio = 0
            self.frag_unigram_ent = 0
            self.frag_brigram_ent = 0
            self.frag_trigram_ent = 0
        else:
            self.frag_digit_count = check_digit_count(fragment)
            self.frag_letter_count = check_letter_count(fragment)
            self.frag_digit_rate = check_digit_count(fragment) / (check_letter_count(fragment) if check_letter_count(fragment) != 0 else 1)
            self.frag_len_ratio = len(fragment) / url_len
            self.frag_unigram_ent = check_unigram_entropy(fragment)
            self.frag_brigram_ent = check_bigram_entropy(fragment)
            self.frag_trigram_ent = check_trigram_entropy(fragment)

def check_letter_count(fragment: str):
    return sum([1 if c in string.ascii_letters else 0 for c in fragment])

def check_digit_count(fragment: str):
    return sum([1 if c in string.digits else 0 for c in fragment])

def check_unigram_entropy(fragment: str):
    unigrams = [c for c in fragment]
    unigram_counts = Counter(unigrams)
    labels = [count for _, count in unigram_counts.most_common()]
    return entropy(labels)

def check_trigram_entropy(fragment: str):
    bigrams = [fragment[i:i+2] for i, _ in enumerate(fragment[0:len(fragment)-2])]
    bigram_counts = Counter(bigrams)
    labels = [count for _, count in bigram_counts.most_common()]
    return entropy(labels)

def check_bigram_entropy(fragment: str):
    trigrams = [fragment[i:i+3] for i, _ in enumerate(fragment[0:len(fragment)-3])]
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
