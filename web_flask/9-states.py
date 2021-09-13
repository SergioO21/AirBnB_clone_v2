#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """ Display a HTML page: (inside the tag BODY) """
    states = storage.all(State).values()
    _id = id

    if id:
        for state in states:
            if state.id == id:
                state_id = state
                break
    else:
        state_id = list(states)

    return render_template("9-states.html", **locals())


@app.teardown_appcontext
def teardown_db(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
