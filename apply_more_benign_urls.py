import csv
import os
import pickle

with open('BuiltModels\\random_forest.pkl', 'rb') as rf_pickle:
    rf = pickle.load(rf_pickle)

dirname = os.getcwd()

legit_url_data = os.path.join(dirname, 'Datasets\\urldata.csv')

print('Start')

with open(legit_url_data, 'r', encoding="utf8") as legit_file:
    csvreader = csv.reader(legit_file)
    next(csvreader, None)

    data_list = list(csvreader)
    for row in data_list[:5000]:
        rf.fit_classifier(row[1], 1)

print('Complete')