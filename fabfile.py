import os
from fabric.api import task, local

here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)


@task(default=True)
def build():
    local('bin/tacot www -o build -v')


@task
def clean():
    local('rm build -rf')
    local('rm www/static/build/ -rf;')
    local('rm www/static/.webassets-cache/ -rf;')
    local('rm www/static/.sass-cache/ -rf')


@task
def upload_beta():
    os.system("rsync -e 'ssh -p 2010' -v -r --delete %s coworking-metz@santa-maria.stephane-klein.info:beta.coworking.a-metz.info/" % here('build/'))


@task
def upload_prod():
    os.system("rsync -e 'ssh -p 2010' -v -r --exclude='slides/2013-06-27/' --delete %s coworking-metz@santa-maria.stephane-klein.info:coworking.a-metz.info/" % here('build/'))
