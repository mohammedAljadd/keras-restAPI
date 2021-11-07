# From app package import app (flask instance)
# The folder app is treated as a package because we put the python file __init__ in it. (init init hahaha)

from app import app

if __name__ == "__main__":
    app.run()
