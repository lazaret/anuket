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


def main():
    """ Upgrade the database using the configuration from the ini file passed
    as a positional argument.
    """
    # get option from command line
    parser = argparse.ArgumentParser(
        description='Upgrade the database',
        usage='%(prog)s config_file.ini',
        epilog='example: %(prog)s developement.ini')
    parser.add_argument('config_file',
        help='the application config file')
    parser.add_argument('-f', '--force', action='store_true',
        help='force the upgrade even if there is no available database backup')
    args = parser.parse_args()

    # look if there an up to date database backup file
    today_backup = check_existing_dump(args.config_file)
    if today_backup or args.force:
        alembic_cfg = get_alembic_settings(args.config_file)
        # perform upgrade with alembic
        upgrade(alembic_cfg, 'head')
    else:
        parser.error("There is no up to date backup for the database."
                     "Please use the backup script before upgrading!")
