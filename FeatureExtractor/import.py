import csv
from pymongo import MongoClient

from URL.url import URL

url_csv_path = 'C:\\Users\\Armand Syahtama\\Dropbox\\Final Year\\Innovation Project\\project\\urls.csv'

# set up mongodb connection
client = MongoClient('localhost', 27017)
db = client['url_test']
urls = db.urls

csv_urls = []
# Open and read url csv file
with open(url_csv_path, 'r', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        csv_urls.append(row[0])

# iterate through urls, making url objects
print('setting up urls')
url_objs = [URL(u).to_json() for u in csv_urls]

# bulk save them into mongodb databases
print('inserting urls')
new_result = urls.insert_many(url_objs)
print('Multiple posts: {0}'.format(new_result))