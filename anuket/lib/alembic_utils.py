# -*- coding: utf-8 -*-
""" Alembic utilities to use with database scripts."""
from pyramid.paster import get_appsettings
from sqlalchemy.exc import OperationalError
from alembic.config import Config

from anuket.models import DBSession
from anuket.models.migration import Migration


def get_alembic_settings(config_uri):
    """ Get alembic settings from the config file.

    :param config_uri: an .ini config file
    :return: an ``alembic.config.Config`` object
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
    database is versioned, then return the current revision.

    :param config_uri: an .ini file
    :return: the alembic revision value or None
    """
    try:
        revision = DBSession.query(Migration.version_num).first()
    except OperationalError:
        revision = None
    return revision
