
from flask_restful import Resource, fields, reqparse, marshal_with, abort

from repapp.extensions import sqldb as db
from .models import Review

data_fields = {
    'id': fields.Integer,
    'addr': fields.String,
    'pubkey': fields.String,
    'token': fields.String,
    'rating': fields.Integer,
    'review': fields.String,
    'sig': fields.String,
    'pointer': fields.String
}

parser = reqparse.RequestParser()

parser.add_argument('addr')
parser.add_argument('pubkey')
parser.add_argument('token')
parser.add_argument('rating')
parser.add_argument('review')
parser.add_argument('sig')
parser.add_argument('pointer')

class ReviewResource(Resource):
    @marshal_with(data_fields)
    def get(self, id):
        rev = db.session.query(Review).filter(Review.id == id).first()
        if not rev:
            abort(404, message="Review {} doesn't exist".format(id))
        return rev

    def delete(self, id):
        rev = db.session.query(Review).filter(Review.id == id).first()
        if not rev:
            abort(404, message="Review {} doesn't exist".format(id))
        db.session.delete(rev)
        db.session.commit()
        return {}, 204

    @marshal_with(data_fields)
    def put(self, id):
        rev = db.session.query(Review).filter(Review.id == id).first()
        if not rev:
            abort(404, message="Review {} doesn't exist".format(id))
        
        parsed_args = parser.parse_args()
        
        rev.addr = parsed_args['addr']
        rev.pubkey = parsed_args['pubkey']
        rev.token = parsed_args['token']
        rev.rating = parsed_args['rating']
        rev.review = parsed_args['review']
        rev.sig = parsed_args['sig']
        rev.pointer = parsed_args['pointer']

        db.session.add(rev)
        db.session.commit()

        return rev, 201

class ReviewListResource(Resource):
    @marshal_with(data_fields)
    def get(self):
        rev = db.session.query(Review).all()
        return rev

    @marshal_with(data_fields)
    def post(self):
        parsed_args = parser.parse_args()
        rev = Review(
                addr=parsed_args['addr'],
                pubkey=parsed_args['pubkey'],
                token=parsed_args['token'],
                rating=parsed_args['rating'],
                review=parsed_args['review'],
                sig=parsed_args['sig'],
                pointer=parsed_args['pointer']
            )

        db.session.add(rev)
        db.session.commit()
        return rev, 201