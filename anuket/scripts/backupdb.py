# -*- coding: utf-8 -*-
import os
import sqlite3
import bz2
from datetime import date


from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings


def dump_sqlite(connect_args):
    """ Dump a SQLite database."""
    con = sqlite3.connect(connect_args['database'])
    sql_dump = os.linesep.join(con.iterdump())
    con.close()
    return sql_dump


def bzip(sql_dump):
    """ Compress the SQL dump with bzip2."""
    today = date.today().isoformat()
    filename = 'anuket-'+today+'.sql.bz2'
    bz = bz2.BZ2File(filename, 'w')
    bz.write(sql_dump)
    bz.close()


def main():
    """Dump the database for backup purpose.

    Supported database: SQLite.
    """
    # get db engine from config
    config_uri = 'development.ini'
    settings = get_appsettings(config_uri)
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
        return "Sorry unsuported database!"

    bzip(sql_dump)


#TODO: this is a very simple script we need to :
#Add other dadatase support (MySQL and Postgres)
#Save in var/backup
