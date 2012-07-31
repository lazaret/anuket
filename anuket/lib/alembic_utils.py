# -*- coding: utf-8 -*-
""" Utilities to use with Alembic."""
from pyramid.paster import get_appsettings
from alembic.config import Config
from alembic.script import ScriptDirectory


def get_alembic_settings(config_uri):
    """ Get alembic settings.

    The Database url is get from the pyramid config file.
    """
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
    database is versioned, then return the current head revision.
    """
    alembic_cfg = Config(config_uri)
    script = ScriptDirectory.from_config(alembic_cfg)
    head_revision = script.get_current_head()
    if head_revision:
        return head_revision
