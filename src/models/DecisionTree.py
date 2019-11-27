from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier

from ClassificationModel import ClassificationModel


class DecisionTree(ClassificationModel):
    def __init__(self, features, feature_columns, target_variable):
        clf = DecisionTreeClassifier()
        super().__init__(features, feature_columns, target_variable, clf)
