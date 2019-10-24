from sklearn.ensemble import RandomForestClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

class RandomForest:
    def __init__(self, features, target_variable):
        self.features = features
        self.target_variable = target_variable

        # 60% training and 40% test
        self.features_train, self.features_test, self.target_train, self.target_test = train_test_split(self.features, self.target_variable, test_size=0.4, random_state=1)
        clf = RandomForestClassifier(n_estimators=100)
        self.clf = clf.fit(self.features_train, self.target_train)

    def predict(self):
        target_predictions = self.clf.predict(self.features_test)
        print(f"Accuracy: {metrics.accuracy_score(self.target_test, target_predictions)}")
        print(f"Precision: {metrics.precision_score(self.target_test, target_predictions)}")
        print(f"Recall: {metrics.recall_score(self.target_test, target_predictions)}")