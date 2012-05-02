# -*- coding: utf-8 -*-
import os
import argparse
from datetime import date

from alembic.config import Config
from alembic import command
from pyramid.paster import get_appsettings

from anuket.scripts.initializedb import set_alembic_settings


def upgrade_db(config_uri):
    """ Upgrade the database schema with alembic."""
    alembic_cfg = set_alembic_settings(config_uri)
    # perform upgrade
    command.upgrade(alembic_cfg, 'head')

def check_existing_dump(backup_directory):
    """ Check for an existing database dump for today. Return True if there is
    one.
    """
    # see also backupdb script
    today = date.today().isoformat()
    filename = 'anuket-'+today+'.sql.bz2'
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

    # get the setting from the config file
    settings = get_appsettings(args.config_file)
    backup_directory = settings['anuket.backup_directory']
    # look if there an up to date database backup file
    today_backup = check_existing_dump(backup_directory)
    if today_backup or args.force:
        upgrade_db(args.config_file)
    else:
        parser.error("There is no up to date backup for the database. " \
                     "Please use the backup script before upgrading!")
