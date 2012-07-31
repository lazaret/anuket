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
#    alembic_cfg = Config(config_uri)
#    script = ScriptDirectory.from_config(alembic_cfg)
#    head_revision = script.get_current_head()
#    if head_revision:
#        return head_revision
    from anuket.models import DBSession, Migration
    from sqlalchemy import engine_from_config
    from sqlalchemy.exc import OperationalError
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    try:
        revision = DBSession.query(Migration.version_num).first()
    except OperationalError:
        revision = None
    return revision
