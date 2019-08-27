from shoe_api import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#init Database
db = SQLAlchemy(app)

#init Marshmallow
ma = Marshmallow(app)

# Create Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = True)
    description = db.Column(db.String(250))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    photo = db.Column(db.String(250))
    color_way = db.Column(db.String(200))

    def __init__(self,name,description,price,qty,photo,color_way):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
        self.photo = photo
        self.color_way = color_way

# Create Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','price','qty','photo','color_way')

#Init Schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True,strict=True)
