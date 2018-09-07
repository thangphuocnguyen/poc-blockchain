
from flask_restful import Resource, fields, reqparse, marshal_with, abort

from repapp.extensions import sqldb as db
from .models import Transaction

data_fields = {
    'id': fields.Integer,
    'desc': fields.String,
    'identifier': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('identifier')
parser.add_argument('desc')

class TransactionResource(Resource):
    @marshal_with(data_fields)
    def get(self, id):
        trans = db.session.query(Transaction).filter(Transaction.id == id).first()
        if not trans:
            abort(404, message="Transaction {} doesn't exist".format(id))
        return trans

    def delete(self, id):
        trans = db.session.query(Transaction).filter(Transaction.id == id).first()
        if not trans:
            abort(404, message="Transaction {} doesn't exist".format(id))
        db.session.delete(trans)
        db.session.commit()
        return {}, 204
    
    @marshal_with(data_fields)
    def put(self, id):
        trans = db.session.query(Transaction).filter(Transaction.id == id).first()
        if not trans:
            abort(404, message="Transaction {} doesn't exist".format(id))
        
        parsed_args = parser.parse_args()

        trans.desc = parsed_args['desc']

        db.session.add(trans)
        db.session.commit()

        return trans, 201

class TransactionListResource(Resource):
    @marshal_with(data_fields)
    def get(self):
        trans = db.session.query(Transaction).all()
        return trans

    @marshal_with(data_fields)
    def post(self):
        parsed_args = parser.parse_args()
        trans = Transaction(
                identifier=parsed_args['identifier'],
                desc=parsed_args['desc']
            )

        db.session.add(trans)
        db.session.commit()
        return trans, 201