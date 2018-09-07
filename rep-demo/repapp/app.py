from flask import Flask, Blueprint, render_template
from flask_restful import Api

from repapp.extensions import sqldb, migrate
# from repapp.database import db

# from repapp.resources.todo import Todo, TodoList
# from repapp.resources.customer import Customer, Customers
# from repapp.resources.service_provider import SProvider, SProviders
# from repapp.resources.transaction import Transactions, Transaction
# from repapp.resources.review import Reviews, Review

# Models register (as signal for flask_migrate)
from repapp.transaction.models import Transaction
from repapp.customer.models import Customer, CustomerTransaction
from repapp.sprovider.models import SProvider
from repapp.review.models import Review

# API Resources
from repapp.transaction.resources import TransactionResource, TransactionListResource
from repapp.customer.resources import CustomerResource, CustomerListResource
from repapp.sprovider.resources import SProviderResource, SProviderListResource
from repapp.review.resources import ReviewResource, ReviewListResource

def create_app(config_object='repapp.settings'):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(config_object)

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    api.add_resource(TransactionListResource, '/transactions')
    api.add_resource(TransactionResource, '/transactions/<id>')

    api.add_resource(CustomerListResource, '/customers')
    api.add_resource(CustomerResource, '/customers/<id>')

    api.add_resource(SProviderListResource, '/providers')
    api.add_resource(SProviderResource, '/providers/<id>')

    api.add_resource(ReviewListResource, '/reviews')
    api.add_resource(ReviewResource, '/reviews/<id>')

    app.register_blueprint(api_bp)

    # db.init_app(app)
    sqldb.init_app(app)
    migrate.init_app(app, db=sqldb)

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return render_template('home.html')

    return app