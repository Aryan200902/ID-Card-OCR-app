from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
def create_app():
    app = Flask(__name__, template_folder='templates')
    CORS(app)
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/Ocr_app'
    mongo = PyMongo(app)
    
    return app, mongo

app, mongo = create_app()
