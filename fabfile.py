from __future__ import with_statement

from datetime import datetime

from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['root@yunyanjin.com']

image_repo = 'powerformarc/yunyanjin-server'
container_name = 'web'


def test():
    """Execute local tests."""
    local('python3 manage.py test')


def build_and_push_image():
    """Build docker image from the code and push to Docker Hub."""
    local("docker build -t %s ." % image_repo)
    local("docker push %s" % image_repo)


def pull_image_and_redeploy():
    """Pull the newest image from Docker Hub."""
    # Pull the newest image
    run("docker pull %s" % image_repo)

    running_containers = run("docker ps --format {{.Names}}").split()
    if container_name in running_containers:
        # The image already has a running container
        # So we need to remove it
        run("docker rm -f %s" % container_name)
        run("docker rm -f proxy")

    # Run a container with the updated image and restart proxy
    run("docker run -d --name %s %s" % (container_name, image_repo))
    run("docker run -d --name proxy -p 80:80 --link web:web \
        --volumes-from web --volumes-from yyj_client powerformarc/pf-proxy")


def deploy():
    local("git push")
    build_and_push_image()
    pull_image_and_redeploy()
