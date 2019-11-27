import os
import pickle
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_restful import Api, Resource, reqparse
from src.features.url import URL

base = os.path.abspath(os.path.join(__file__, "../../.."))


class Predict(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url')

    def __init__(self, **kwargs):
        self.classification_model = kwargs['classification_model']
        self.mongo = kwargs['mongo']

    def post(self):
        args = Predict.parser.parse_args()
        url = args['url']
        print(f'url: {url}')
        (u, predicted_result, confidence_score) = self.classification_model.predict_url(url)
        u['is_legit'] = int(predicted_result)
        u['confidence_score'] = confidence_score
        self.mongo.db.url.insert(u)
        return jsonify({'url': url, 'predicted result': 'legit' if predicted_result == 1 else 'phish', 'confidence_score': confidence_score})


class PredictList(Resource):
    def __init__(self, **kwargs):
        self.mongo = kwargs['mongo']

    def delete(self):
        self.mongo.db.url.delete_many({})
        return 'Delete Successful', 201


with open(os.path.join(base, 'models\\random_forest.pkl'), 'rb') as rf_pickle:
    rf = pickle.load(rf_pickle)

APP = Flask(__name__)
APP.config['MONGO_URI'] = 'mongodb://localhost:27017/incoming_urls_db'
APP.secret_key = os.environ.get('SECRET_KEY') or 'default'
mongo = PyMongo(APP)
API = Api(APP)

API.add_resource(Predict, '/predict',
                 resource_class_kwargs={'classification_model': rf, 'mongo': mongo})
API.add_resource(PredictList, '/predictList',
                 resource_class_kwargs={'mongo': mongo})

if __name__ == '__main__':
    APP.run(port=5000)
