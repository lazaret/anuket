# -*- coding: utf-8 -*-
import os
import argparse
from datetime import date

from alembic.command import upgrade
from pyramid.paster import get_appsettings

from anuket.lib.alembic_utils import get_alembic_settings


def check_existing_dump(config_uri=None):
    """ Check for an existing database dump for today. Return True if there is
    already one.
    """
    # get the setting from the config file
    settings = get_appsettings(config_uri)
    backup_directory = settings['anuket.backup_directory']
    brand_name = settings['anuket.backup_directory']
    today = date.today().isoformat()
    filename = '{0}-{1}.sql.bz2'.format(brand_name, today)
    path = os.path.join(backup_directory, filename)
    return os.path.isfile(path)


def upgrade_db(config_uri=None, force=None):
    """ Upgrade the database to the head revision with alembic."""
    today_backup = check_existing_dump(config_uri)
    if today_backup or args.force:
        # upgrade the database
        alembic_cfg = get_alembic_settings(config_uri)
        upgrade(alembic_cfg, 'head')
    else:
        message = "There is no up to date backup for the database. " \
                  "Please use the backup script before upgrading!"
        log.error(message)
        return message


def main():  # pragma: no cover
    """ Upgrade the database using the configuration from the ini file passed
    as a positional argument.
    """
    # get option from command line
    parser = argparse.ArgumentParser(
        description='Upgrade the database',
        usage='%(prog)s config_file.ini',
        epilog='example: %(prog)s developement.ini')
    parser.add_argument('config_file',
        nargs='?',
        help='the application config file')
    parser.add_argument('-f', '--force', action='store_true',
        help='force the upgrade even if there is no available database backup')
    args = parser.parse_args()

    if not args.config_file:
        # display the help message if no config_file is provided
        parser.print_help()
    else:
        upgrade_db(args.config_file, args.force)
