import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import KFold, train_test_split
from sklearn import metrics
from src.features.url import URL


# Import train_test_split function
# Import scikit-learn metrics module for accuracy calculation


class ClassificationModel:
    def __init__(self, features, feature_columns, target_variables, classifier):
        self.features = features
        self.feature_columns = feature_columns
        self.target_variable = target_variables

        selector = SelectKBest(chi2, k=30)
        selector.fit(self.features, self.target_variable)

        cols = selector.get_support(indices=True)
        self.features = self.features.iloc[:, cols]
        self.feature_columns = [self.feature_columns[c] for c in cols]

        print(f'selected features: {feature_columns}')

        self.features_train, self.features_test, self.target_train, self.target_test = train_test_split(
            self.features, self.target_variable, test_size=.4, random_state=42)
        self.clf = classifier.fit(self.features_train, self.target_train)

    def predict_test_set(self):
        target_predictions = self.clf.predict(self.features_test)
        feature_predictions = self.clf.predict(self.features_train)
        print(
            f"Train Accuracy: {metrics.accuracy_score(self.target_train, feature_predictions)}")
        print(
            f"Train Precision: {metrics.precision_score(self.target_train, feature_predictions)}")
        print(
            f"Train Recall: {metrics.recall_score(self.target_train, feature_predictions)}")
        print(
            f"Test Accuracy: {metrics.accuracy_score(self.target_test, target_predictions)}")
        print(
            f"Test Precision: {metrics.precision_score(self.target_test, target_predictions)}")
        print(
            f"Test Recall: {metrics.recall_score(self.target_test, target_predictions)}")
        print(
            f"\nTrain Confusion Matrix: \n {metrics.confusion_matrix(self.target_train, feature_predictions)}")
        print(
            f"\nTest Confusion Matrix: \n {metrics.confusion_matrix(self.target_test, target_predictions)}")
        print(
            f"\nTrain Label Count Actual:\n{self.target_train.value_counts()}")
        print(f"\nTest Label Count Actual:\n{self.target_test.value_counts()}")

    def predict_url(self, url: str):
        u = URL(url).to_json()
        url_df = pd.DataFrame.from_records([u])
        url_df['http'] = 1 if url_df.iloc[0]['protocol'] == 'http' else 0
        url_df['https'] = 1 if url_df.iloc[0]['protocol'] == 'https' else 0
        url_features = url_df[self.feature_columns]
        target_prediction = self.clf.predict(url_features)
        class_probabilities = self.clf.predict_proba(url_features)
        print(f'Predictions for {url}: {target_prediction[0]}')
        return (u, target_prediction[0], np.max(class_probabilities))

    def fit_classifier(self, url: str, label):
        u = URL(url).to_json()
        url_df = pd.DataFrame.from_records([u])
        url_df['http'] = 1 if url_df.iloc[0]['protocol'] == 'http' else 0
        url_df['https'] = 1 if url_df.iloc[0]['protocol'] == 'https' else 0
        url_features = url_df[self.feature_columns]
        self.clf.fit(url_features, [label])
