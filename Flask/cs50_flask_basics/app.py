from crypt import methods
from flask import (
    Flask,
    render_template,
    request
)

# __name__ represent the current file
# the above line basically tells python
# to turn the current file into a Flask application 
app = Flask(__name__)

@app.route("/") # define a route for / 
def index():
    # name = request.args.get("name")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    #name = request.args.get("name", default="world") # if someone visit /greet directly, it'll see Hello world directly
    return render_template(
        "greet.html",
        name=request.args.get("name", default="world"))