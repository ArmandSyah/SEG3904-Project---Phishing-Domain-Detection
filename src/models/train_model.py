import csv
from pymongo import MongoClient
import os
import json

import pandas as pd
import pickle

from DecisionTree import DecisionTree
from RandomForest import RandomForest
from NaiveBayes import NaiveBayes

base = os.path.abspath(os.path.join(__file__, "../../.."))

# Set up MongoDB connection
client = MongoClient('localhost', 27017)
db = client['url_training_data']
urls = db.urls

df = pd.DataFrame(list(urls.find()))

df = df.sample(frac=1)  # shuffle the rows

one_hot_protocol = pd.get_dummies(df['protocol'], columns=['protocol'])
df = pd.concat([df, one_hot_protocol], axis=1)
feature_columns = list(df.columns)
feature_columns.remove('is_legit')
feature_columns.remove('_id')
feature_columns.remove('protocol')
feature_columns.remove('url')
feature_columns.remove('domain')
feature_columns.remove('path')
feature_columns.remove('query')
feature_columns.remove('fragment')
feature_columns.remove('file_extension')

features = df[feature_columns]
target_variable = df.is_legit

print('\nDecsion Tree Results:')
dt = DecisionTree(features, feature_columns, target_variable)
dt.predict_test_set()
dt.predict_url(
    'https://www.reddit.com/r/Games/comments/dmgu22/sources_the_last_of_us_2_delayed_to_spring/')
dt.predict_url(
    'https://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-dataframe')

print('\nRandom Forest Results:')
rf = RandomForest(features, feature_columns, target_variable)
rf.predict_test_set()
rf.predict_url(
    'https://www.reddit.com/r/Games/comments/dmgu22/sources_the_last_of_us_2_delayed_to_spring/')
rf.predict_url(
    'https://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-dataframe')

print('\nNaive Bayes Results:')
nb = NaiveBayes(features, feature_columns, target_variable)
nb.predict_test_set()
nb.predict_url(
    'https://www.reddit.com/r/Games/comments/dmgu22/sources_the_last_of_us_2_delayed_to_spring/')
nb.predict_url(
    'https://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-dataframe')

print('Pickling decision tree')
with open(os.path.join(base, 'models\\decion_tree.pkl'), 'wb') as decision_tree_output:
    pickle.dump(dt, decision_tree_output, pickle.HIGHEST_PROTOCOL)

print('Pickling random forest')
with open(os.path.join(base, 'models\\random_forest.pkl'), 'wb') as random_forest_output:
    pickle.dump(rf, random_forest_output, pickle.HIGHEST_PROTOCOL)

print('Pickling naive bayes')
with open(os.path.join(base, 'models\\naive_bayes.pkl'), 'wb') as naive_bayes_output:
    pickle.dump(nb, naive_bayes_output, pickle.HIGHEST_PROTOCOL)

# Disconnect from MongoDB
client.close()
