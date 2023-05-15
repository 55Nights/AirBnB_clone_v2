#!/usr/bin/python3
import os
from fabric.api import *
from fabric import Connection

env.hosts = ['52.87.255.120', '100.26.220.215']






def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive to the /tmp/ directory of the web server
        with Connection(env.hosts[0]) as c:
            put(archive_path, '/tmp/')

        # Uncompress the archive to /data/web_static/releases/<archive filename without extension> on the web server
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]
        releases_path = '/data/web_static/releases/{}'.format(archive_name)

        with Connection(env.hosts[0]) as c:
            run('mkdir -p {}'.format(releases_path))
            run('tar -xzf /tmp/{} -C {}'.format(archive_filename, releases_path))
            run('rm /tmp/{}'.format(archive_filename))
            run('mv {}/web_static/* {}'.format(releases_path, releases_path))
            run('rm -rf {}/web_static'.format(releases_path))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(releases_path))

        return True

    except Exception as e:
        print(str(e))
        return False