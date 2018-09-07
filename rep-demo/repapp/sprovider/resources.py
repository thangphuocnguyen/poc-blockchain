import uuid
from flask_restful import Resource, fields, reqparse, marshal_with, abort

from repapp.extensions import sqldb as db
from .models import SProvider

data_fields = {
    'id': fields.Integer,
    'identifier' : fields.String,
    'pubkey' : fields.String,
    'privkey' : fields.String,
    'e' : fields.String,
    'n' : fields.String,
    'd' : fields.String
}
sub_data_fields = {
    'id': fields.Integer,
    # 'sprovider_id': fields.Integer,
    'identifier': fields.String,
    'desc': fields.String
}
data_fields['transactions'] = fields.List(fields.Nested(sub_data_fields))

parser = reqparse.RequestParser()
parser.add_argument('identifier')
parser.add_argument('pubkey')
parser.add_argument('privkey')
parser.add_argument('e')
parser.add_argument('n')
parser.add_argument('d')

class SProviderResource(Resource):
    @marshal_with(data_fields)
    def get(self, id):
        sp = db.session.query(SProvider).filter(SProvider.id == id).first()
        if not sp:
            abort(404, message="SProvider {} doesn't exist".format(id))
        return sp

    def delete(self, id):
        sp = db.session.query(SProvider).filter(SProvider.id == id).first()
        if not sp:
            abort(404, message="SProvider {} doesn't exist".format(id))
        db.session.delete(sp)
        db.session.commit()
        return {}, 204
    
    @marshal_with(data_fields)
    def put(self, id):
        sp = db.session.query(SProvider).filter(SProvider.id == id).first()
        if not sp:
            abort(404, message="SProvider {} doesn't exist".format(id))
        
        parsed_args = parser.parse_args()

        sp.identifier = parsed_args['identifier']
        sp.pubkey = parsed_args['pubkey']
        sp.privkey = parsed_args['privkey']
        sp.e = parsed_args['e']
        sp.n = parsed_args['n']
        sp.d = parsed_args['d']

        db.session.add(sp)
        db.session.commit()

        return sp, 201

class SProviderListResource(Resource):
    @marshal_with(data_fields)
    def get(self):
        sp = db.session.query(SProvider).all()
        return sp

    @marshal_with(data_fields)
    def post(self):
        parsed_args = parser.parse_args()
        sp = SProvider(
                identifier=str(uuid.uuid4()),
                pubkey=parsed_args['pubkey'],
                privkey=parsed_args['privkey'],
                e=parsed_args['e'],
                n=parsed_args['n'],
                d=parsed_args['d']
            )

        db.session.add(sp)
        db.session.commit()
        return sp, 201