# -*- coding: utf-8 -*-
""" Alembic utilities to use with database scripts."""
from pyramid.paster import get_appsettings
from alembic.config import Config
from alembic.script import ScriptDirectory


def get_alembic_settings(config_uri):
    """ Get alembic settings from the config file."""
    # get setting from the pyramid config file
    settings = get_appsettings(config_uri)
    # set alembic settings
    alembic_cfg = Config(config_uri)
    alembic_cfg.set_section_option(
        'alembic',
        'sqlalchemy.url',
        settings['sqlalchemy.url'])
    return alembic_cfg


def get_alembic_revision(config_uri):
    """ Check the existence of an alembic revision in the database. If the
    database is versioned, then return the current revision.
    """
    from anuket.models import DBSession, Migration
    from sqlalchemy.exc import OperationalError
    try:
        revision = DBSession.query(Migration.version_num).first()
    except OperationalError:
        revision = None
    return revision
