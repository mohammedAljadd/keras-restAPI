from flask_restful import Resource
from flask import request

# The first resource is used for facial recognition
class FacialRecognition(Resource):
    def post(self):

        if request.method == "POST":
            if request.files:
                
                # receive and save the image
                image = request.files["image"]
                from app import app
                image_path = app.config["IMAGE_FOLDER"]+"/"+image.filename
                image.save(image_path)

                # facial recogntion
                from keras.models import load_model
                from PIL import Image, ImageOps
                import numpy as np
                model = load_model(app.config["MODEL_FOLDER"]+'keras_model.h5')
                data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
                image = Image.open(image)
                size = (224, 224)
                image = ImageOps.fit(image, size, Image.ANTIALIAS)
                image_array = np.asarray(image)
                normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
                data[0] = normalized_image_array
                prediction = model.predict(data)

        # return result
        return {"data": f"{prediction}"}



class ObjectDetection(Resource):
    def post(self, image=0):
        return {"data": "objectdetection function"}

class TextRecognition(Resource):
    def post(self, image=0):
        return {"data": "textrecognition function"}