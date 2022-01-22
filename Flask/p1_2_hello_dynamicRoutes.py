from flask import Flask
app = Flask(__name__)

# <h1> is the html tag remember?
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# During execution, you can type /user/<thename> behind the 
# 127.0.0.1 url, it will auto generate your name after hello
@app.route("/") # with or without this line still worked
@app.route('/user/<name>') 
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


if __name__ == "__main__":
    app.run(debug=True)
