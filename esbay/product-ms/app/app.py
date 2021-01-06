from flask import Flask, json, request, jsonify
import models

app = Flask(__name__)

app.config.update(
    dict(
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@user_db/product',
    )
)

models.init_app(app)
models.create_tables(app)

@app.route('/product/welcome')
def hello():
    return 'Hello, welcome to the ESBAY Product API`\n'


@app.route('product/create', methods=['POST'])
def create_product():

    name = request.form['name']
    seller = request.form['seller']
    price = request.form['price']

    item = models.Product()
    item.name = name
    item.seller = seller
    item.price = price

    models.db.session.add(item)
    models.db.session.commit()

    response = jsonify({'message' : 'Product added', 'product': item.to_json})
    return response

@app.route('/api/products', method=['GET'])
def get_products():
    data = []

    for row in models.Product.query.all():
        data.append(row.to_json())

    response = jsonify(data)

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
