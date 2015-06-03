# -*- coding: utf-8 -*-

import re
import os

from flask import Flask, Response, request
from flask_cors import CORS


app = Flask(__name__, static_url_path="")

app.config['DEBUG'] = os.environ.get('DEBUG', "True") == "True"

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60

cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/")
def index():
    return u"Use o /matches.json no exercicio."


def add_charset_to_json_static_files(response):
    if (request.path and 
            re.search(r'\.(json)$', request.path)):
        response.headers['Content-Type'] = 'application/json; charset=utf-8'

    return response

app.after_request(add_charset_to_json_static_files)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
