from sklearn.naive_bayes import GaussianNB

from ClassificationModel import ClassificationModel


class NaiveBayes(ClassificationModel):
    def __init__(self, features, feature_columns, target_variable):
        clf = GaussianNB()
        super().__init__(features, feature_columns, target_variable, clf)
