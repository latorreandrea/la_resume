import os
from flask import Flask
# import blueprint
from blueprints.home.home import home_bp

app = Flask(__name__)

# --------------------- #
#    Flask Blueprint    #
# --------------------- #
app.register_blueprint(home_bp)
#app.register_blueprint



# execute app
if __name__ == "__main__":
    app.run(
        debug=True
    )