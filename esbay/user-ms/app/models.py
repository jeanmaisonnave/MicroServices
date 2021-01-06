from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from passlib.hash import sha256_crypt

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)
    return db

def create_tables(app):
    engine = create_engine(app.config['SQLALCHLEMY_DATABASE_URI'])
    db.metadata.create_all(engine)
    return engine

class User(db.Model):

    def encode_api_key(self):
        self.api_key = sha256_crypt.hash(self.username + str(datetime.utcnow))

    def encode_password(self):
        self.password = sha256_crypt.hash(self.password)

    def is_autheticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_email(self):
        return self.email

    def __repr__(self):
        return '<User %r>' %(self.email)

    def to_json(self):
        return{
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'api_key': self.api_key,
            'is_active': True
        }