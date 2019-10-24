from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier

from ClassificationModels.ClassificationModel import ClassificationModel

class DecisionTree(ClassificationModel):
    def __init__(self, features, target_variable):
        clf = DecisionTreeClassifier()
        super().__init__(features, target_variable, clf)