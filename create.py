from flask import Flask
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import *

# Settings
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://shbhdlrudoukbc:56b95ae93382d47bfe6f63214cd8fdd5bb7353e73867d0c6f1f09d5a390fc60a@ec2-54-165-36-134.compute-1.amazonaws.com:5432/d4e8h9gsq3giaq"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()