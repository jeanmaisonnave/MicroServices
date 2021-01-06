from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)
    return db

def create_tables(app):
    engine = create_engine(app.config['SQLALCHLEMY_DATABASE_URI'])
    db.metadata.create_all(engine)
    return engine


class Product(db.Model):
    id = db.Collumn(db.Integer, primary_key=True)
    name = db.Collumn(db.String(255), nullable=False)
    price = db.Collumn(db.Integer, nullable=False)
    seller = db.Collumn(db.String(255), nullable=False)
    buyer = db.Collumn(db.String(255), nullable=False)
    date_added = db.Collumn(db.DateTime, default=datetime.utcnow)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'seller': self.seller,
            'buyer': self.buyer,
            'date_added': self.date_added
        }