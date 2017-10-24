from flask import Flask, render_template
import mlab
from mongoengine import *
from faker import Faker
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host:'127.0.0.1', port=8000, debug=True)
