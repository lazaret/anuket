# -*- coding: utf-8 -*-
import os
import argparse
import bz2
import sqlite3
from datetime import date

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings


def verify_directory(dir):
    """ Create and/or verify a filesystem directory."""
    if not os.path.exists(dir):
        try:
            os.makedirs(dir, 0775)
        except:
            raise

def dump_sqlite(connect_args):
    """ Dump a SQLite database."""
    con = sqlite3.connect(connect_args['database'])
    sql_dump = os.linesep.join(con.iterdump())
    con.close()
    return sql_dump

def bzip(sql_dump, backup_directory, overwrite=False):
    """ Compress the SQL dump with bzip2."""
    today = date.today().isoformat()
    filename = 'anuket-'+today+'.sql.bz2'
    path = os.path.join(backup_directory, filename)
    # check if the file already exist
    isfile = os.path.isfile(path)
    if not isfile or overwrite:
        # create the zipped dump
        bz = bz2.BZ2File(path, 'w')
        bz.write(sql_dump)
        bz.close()
    else:
        print "Theyre is already a database backup with the same name!"

def main():
    """Dump the database for backup purpose.

    Supported database: SQLite.
    """
    # get option from command line
    parser = argparse.ArgumentParser(
        description='Dump the database',
        usage='%(prog)s config_file.ini',
        epilog='example: %(prog)s developement.ini')
    parser.add_argument('config_file',
        help='the application config file')
    parser.add_argument('-o', '--overwrite', action='store_true',
        help='overwrite existing backups files if set')
    args = parser.parse_args()

    # get the setting from the config file
    settings = get_appsettings(args.config_file)
    # verify and/or create the backup directory
    backup_directory = settings['anuket.backup_directory']
    verify_directory(backup_directory)
    # get db engine from settings
    engine = engine_from_config(settings, 'sqlalchemy.')
    connect_args = engine.url.translate_connect_args()
    # dump the database based on the engine
    if engine.dialect.name == 'sqlite':
        sql_dump = dump_sqlite(connect_args)
#    if engine.dialect.name == 'mysql':
#        pass
#    if engine.dialect.name == 'postgresql':
#        pass
    else:
        return "Sorry unsuported database engine!"
    bzip(sql_dump, backup_directory, args.overwrite)


#TODO: this is a very simple script we need to :
#Add other dadatases support (MySQL and Postgres)
#Use the brand_name option instad of 'anuket' for the database backup name
