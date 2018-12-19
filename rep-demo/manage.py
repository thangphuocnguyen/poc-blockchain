from flask_script import Manager
from flask_migrate import MigrateCommand

from repapp.app import create_app
from repapp.scripts import gendb_sample, debug, chaum_demo

app = create_app()
manager = Manager(app)

manager.add_command('db', MigrateCommand)

manager.add_command('gendb', gendb_sample.GenerateDBSample)
manager.add_command('debug', debug.Demo)
manager.add_command('chaum_demo', chaum_demo.Demo)


if __name__ == '__main__':
    manager.run()

