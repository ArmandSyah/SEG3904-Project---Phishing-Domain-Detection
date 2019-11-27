from pymongo import MongoClient
from url import URL

import csv
import os
import json

base = os.path.abspath(os.path.join(__file__, "../../.."))

phish_url_data = os.path.join(
    base, 'Datasets\\external\\retrieved_phish_urls.txt')
legit_url_data = os.path.join(
    base, 'Datasets\\external\\Benign_list_big_final.csv')
more_legit_url_data = os.path.join(base, 'Datasets\\external\\urldata.csv')

# Set up MongoDB connection
client = MongoClient('localhost', 27017)
db = client['url_training_data']
urls = db.urls

phish_urls = []
with open(phish_url_data, 'r', encoding='utf8') as phish_file:
    phish_urls = phish_file.readlines()

phish_urls = [url.strip() for url in phish_urls]

legit_urls = []
with open(legit_url_data, 'r', encoding="utf8") as legit_file:
    csvreader = csv.reader(legit_file)

    for row in csvreader:
        legit_urls.append(row[0])

with open(more_legit_url_data, 'r', encoding='utf8') as more_legit_file:
    csvreader = csv.reader(more_legit_file)

    data_list = list(csvreader)
    for row in data_list[:50000]:
        legit_urls.append(row[1])

num_legit_urls = len(legit_urls)
num_phish_urls = len(phish_urls) if len(
    phish_urls) <= len(legit_urls) else len(legit_urls)

print(f'num legit: {num_legit_urls}')
print(f'num phish: {num_phish_urls}')

# iterate through urls, making url objects
print('setting up urls')
url_objs = [URL(u, 0).to_json() for u in phish_urls[:num_phish_urls]] + \
    [URL(u, 1).to_json() for u in legit_urls[:num_legit_urls]]

# bulk save them into mongodb databases
print('inserting urls')
new_result = urls.insert_many(url_objs)
print(f'Number of inserts: {len(new_result.inserted_ids)}')

# Disconnect from MongoDB
client.close()
