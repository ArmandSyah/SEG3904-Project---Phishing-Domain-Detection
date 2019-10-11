import csv
from pymongo import MongoClient
import os

from FeatureExtractor.URL.url import URL

dirname = os.getcwd()

phish_url_data = os.path.join(dirname, 'Datasets\\retrieved_phish_urls.txt')
legit_url_data = os.path.join(dirname, 'Datasets\\Benign_list_big_final.csv')

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

# iterate through urls, making url objects
print('setting up urls')
url_objs = [URL(u, 0).to_json() for u in phish_urls[:1000]] + [URL(u, 1).to_json() for u in legit_urls[:1000]]

# bulk save them into mongodb databases
print('inserting urls')
new_result = urls.insert_many(url_objs)
print(f'Number of inserts: {len(new_result.inserted_ids)}')

# Disconnect from MongoDB
client.close()