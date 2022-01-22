from flask import (
    Flask,
    request
)

"""When Flask receives a request from a client,
it needs to make a few objects available to the view function that will handle it.

A good example is request object, which encapsulates the HTTP request sent by the client

Flask context globals

current_app
g
request
session
"""

app = Flask(__name__)

@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    return "<p> Your browser is {}</p>".format(user_agent)