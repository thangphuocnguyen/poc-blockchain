from tinydb import Query, TinyDB


from repapp.settings import TINYDB_PATH


class DB_ADAPTER(object):

    def __init__(self, tinydb):
        self.db_wrapper = tinydb
        self.tbl_transaction = tinydb.table('transaction')
        self.tbl_customer = tinydb.table('customer')
        self.tbl_sprovider = tinydb.table('sprovider')
        self.tbl_review = tinydb.table('review')

db = DB_ADAPTER(TinyDB(TINYDB_PATH))