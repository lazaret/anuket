# -*- coding: utf-8 -*-
import argparse
import transaction

from alembic.command import stamp
from sqlalchemy import engine_from_config
from sqlalchemy.exc import IntegrityError
from pyramid.paster import get_appsettings, setup_logging

from anuket.lib.alembic_utils import get_alembic_revision
from anuket.lib.alembic_utils import get_alembic_settings
from anuket.models import DBSession, Base, AuthUser, AuthGroup


def initialize_db(config_uri):
    """ Initialize the database schema and add default values."""
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    # create the tables
    Base.metadata.create_all(engine)
    # add default values
    with transaction.manager:
        admins_group = AuthGroup(
            groupname=u'admins')
        admin_user = AuthUser(
            username=u'admin',
            password=u'admin',
            group=admins_group)
        try:
            DBSession.add(admins_group)
            DBSession.add(admin_user)
            DBSession.flush()
        except IntegrityError:
            DBSession.rollback()


def main():
    """ Create the database using the configuration from the ini file passed
    as a positional argument.
    """
    # get option from command line
    parser = argparse.ArgumentParser(
        description='Initialize the database',
        usage='%(prog)s config_file.ini',
        epilog='example: %(prog)s developement.ini')
    parser.add_argument('config_file',
        help='the application config file')
    args = parser.parse_args()
    # check if there is already a versioned database
    revision = get_alembic_revision(args.config_file)
    if revision:
        parser.error("This database is versioned."
                     "Please use the upgrade script instead!")
    # initialize the db
    initialize_db(args.config_file)
    # stamp the database with the most recent schema revision
    alembic_cfg = get_alembic_settings(args.config_file)
    stamp(alembic_cfg, 'head')
