from flask_script import Manager
from flask_migrate import MigrateCommand

from repapp.app import create_app
from repapp.scripts import demo, debug

app = create_app()
manager = Manager(app)

manager.add_command('db', MigrateCommand)

manager.add_command('demo', demo.Demo)
manager.add_command('debug', debug.Demo)


if __name__ == '__main__':
    manager.run()

