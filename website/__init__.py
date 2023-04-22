from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, create_engine, text
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Brody678@localhost/exam_management"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

conn_str = "mysql://root:Brody678@localhost/exam_management"
engine = create_engine(conn_str, echo=True)
conn = engine.connect()