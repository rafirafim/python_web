from flask import Flask,render_template
from data import Students

app=Flask(__name__)

stud=Students()


@app.route('/')
def index():
    return  render_template('index.html',studList=stud)

@app.route('/home')
def home():
    return render_template('home.html')


if (__name__=='__main__'):
    app.run(debug=True)