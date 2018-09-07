from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

sqldb = SQLAlchemy()
migrate = Migrate(compare_type=True)