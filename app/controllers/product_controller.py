from flask import Blueprint, jsonify, make_response, request


from app import db
from app.models.product import Product
from app.models.product_schema import ProductSchema


class ProductController:
    product_controller = Blueprint(name='product_controller', import_name=__name__)

    @product_controller.route('/products', methods=['GET'])
    def index():

        product_list = Product.query.all()
        product_schema = ProductSchema(many=True)
        products = product_schema.dump(product_list)

        return make_response(jsonify({
            "products": products
        }))

    @product_controller.route('/products/<id>', methods=['GET'])
    def get_product(id):
        product = Product.query.get(id)
        product_schema = ProductSchema()
        product_dumped = product_schema.dump(product)

        return make_response(jsonify({
            "product": product_dumped
        }))

    @product_controller.route('/products',methods=['POST'])
    def create():
        data = request.get_json()
        product_schema = ProductSchema(many=True)
        dataDumped = product_schema.dump(data)
        product = product_schema.load(dataDumped)
        result = product_schema.dump(product.create())

        # data = request.get_json()
        # product_schema = ProductSchema(many=True)
        #
        # product = product_schema.load(data)
        # result = product_schema.dump(product.create())


        return make_response(jsonify({
            "products": result
        }), 201)

    @product_controller.route('/products/<id>', methods=['DELETE'])
    def delete(id):
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return make_response(jsonify({}), 204)

    @product_controller.route('/products/<id>', methods=['PUT'])
    def update(id):
        product = Product.query.get(id)
        data = request.get_json()
        product_schema = ProductSchema()

        if(data.get('name')):
            product.name = data['name']
        if (data.get('price')):
            product.price = data['price']
        if (data.get('amount')):
            product.amount = data['amount']

        db.session.add(product)
        db.session.commit()

        updated_product = product_schema.dump(product)
        return make_response(jsonify({
            "products": updated_product
        }), 200)
