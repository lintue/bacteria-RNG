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

"""
# Image to RNG TO DO.
@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.get_data()
    # message = request.form['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    response_text = {"message":  fulfillment_text}

    return jsonify(response_text)
"""


# General.
@app.route('/', methods=['GET', 'POST'])
def index():
    return send_file("../static/index.html")


# Use app.py for development;
# but wsgi.py for production deployment.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
