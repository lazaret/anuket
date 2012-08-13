# -*- coding: utf-8 -*-
""" Script for upgrading the Anuket database with Alembic."""
import argparse
import os
import sys
from datetime import date

from alembic.command import upgrade
from pyramid.paster import get_appsettings

from anuket.lib.alembic_utils import get_alembic_settings


def main(argv=None):
    """ Main entry point for the `upgradedb` script."""
    if argv is None:  # pragma: no cover
        argv = sys.argv
    command = UpgradeDBCommand(argv)
    return command.run()


class UpgradeDBCommand(object):
    """ Upgrade the database using the configuration from the .ini file passed
    as a positional argument.
    """
    description = 'Upgrade the database'
    usage = '%(prog)s config_uri'
    epilog = 'example: %(prog)s development.ini'

    parser = argparse.ArgumentParser(
        description=description,
        usage=usage,
        epilog=epilog)
    parser.add_argument('config_uri',
        nargs='?',
        help='the application config file')
    parser.add_argument('-f', '--force', action='store_true',
        help='force the upgrade even if there is no available database backup')

    def __init__(self, argv):
        """ Get arguments from the ``argparse`` parser."""
        self.args = self.parser.parse_args(argv[1:])

    def run(self):
        """ Run the ``upgrade_db`` method or display the parser help message
        if the `config_uri` argument is missing.

        :return: ``upgrade_db`` method or 2 (missing argument error)
        """
        if not self.args.config_uri:
            self.parser.print_help()
            return 2
        else:
            return self.upgrade_db()

    def upgrade_db(self):
        """ Upgrade the database to the head revision with Alembic.

        :return: 0 (OK) or 1 (abnormal termination error)
        """
        config_uri = self.args.config_uri
        force = self.args.force
        settings = get_appsettings(config_uri)
        name = settings['anuket.brand_name']
        directory = settings['anuket.backup_directory']
        today = date.today().isoformat()
        filename = '{0}-{1}.sql.bz2'.format(name, today)
        path = os.path.join(directory, filename)

        # check if there is a database backup
        isfile = os.path.isfile(path)
        if not isfile and not force:
            print("There is no up to date backup for the database. "
                  "Please use the backup script before upgrading!")
            return 1

        # upgrade the database
        alembic_cfg = get_alembic_settings(config_uri)
        upgrade(alembic_cfg, 'head')

        print("Database upgrade done.")
        return 0
