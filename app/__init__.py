from flask import Flask

#Create a Flask object and configures it
app = Flask(__name__)
app.config.from_object('config')

from app import views