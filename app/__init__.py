from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

#import models
from app.models import product
db.create_all()
#import controllers
from app.controllers.product_controller import ProductController
app.register_blueprint(ProductController.product_controller, url_prefix="/api/v1")

