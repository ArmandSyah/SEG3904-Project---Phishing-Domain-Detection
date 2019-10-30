import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

from FeatureExtractor.URL.url import URL

class ClassificationModel:
    def __init__(self, features, feature_columns, target_variables, classifier):
        self.features = features
        self.feature_columns = feature_columns
        self.target_variable = target_variables

        self.features_train, self.features_test, self.target_train, self.target_test = train_test_split(self.features, self.target_variable, test_size=0.4, random_state=1)
        self.clf = classifier.fit(self.features_train, self.target_train)

    def predict_test_set(self):
        target_predictions = self.clf.predict(self.features_test)
        print(f"Accuracy: {metrics.accuracy_score(self.target_test, target_predictions)}")
        print(f"Precision: {metrics.precision_score(self.target_test, target_predictions)}")
        print(f"Recall: {metrics.recall_score(self.target_test, target_predictions)}")

    def predict_url(self, url):
        u = URL(url).to_json()
        url_df = pd.DataFrame.from_records([u])
        url_df['http'] = 1 if url_df.iloc[0]['protocol'] == 'http' else 0
        url_df['https'] = 1 if url_df.iloc[0]['protocol'] == 'https' else 0
        url_features = url_df[self.feature_columns]
        target_prediction = self.clf.predict(url_features)
        class_probabilities = self.clf.predict_proba(url_features)
        return (u, target_prediction[0], np.max(class_probabilities))