# -*- coding: utf-8 -*-
""" Script to backup the Anuket database."""
import argparse
import bz2
import os
import sqlite3
import subprocess
import sys
import tempfile
from datetime import date

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings


def main(argv=None):
    """ Main entry point for the `backupdb` script."""
    if argv is None:  # pragma: no cover
        argv = sys.argv
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
        """ Get arguments from the ``argparse`` parser."""
        self.args = self.parser.parse_args(argv[1:])

    def run(self):
        """ Run the ``backup_db`` method or display the parser help message
        if the `config_uri` argument is missing.

        :return: ``backup_db`` method or 2 (missing argument error)
        """
        if not self.args.config_uri:
            self.parser.print_help()
            return 2
        else:
            return self.backup_db()

    def backup_db(self):
        """ Dump the database and then compress and save the file.

        :return: 0 (OK) or 1 (abnormal termination error)
        """
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
#        elif engine.dialect.name == 'mysql':
#            pass
        elif engine.dialect.name == 'postgresql':
            sql_dump = self.dump_postgresql(connect_args)
        else:  # pragma: no cover
            print("Unsuported database engine! (%s)" % engine.dialect.name)
            return 1

        if sql_dump:
            # verify and/or create the backup directory if necessary
            if not os.path.exists(directory):
                try:
                    os.makedirs(directory, 0775)
                except OSError:  # pragma: no cover
                    print("Could not create the backup directory.")
                    return 1
            # bzip and save the dump
            bz = bz2.BZ2File(path, 'w')
            bz.writelines(sql_dump)
            bz.close()
            sql_dump.close()
            print("Database backup done.")
            return 0


#    def dump_mysql(self, connect_args=None):
#        """ Dump a MySQL database."""


    def dump_postgresql(self, connect_args=None):
        """ Dump a PostgreSQL database with the `pg_dump` command.

        Dump the database in plain text format with ACLs, owner statments and
        COPY command.

        return a temporary file object (opened).
        """
        # ACLS and owners can be droped if necessary by `pg_retore`

        # construct the `pg_dump` command
        command = ['pg_dump']
        command.append('-w')  # no password prompt
        command.extend(['-U', connect_args['username']])
        command.extend(['-h', connect_args['host']])
        if connect_args.has_key('port'):
            command.extend(['-p', str(connect_args['port'])])
        command.append(connect_args['database'])
        # put the password in the environment variables
        os.putenv("PGPASSWORD", connect_args['password'])
        # save the database dump in a temp file
        sql_dump = tempfile.SpooledTemporaryFile()
        sql_dump.write(subprocess.check_output(command))
        sql_dump.seek(0)
        return sql_dump

        # TODO test the generated pg_dump command for windows too


    def dump_sqlite(self, connect_args=None):
        """ Dump a SQLite database.

        return a temporary file object"""
        connection = sqlite3.connect(connect_args['database'])
        sql_dump = tempfile.SpooledTemporaryFile()
        sql_dump.write('\n'.join(connection.iterdump()))
        connection.close()
        sql_dump.seek(0)
        return sql_dump


