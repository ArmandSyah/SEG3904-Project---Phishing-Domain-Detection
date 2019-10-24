from sklearn.naive_bayes import GaussianNB

from ClassificationModels.ClassificationModel import ClassificationModel

class NaiveBayes(ClassificationModel):
    def __init__(self, features, target_variable):
        clf = GaussianNB()
        super().__init__(features, target_variable, clf)