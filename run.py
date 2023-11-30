"""Start the Flask application.

This script initializes and runs the Flask application using the 
create_app factory function.

Example:
    To start the Flask application:
    $ python run.py
"""

from logging import basicConfig, DEBUG
from app import create_app

basicConfig(level=DEBUG)

app = create_app()

host = app.config["HOST"]
port = app.config["PORT"]

print(app.config["SECRET_KEY"])

if __name__ == "__main__":
    app.run(host=host, port=port)
