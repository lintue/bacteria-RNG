"""Bacteria RNG.

pixel-tree, 2020.
"""

import os

from flask import Flask, send_file
# include jsonify, request in Flask imports.

# from rng import *

app = Flask(__name__,
            static_url_path="",
            static_folder=os.path.abspath("../static"))

# Image to RNG TO DO.

# General.
@app.route('/', methods=['GET', 'POST'])
def index():
    return send_file("../static/index.html")


# Use app.py for development;
# but wsgi.py for production deployment.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
