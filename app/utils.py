def save_image(request):
    image = request.files["image"]
    txt = request.files["type"]
    with open(txt) as f:
        lines = f.readlines()
    from app import app
    image_path = app.config["IMAGE_FOLDER"]+"/"+image.filename
    image.save(image_path)
    return image


def facial_recognition(image):
    from keras.models import load_model
    from PIL import Image, ImageOps
    import numpy as np
    from app import app
    model = load_model(app.config["MODEL_FOLDER"]+'keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = round(model.predict(data)[0][0])
    return prediction
                