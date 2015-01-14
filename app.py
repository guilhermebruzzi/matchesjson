# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)

app.config['DEBUG'] = os.environ.get('DEBUG', "True") == "True"

local_connection = "mysql+pymysql://root:@localhost/matches?charset=utf8"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', local_connection)

db = SQLAlchemy(app)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(255), unique=True)
    shield = db.Column(db.String(255))


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt_of_match = db.Column(db.DateTime)
    where = db.Column(db.Unicode(255), nullable=False)
    link_of_match = db.Column(db.String(255), nullable=False)
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    guest_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    home_team_score = db.Column(db.Integer, nullable=False)
    guest_team_score = db.Column(db.Integer, nullable=False)
    home_team = db.relationship(Team, foreign_keys=[home_team_id], backref='matches_as_home_team')
    guest_team = db.relationship(Team, foreign_keys=[guest_team_id], backref='matches_as_guest_team')

db.create_all()

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Team, methods=['GET', 'POST', 'DELETE'], results_per_page=None)
manager.create_api(Match, methods=['GET', 'POST', 'DELETE'], results_per_page=None)

cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/")
def index():
    return "Use RESTFUL /api/match e /api/team para criar/ver/deletar/listar"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
