from flask_restful import Resource

class FacialRecognition(Resource):
    def post(self, image=0):
        return {"data": "facialrecogntion function"}

class ObjectDetection(Resource):
    def post(self, image=0):
        return {"data": "objectdetection function"}

class TextRecognition(Resource):
    def post(self, image=0):
        return {"data": "textrecognition function"}