# -*- coding: utf-8 -*-
import argparse
import bz2
import os
import sqlite3
import sys
from datetime import date

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings


def main(argv=sys.argv):
    command = BackupDBCommand(argv)
    return command.run()


class BackupDBCommand(object):
    """Dump the database for backup purpose.

    Supported database: SQLite.
    """
    description = 'Dump the database'
    usage = '%(prog)s config_uri'
    epilog = 'example: %(prog)s development.ini'

    parser = argparse.ArgumentParser(
        description=description,
        usage=usage,
        epilog=epilog)
    parser.add_argument('config_uri',
        nargs='?',
        help='the application config file')
    parser.add_argument('-o', '--overwrite', action='store_true',
        help='overwrite existing backups files')

    def __init__(self, argv):
        self.args = self.parser.parse_args(argv[1:])


    def run(self):
        if not self.args.config_uri:
            self.parser.print_help()
            return 2
        else:
            return self.backup_db()


    def backup_db(self):
        config_uri = self.args.config_uri
        overwrite = self.args.overwrite
        settings = get_appsettings(config_uri)
        name = settings['anuket.brand_name']
        directory = settings['anuket.backup_directory']
        today = date.today().isoformat()
        filename = '{0}-{1}.sql.bz2'.format(name, today)
        path = os.path.join(directory, filename)

        # check if the backup file already exist
        isfile = os.path.isfile(path)
        if isfile and not overwrite:
            print("There is already a database backup with the same name!")
            return 1

        # get db engine from settings and create a dump
        engine = engine_from_config(settings, 'sqlalchemy.')
        connect_args = engine.url.translate_connect_args()
        if engine.dialect.name == 'sqlite':
            sql_dump = self.dump_sqlite(connect_args)
#        if engine.dialect.name == 'mysql':
#            pass
#       if engine.dialect.name == 'postgresql':
#            pass
        else:
            print("Unsuported database engine!")
            return 1

        if sql_dump:
            # verify and/or create the backup directory
            self.verify_directory(directory)
            # bzip and save the file
            bz = bz2.BZ2File(path, 'w')
            bz.write(sql_dump)
            bz.close()
            print("Database backup done.")
            return 0


    def verify_directory(self, dir=None):
        """ Create and/or verify the existence of a filesystem directory."""
        if not os.path.exists(dir):
            try:
                os.makedirs(dir, 0775)
            except:
                raise

#    def dump_mysql(self, connect_args=None):
#        """ Dump a MySQL database."""
#        #TODO: MySQL support

#    def dump_postgresql(self, connect_args=None):
#        """ Dump a PostgreSQL database."""
#        #TODO: PostgreSQL support

    def dump_sqlite(self, connect_args=None):
        """ Dump a SQLite database."""
        con = sqlite3.connect(connect_args['database'])
        sql_dump = os.linesep.join(con.iterdump())
        con.close()
        return sql_dump


#TODO: add options for name and directory
