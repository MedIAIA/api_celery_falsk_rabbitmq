from urllib import request
from flask import jsonify
from app import app, db
from app.models import Product
from app.tasks import celery

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    # Convertir les produits en dictionnaires ou JSON si nécessaire
    return jsonify(products)

@app.route('/products', methods=['POST'])
def create_product():
    name = request.json.get('name')
    description = request.json.get('description')

    product = Product(name=name, description=description)
    db.session.add(product)
    db.session.commit()

    # Appeler la tâche Celery pour le traitement asynchrone si nécessaire
    celery.send_task('app.tasks.process_product', args=[product.id])

    return jsonify({'message': 'Product created successfully'}), 201
