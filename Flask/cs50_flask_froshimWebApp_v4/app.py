from crypt import methods
import sqlite3
from flask import (
    Flask,
    render_template,
    request,
    redirect
)

# __name__ represent the current file
# the above line basically tells python
# to turn the current file into a Flask application 
app = Flask(__name__)

# store data into db
db = sqlite3.connect("./froshims.db", check_same_thread=False)


# create a global variable
SPORTS = [
    "Basketball",
    "Soccer",
    "Diving",
    "Scuba",
    "Bumpgee Jump"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    # Validate name
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")

    # Validate sport
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    # Remember registrant
    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))

    # Confirm registration
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)

# Seems good but can you see the problem?
# the code above actually store info in your memory
# once you close the website, all the data lost!
# sure you can store data into csv file,
# an better option is stored everything in database   