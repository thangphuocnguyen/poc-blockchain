import os

from repapp.app import create_app

if __name__ == '__main__':
    app = create_app()
    # run app
    app.run()
