# -*- coding: utf-8 -*-
import os
import sqlite3
import bz2


def dump_sqlite():
    """ Dump a SQLite database."""
    con = sqlite3.connect('anuket.db')
    full_dump = os.linesep.join(con.iterdump())
    con.close()
    f = open('anuket.sql', 'w')
    f.writelines(full_dump)
    f.close()


def bzip_dump():
    """ Compress the SQL dump with bzip2."""
    bz = bz2.BZ2File('anuket.sql.bz2', 'w')
    f = open('anuket.sql', 'rb')
    data = f.read()
    f.close()
    bz.write(data)
    bz.close()


def main():
    """Dump the database for backup purpose.

    Supported database: SQLite.
    """
    dump_sqlite()
    bzip_dump()


#TODO: this is a very simple script we need to :
#Get database engine from config
#Add other dadatase support (MySQL and Postgres)
#Add timestamp
#Save in var/backup
