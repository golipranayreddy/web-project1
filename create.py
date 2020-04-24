from flask import Flask
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import *

# Settings
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()