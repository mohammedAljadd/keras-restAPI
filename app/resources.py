from flask_restful import Resource
from flask import request
from app.utils import *

# The first resource is used for facial recognition
# All the useful functions are defined in utils python file to make this code readable and also
# it is very easy to use the same functions for diffrent resources.
class FacialRecognition(Resource):
    def post(self):

        if request.method == "POST":
            if request.files:

                # receive and save the image
                image = save_image(request)

                # facial recogntion
                prediction = facial_recognition(image)

        # return result
        return prediction





class ObjectDetection(Resource):
    def post(self, image=0):
        return {"data": "objectdetection function"}

class TextRecognition(Resource):
    def post(self, image=0):
        return {"data": "textrecognition function"}



class Test(Resource):
    def post(self):
        return {
        "data": "Flask is working"
        }