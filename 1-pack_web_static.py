#!/usr/bin/python3
"""This module createscompressed archive file of in
    directory named web_static"""

import datetime
from fabric.api import local


def do_pack():
    """The function creates the compressed archive in the naming
        format web_static_<year><month><day><hour><minute><second>.tgz
    """
    try:
        now = datetime.datetime.now()
        now = now.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        name = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static".format(name))
        return name
    except Exception:
        return None
