from flask import Flask 
# __name__ is the name of the module
app = Flask(__name__)

# a route is what we type 
# in our browser to go for different pages
# / is the root page of our web
# usually it should be index.html
@app.route('/')
def index():
    return '<h1> Hello! and Hello!</h1>' # wrap with h1 tag

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) # host the web on machine ip

# alternatively, yuou can use terminal directly
# export  FLASK_APP=file_name.py
# export FLASK_DEBUG=1 (optional)
# flask run --host 0.0.0.0 (host is optional) --reload, --no-reload, --debugger, and --no-debugger options
