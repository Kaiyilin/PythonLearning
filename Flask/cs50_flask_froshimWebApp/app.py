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

# create a global variable
SPORTS = [
    "Basketball",
    "Soccer",
    "Diving",
    "Scuba",
    "Bumpgee Jump"
]

# notice that we name the function index for convention
# in fact you can always named the function in your way
# it's a function that will be called when you get to / route
@app.route("/") # define a route for / 
def index():
    return render_template("index.html", sports=SPORTS)

# since you'd like to get info from users,
# you must assumed that the users might go wrong 
@app.route("/register", methods=["POST"])
def register():

    
    # Validate submission
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")

    # Confirm submission
    return render_template("success.html")
    