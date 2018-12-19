
# TPN

# Trustless Reputation Demo

This is the app application.


## Minimum Requirements

- Python 3.4
- pipenv is already installed


## Optional Requirements

* `_pytest`: http://pytest.org - (for running the test suite)
* `_Sphinx`: http://sphinx-doc.org - (for generating documentation)


## Development Setup

Install for the current user:

    $ python setup.py develop

Run the application with cli:

    $ python -m app.cli --help

Run the test suite:
   
    $ pytest test/


Build documentation:

    $ sphinx-build -b html doc doc/_build/html


## Basic Setup

Install for the current user:

    $ python setup.py install --user


Run the application:

    $ python -m app --help


Run the test suite:
   
    $ pytest test/


Build documentation:

    $ sphinx-build -b html doc doc/_build/html
