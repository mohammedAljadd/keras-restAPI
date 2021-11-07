class Myconfig(object):
    from app import app
    import os
    DEBUG = True
    MODEL_FOLDER = os.path.join(app.root_path)+"/static/model/"
    IMAGE_FOLDER = os.path.join(app.root_path)+"/static/image/"