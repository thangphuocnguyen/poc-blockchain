
# TPN

# Repapp Demo

Practices/Demo for [A trustless privacy-preserving reputation system](https://drive.google.com/file/d/12KyQKBwWgRUW-savTBvPqKq9mNtxFeTx/view?usp=sharing).


## Minimum Requirements

- Python 3.5
- pipenv is already installed


## Development Setup

Install for the current user:

    $ pipenv install

Activate Develop Environment
	
	$ pipenv shell

Base on .env.example, create/add Environment setting to .env file

Init the db

    $ python manage.py db init

Migrate db
   
    $ python manage.py db migrate

    $ python manage.py db upgrade


Debug/demo command:

    Run flask server:

        $ python manage.py runserver

    Generate db for sample:

        $ python manage.py gendb

    RSA sample:

        $ python manage.py debug

    Chaum sample:

        $ python manage.py chaum
