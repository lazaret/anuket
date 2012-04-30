# -*- coding: utf-8 -*-
from alembic.config import Config
from alembic import command


def main():
    """ Upgrade the database schema with alembic."""
    alembic_cfg = Config('alembic.ini')
    command.upgrade(alembic_cfg, 'head')


#TODO:
# dump db before by default
# add argpase fo dump/nodump
# do nothing but check db version by default / user need to add "upgrade"
# as argument