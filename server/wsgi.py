"""WSGI entry point.

Run app.py for dev; this for deployment.
"""

from app import app

if __name__ == "__main__":
    app.run()
