#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    """display States, object found by id State and its cities"""
    states = storage.all(State).values()
    if id:
        _id = id
        id_state = None
        for state in states:
            if state.id == _id:
                id_state = state
                break
    else:
        id_state = list(states)
    return (render_template('9-states.html', **locals()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
