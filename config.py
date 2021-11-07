class Myconfig(object):
    
    from app import app
    import os
    
    # Do not use debut mode in production!
    DEBUG = True
    MODEL_FOLDER = os.path.join(app.root_path)+"/static/model/"
    IMAGE_FOLDER = os.path.join(app.root_path)+"/static/image/"