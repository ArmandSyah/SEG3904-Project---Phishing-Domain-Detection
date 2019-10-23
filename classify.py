import pandas as pd
from pymongo import MongoClient
from ClassificationModels.DecisionTree import DecisionTree

# Set up MongoDB connection
client = MongoClient('localhost', 27017)
db = client['url_training_data']
urls = db.urls

df = pd.DataFrame(list(urls.find()))

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

import pprint
pprint.pprint(df)

features = df[feature_columns]
target_variable = df.is_legit

dt = DecisionTree(features, target_variable)
dt.predict()

