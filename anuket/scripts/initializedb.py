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


def initialize_db(config_uri=None):
    """ Initialize the database schema and add default values."""
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    # check if there is already a versioned database
    revision = get_alembic_revision(config_uri)
    if revision:
        message = "ERROR: This database is versioned. " \
                        "Please use the upgrade script instead!"
        return message
    # create the tables (except alembic_version)
    Base.metadata.create_all(engine)
    # add default user & group values
    with transaction.manager:
        admins_group = AuthGroup()
        admins_group.groupname = u'admins'
        admin_user = AuthUser()
        admin_user.username = u'admin'
        admin_user.password = u'admin'
        admin_user.group = admins_group
        try:
            DBSession.add(admins_group)
            DBSession.add(admin_user)
            DBSession.flush()
            message = "Database initialization done."
        except IntegrityError:
            DBSession.rollback()
            message = "ERROR: An IntegrityError have occured"
    # stamp the database with the most recent revision
    # (and create alembic_version table)
    alembic_cfg = get_alembic_settings(config_uri)
    stamp(alembic_cfg, 'head')
    return message


def main():  # pragma: no cover
    """ Create the database using the configuration from the ini file passed
    as a positional argument.
    """
    # get option from command line
    parser = argparse.ArgumentParser(
        description='Initialize the database',
        usage='%(prog)s config_file.ini',
        epilog='example: %(prog)s developement.ini')
    parser.add_argument('config_file',
        nargs='?',
        help='the application config file')
    args = parser.parse_args()
    if not args.config_file:
        # display the help message if no config_file is provided
        parser.print_help()
    else:
        message = initialize_db(args.config_file)
        if message:
            print message

#TODO: use logging instead of messages
