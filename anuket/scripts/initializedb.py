# -*- coding: utf-8 -*-
""" Script to initialize the Anuket database."""
import argparse
import sys
import transaction

from alembic.command import stamp
from sqlalchemy import engine_from_config
from sqlalchemy.exc import IntegrityError
from pyramid.paster import get_appsettings

from anuket.lib.alembic_utils import get_alembic_revision
from anuket.lib.alembic_utils import get_alembic_settings
from anuket.models import DBSession, Base
from anuket.models.auth import AuthUser, AuthGroup


def main(argv=None):
    """ Main entry point for the `initilizedb` script."""
    if argv is None:  # pragma: no cover
        argv = sys.argv
    command = InitializeDBCommand(argv)
    return command.run()


class InitializeDBCommand(object):
    """ Create the database using the configuration from the .ini file passed
    as a positional argument.
    """
    description = 'Initialize the database'
    usage = '%(prog)s config_uri'
    epilog = 'example: %(prog)s development.ini'

    parser = argparse.ArgumentParser(
        description=description,
        usage=usage,
        epilog=epilog)
    parser.add_argument('config_uri',
        nargs='?',
        help='the application config file')

    def __init__(self, argv):
        """ Get arguments from the ``argparse`` parser."""
        self.args = self.parser.parse_args(argv[1:])

    def run(self):
        """ Run the ``initialize_db`` method or display the parser help message
        if the `config_uri` argument is missing.

        :return: ``initialize_db`` method or 2 (missing argument error)
        """
        if not self.args.config_uri:
            self.parser.print_help()
            return 2
        else:
            return self.initialize_db()

    def initialize_db(self):
        """ Initialize the database schema and insert default values.

        :return: 0 (OK) or 1 (abnormal termination error)
        """
        config_uri = self.args.config_uri
        settings = get_appsettings(config_uri)
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)

        # check if there is already a versioned database
        revision = get_alembic_revision(config_uri)
        if revision:
            print("This database is versioned. "
                  "Use the upgrade script instead!")
            return 1

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
            except IntegrityError:
                DBSession.rollback()
                print("There is already a database. "
                      "Use the upgrade script instead!")
                return 1

        # stamp the database with the most recent revision
        # (and create alembic_version table)
        try:
            alembic_cfg = get_alembic_settings(config_uri)
            stamp(alembic_cfg, 'head')
        except (AttributeError, ImportError):  # pragma: no cover
            # alembic is missing or not configured
            pass

        print("Database initialization done.")
        return 0
