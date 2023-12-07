#!/usr/bin/python3
"""This module distributes an archive to my web servers
    using the function do_deploy"""

import datetime
from fabric.api import local, run, env, put
from os.path import exists
env.hosts = ['54.237.85.149', '52.91.127.145']


def do_deploy(archive_path):
    """The function do_deploy which distributes an archive
    to my web servers"""
    if exists(archive_path) is False:
        return False
    try:
        name = archive_path.split('/')[-1]
        put(archive_path, '/tmp/{}'.format(name))
        spl = name.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(spl))
        dis = '/data/web_static/releases/{}/'.format(spl)
        c = 'tar -xzf'
        run('{} /tmp/{} -C /data/web_static/releases/{}/'.format(c, name, spl))
        run('rm /tmp/{}'.format(name))
        run('mv /data/web_static/releases/{}/web_static/* {}'.format(spl, dis))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(spl))
        run('rm -rf /data/web_static/current')
        run('ln -sf {} /data/web_static/current'.format(dis))
        return True
    except Exception:
        return False
