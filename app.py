# -*- coding: utf-8 -*-

import os
from flask import Flask, Response
from flask_cors import CORS
from flask_cache_response_decorator import cache

app = Flask(__name__)

app.config['DEBUG'] = os.environ.get('DEBUG', "True") == "True"

cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/")
def index():
    return u"Use o /matches.json no exercicio."

def read_file(filename, charset='utf-8'):
    json_value = ""
    with open(filename, 'r') as f:
        json_value = f.read().decode(charset)
    return json_value


@app.route("/matches.json")
@cache(expires=60)
def list_matches():
    json_value = read_file('matches.json')

    rv = Response(
        json_value,
        content_type='application/json; charset=utf-8')

    return rv


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
