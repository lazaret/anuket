# -*- coding: utf-8 -*-
import os
import sys
import argparse
import transaction

from sqlalchemy import engine_from_config
from sqlalchemy.exc import IntegrityError
from pyramid.paster import get_appsettings, setup_logging
from alembic.config import Config
from alembic import command

from anuket.models import DBSession, Base, AuthUser, AuthGroup


def set_alembic_settings(config_uri):
    """ Set alembic settings.

    The Database url is get from the pyramid config file."""
    # get setting from the pyramid config file
    settings = get_appsettings(config_uri)
    # set alembic settings
    alembic_cfg = Config(config_uri) # workaround for the alembic #45 bug
    alembic_cfg.set_section_option(
        'alembic',
        'script_location',
        settings['alembic.script_location'])
    alembic_cfg.set_section_option(
        'alembic',
        'sqlalchemy.url',
        settings['sqlalchemy.url'])
    return alembic_cfg


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

def check_db(config_uri):
    """ Check the existence of a alembic version in the database. If the
    database is versioned, then return the version.
    """
    alembic_cfg = set_alembic_settings(config_uri)
    # hack to remove stdout output from command.current
    devnull = open(os.devnull, 'w')
    _stdout = sys.stdout
    sys.stdout = devnull
    # get the alembic current revision
    revision = command.current(alembic_cfg)
    # undo the stdout hack
    sys.stdout = _stdout
    # return the current revision
    if revision:
        return revision

def stamp_db(config_uri):
    """ Stamp the database with the most recent schema revision.

    Create a `alembic_version` in the database with a `version_num` field and
    set the version value to the last revision."""
    alembic_cfg = set_alembic_settings(config_uri)
    command.stamp(alembic_cfg, 'head')

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
    version = check_db(args.config_file)
    if version:
        parser.error("Database is versioned." \
                     "Please use the upgrade script instead!")
    # initialize the db
    initialize_db(args.config_file)
    stamp_db(args.config_file)


#TODO: move alembic functions in lib/alembic for use in admin tools ?