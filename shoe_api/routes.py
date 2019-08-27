from shoe_api import app
from shoe_api.models import db,product_schema,products_schema,Product
from flask import request, jsonify


# Create Product
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    photo = request.json['photo']
    color_way = request.json['color_way']

    new_product = Product(name,description,price,qty,photo,color_way)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Get Single Product
@app.route('/product/<id>', methods=["GET"])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

@app.route('/product/<id>', methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    # Say what we want to update
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    photo = request.json['photo']
    color_way = request.json['color_way']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty
    product.photo = photo
    product.color_way = color_way

    db.session.commit()

    return product_schema.jsonify(product)

#Delete Product
@app.route('/product/<id>', methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)


# Get All Products
@app.route('/product',methods=["GET"])
def get_all_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result.data)
