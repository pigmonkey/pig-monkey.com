import os

from fabric.api import env, local
from fabric.contrib.project import rsync_project

env.user = 'pigmonkey'
env.hosts = ['pig-monkey.com']
env.target_dir = 'pig-monkey.com'
env.project_dir = os.path.dirname(__file__)


def push(remote='origin'):
    """
    Push the current branch to origin.
    """
    local('git push %s' % remote)


def generate(settings='publishconf.py'):
    """
    Generate the site contents, defaulting to production settings.
    """
    local('pelican content -s %s' % settings)


def sync(delete=False):
    """
    Sync the munki repository to the target directory.
    """
    rsync_project(
        local_dir=env.project_dir + '/output/',
        remote_dir=env.target_dir,
        delete=delete
    )


def deploy():
    """
    Push, generate, and sync.
    """
    push()
    generate()
    sync()
