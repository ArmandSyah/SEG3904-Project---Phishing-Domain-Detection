from sklearn.ensemble import RandomForestClassifier # Import Decision Tree Classifier

from ClassificationModels.ClassificationModel import ClassificationModel

class RandomForest(ClassificationModel):
    def __init__(self, features, target_variable):
        clf = RandomForestClassifier(n_estimators=100)
        super().__init__(features, target_variable, clf)