#imports
from flask import Flask, render_template, request
import sqlite3
from flask import Blueprint


app=Flask(__name__)

main = Blueprint('main', __name__)

# home page route 
@app.route('/')
def home():
    return render_template ('home.html')


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=8080,
host='0.0.0.0')