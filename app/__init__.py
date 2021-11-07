from flask import Flask, app
from flask_restful import Api
from app.resources import *

# Create our flask instance and configure it :
app = Flask(__name__)
app.config.from_object("config.Myconfig")

# Create our Rest Api and add resources to it :
api = Api(app)
api.add_resource(FacialRecognition, "/face")
api.add_resource(ObjectDetection, "/object")
api.add_resource(TextRecognition, "/text")





from app import application