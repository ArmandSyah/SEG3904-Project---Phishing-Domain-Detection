from flask import jsonify
from flask_restful import Resource, reqparse

class Predict(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url')

    def __init__(self, **kwargs):
        self.classification_model = kwargs['classification_model']
        self.mongo = kwargs['mongo']

    def post(self):
        args = Predict.parser.parse_args()
        url = args['url']
        (u, predicted_result, confidence_score) = self.classification_model.predict_url(url)
        u['is_legit'] = int(predicted_result)
        u['confidence_score'] = confidence_score
        self.mongo.db.url.insert(u)
        return jsonify({'url': url, 'predicted result': 'legit' if predicted_result == 1 else 'phish', 'confidence_score': confidence_score})