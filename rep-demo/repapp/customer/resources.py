
from flask_restful import Resource, fields, reqparse, marshal_with, abort

from repapp.extensions import sqldb as db

from .models import Customer


data_fields = {
    'id': fields.Integer,
    'identifier': fields.String,
    # 'transactions': fields.List
    # 'privkey': fields.String,
    # 'pubkey': fields.String
}
sub_data_fields = {
    'id': fields.Integer,
    # 'customer_id': fields.Integer,
    'trans_identifier': fields.String,
    'pubkey': fields.String,
    'privkey': fields.String
}
data_fields['transactions'] = fields.List(fields.Nested(sub_data_fields))

parser = reqparse.RequestParser()
parser.add_argument('identifier')
# parser.add_argument('transactions')
# parser.add_argument('privkey')
# parser.add_argument('pubkey')

class CustomerResource(Resource):
    @marshal_with(data_fields)
    def get(self, id):
        cus = db.session.query(Customer).filter(Customer.id == id).first()
        if not cus:
            abort(404, message="Customer {} doesn't exist".format(id))
        return cus

    def delete(self, id):
        cus = db.session.query(Customer).filter(Customer.id == id).first()
        if not cus:
            abort(404, message="Customer {} doesn't exist".format(id))
        db.session.delete(cus)
        db.session.commit()
        return {}, 204
    
    @marshal_with(data_fields)
    def put(self, id):
        cus = db.session.query(Customer).filter(Customer.id == id).first()
        if not cus:
            abort(404, message="Customer {} doesn't exist".format(id))
        
        parsed_args = parser.parse_args()
        cus.identifier = parsed_args['identifier']
        # cus.pubkey = parsed_args['pubkey']
        # cus.privkey = parsed_args['privkey']

        db.session.add(cus)
        db.session.commit()

        return cus, 201

class CustomerListResource(Resource):
    @marshal_with(data_fields)
    def get(self):
        cus = db.session.query(Customer).all()
        return cus

    @marshal_with(data_fields)
    def post(self):
        parsed_args = parser.parse_args()
        cus = Customer(
                identifier=parsed_args['identifier']
                # pubkey=parsed_args['pubkey'],
                # privkey=parsed_args['privkey']
            )

        db.session.add(cus)
        db.session.commit()
        return cus, 201