# -*- coding: utf-8 -*-
import argparse
import transaction

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings, setup_logging
from alembic.config import Config
from alembic import command

from anuket.models import DBSession, Base, AuthUser, AuthGroup


def initialize_db(config_uri=None):
    """ Initialize the database with default values."""
    if config_uri:
        setup_logging(config_uri)
        settings = get_appsettings(config_uri)
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            admins_group = AuthGroup(
                groupname=u'admins')
            DBSession.add(admins_group)
            admin_user = AuthUser(
                username=u'admin',
                password=u'admin',
                group=admins_group)
            DBSession.add(admin_user)

def alembic_stamp():
    """ Stamp the database with the most recent schema revision.

    Create a `alembic_version` in the database with a `version_num` field and
    set the version value to the last almebic revision."""
    alembic_cfg = Config("alembic.ini")
    command.stamp(alembic_cfg, "head")

def main():
    """ Create the database using the configuration from the ini file passed
    as a positional argument.
    """
    # get option from comand line
    parser = argparse.ArgumentParser(
                description='Initialize the database',
                usage='%(prog)s file.ini',
                epilog='example: %(prog)s developement.ini')
    parser.add_argument(
                'file',
                help='The application config file')
    args = parser.parse_args()
    # initialize the db
    initialize_db(args.file)
    alembic_stamp()

