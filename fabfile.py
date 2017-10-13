# -*- encoding: utf-8 -*-
from fabric.api import run, local
from fabric.api import env
from fabric.api import roles

path = '/home/services/python/rigipstrophy'
venv_path = '/virtuals/rigipstrophy/'
env.shell = '/bin/bash -l -c'
sock_path = '/virtuals/rigipstrophy/rigipstrophy.sock'
SETTINGS = 'settings.production'

env.roledefs = {
    'production': ['jmk@rigips.pl:1922']
}


def host_type():
    run('uname -s')


@roles('production')
def deploy():
    host_type()
    # local('git push')
    gitup()
    run('%s/bin/pip install -r %s/requirements.txt' % (venv_path, path))
    run('SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py migrate' % (SETTINGS, venv_path, path))
    # run('SETTINGS=%s %s/bin/python %s/manage.py calculate' % (SETTINGS,venv_path, path))
    reload_app()
    collect_static()

@roles('production')
def quickdeploy():
    host_type()
    # local('git push')
    gitup()
    run('SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py migrate' % (SETTINGS, venv_path, path))
    # run('SETTINGS=%s %s/bin/python %s/manage.py calculate' % (SETTINGS,venv_path, path))
    reload_app()
    collect_static()

@roles('production')
def makemigrations():
    run('SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py makemigrations' % (SETTINGS, venv_path, path))

@roles('production')
def gitstash():
    run('cd %s; git stash' % path)

@roles('production')
def clean_cache():
    run('SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py thumbnail clear' % (SETTINGS, venv_path, path))


@roles('production')
def rebuild_tree():
    run('SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py rebuild_tree' % (SETTINGS, venv_path, path))


@roles('production')
def gitup():
    run('cd %s; git pull' % path)


@roles('production')
def reload_app():
    run('source %s/bin/activate' % venv_path)
    run('bash %s/run-sc.sh' % path)

@roles('production')
def pip_install():
    gitup()
    run('%s/bin/pip install -r %s/requirements.txt' % (venv_path, path))


@roles('production')
def collect_static():
    run('LC_ALL=pl_PL.UTF8 PYTHONENCODING=UTF-8 SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py collectstatic  --noinput' % (SETTINGS, venv_path, path))
    reload_app()

@roles('production')
def clean_cache():
    run('LC_ALL=pl_PL.UTF8 PYTHONENCODING=UTF-8 SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py thumbnail clear' % (SETTINGS, venv_path, path))

@roles('production')
def quick_test():
    run('LC_ALL=pl_PL.UTF8 PYTHONENCODING=UTF-8 SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py quick_test' % (SETTINGS, venv_path, path))


@roles('production')
def createsuperuser():
    run('LC_ALL=pl_PL.UTF8 PYTHONENCODING=UTF-8 SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py createsuperuser' % (SETTINGS, venv_path, path))

#
# @roles('production')
# def fix_users():
#     run('LC_ALL=pl_PL.UTF8 PYTHONENCODING=UTF-8 SETTINGS=%s %s/bin/python %s/rigipstrophy/manage.py fix_users' % (SETTINGS, venv_path, path))