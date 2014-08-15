#!/usr/bin/env python

"""
Usage: ./manage.py [submanager] <command>
Manage script for development. Type ./manage.py for more info
"""
import os

from flask_script import Manager
from flask_script.commands import ShowUrls

from src.app import create_app
from src.settings import app_config

def import_env():
    if os.path.exists('.env'):
        print 'Importing environment from .env...'
        for line in open('.env'):
            var = line.strip().split('=', 1)
            if len(var) == 2:
                os.environ[var[0]] = var[1]

import_env()

app = create_app(app_config)
manager = Manager(app)

manager.add_command("routes", ShowUrls())

@manager.shell
def make_context_shell():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()
