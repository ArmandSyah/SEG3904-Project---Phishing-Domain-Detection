import os
import pickle
from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

from API.predict_url import Predict

with open('BuiltModels\\random_forest.pkl', 'rb') as rf_pickle:
    rf = pickle.load(rf_pickle)

APP = Flask(__name__)
APP.config['MONGO_URI'] = 'mongodb://localhost:27017/incoming_urls_db'
APP.secret_key = os.environ.get('SECRET_KEY') or 'default'
mongo = PyMongo(APP)
API = Api(APP)

API.add_resource(Predict, '/predict', resource_class_kwargs={'classification_model': rf, 'mongo': mongo})

if __name__ == '__main__':
    APP.run(port=5000)