from fabric.api import local


def deploy():
    local("scp -r index.html resourcelist.manifest static/ threepines.org:/var/www/meyer/oddbird.net/files/mahjongg/")
