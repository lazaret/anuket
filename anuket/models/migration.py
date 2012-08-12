# -*- coding: utf-8 -*-
""" ``SQLAlchemy`` model definition for database migration with ``Alembic``."""
from sqlalchemy import Table, MetaData, Column, String
from sqlalchemy.orm import mapper


version_num = Column('version_num', String(32), nullable=False)
version_table = Table('alembic_version', MetaData(), version_num)


class Migration(object):
    """ Migration table and model definition.

    Reflect the default version table used by Alembic. This table is used
    for tracking database migrations.
    """
    pass


# the primary_key is defined only at mapper level to avoid
# modifing the original alembic version_table
mapper(Migration, version_table, primary_key=version_num)
