# -*- coding: utf-8 -*-

import os
from flask import Flask, Response
from flask_cors import CORS
from flask_cache_response_decorator import cache

app = Flask(__name__, static_url_path="")

app.config['DEBUG'] = os.environ.get('DEBUG', "True") == "True"

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60

cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/")
def index():
    return u"Use o /matches.json no exercicio."

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
