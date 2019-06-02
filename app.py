from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return "Welcome to my python web app"

@app.route('/home')
def home():
    return "Welcome to my python home page"


if (__name__=='__main__'):
    app.run(debug=True)