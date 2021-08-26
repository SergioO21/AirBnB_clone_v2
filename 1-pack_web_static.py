#!/usr/bin/python3
""" do_pack function """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive from the contents of the
        web_static folder of your AirBnB Clone repository.
    """

    date = datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                    date.month,
                                                    date.day,
                                                    date.hour,
                                                    date.minute,
                                                    date.second)

    local("mkdir -p versions")

    to_tgz = local("tar -cvzf versions/{} web_static".format(filename))

    if to_tgz.failed:
        return None
    else:
        return "versions/{}".format(filename)
