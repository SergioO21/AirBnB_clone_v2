#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ Display a HTML page: (inside the tag BODY) """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
