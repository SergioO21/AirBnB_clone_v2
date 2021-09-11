#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.amenity import Amenity
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ Display a HTML page like 6-index.html """
    path = "10-hbnb_filters.html"
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    states.sort(key=lambda x: x.name)
    amenities.sort(key=lambda x: x.name)
    return render_template(path, states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
