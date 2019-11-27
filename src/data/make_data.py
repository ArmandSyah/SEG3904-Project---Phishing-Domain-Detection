import csv
import json
import os

from collections import Counter
from urllib.parse import urlparse

base = os.path.abspath(os.path.join(__file__, "../../.."))

def retrieve_file_extension(path: str):
    path_frags = path.split('/')
    file_portion = path_frags[-1]
    if not '.' in file_portion:
        return None
    else:
        file_extension = file_portion.split('.')[-1]
        return file_extension

def setup_probabilities(): 

    phish_url_data = os.path.join(base, 'Datasets\\external\\retrieved_phish_urls.txt')
    legit_url_data = os.path.join(base, 'Datasets\\external\\Benign_list_big_final.csv')

    total = 0
    file_extension_counts = Counter({'none': 0})

    with open(phish_url_data, 'r', encoding='utf8') as phish_file:
        for line in phish_file:
            url = urlparse(line)
            possible_path = retrieve_file_extension(url.path)
            if possible_path is None:
                file_extension_counts['none'] += 1
            else:
                if possible_path in file_extension_counts:
                    file_extension_counts[possible_path] += 1
                else:
                    file_extension_counts[possible_path] = 1
            total += 1

    with open(legit_url_data, 'r', encoding="utf8") as legit_file:
        csvreader = csv.reader(legit_file)

        for row in csvreader:
            url = urlparse(row[0])
            possible_path = retrieve_file_extension(url.path)
            if possible_path is None:
                file_extension_counts['none'] += 1
            else:
                if possible_path in file_extension_counts:
                    file_extension_counts[possible_path] += 1
                else:
                    file_extension_counts[possible_path] = 1
            total += 1

    probability_dict = dict()
    for key, value in file_extension_counts.items():
        probability_dict[key] = value / total

    with open(os.path.join(base, 'Datasets\\file_probabilities.json'), 'w') as fp:
        json.dump(probability_dict, fp)
    

if __name__ == "__main__":
    setup_probabilities()