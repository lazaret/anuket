# -*- coding: utf-8 -*-
""" Utilities to use with Alembic."""
#import os
#import sys

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
    alembic_cfg = Config()
    alembic_cfg.set_section_option(
        'alembic',
        'script_location',
        settings['alembic.script_location'])
    alembic_cfg.set_section_option(
        'alembic',
        'sqlalchemy.url',
        settings['sqlalchemy.url'])
    return alembic_cfg


def get_alembic_revision(config_uri):
    """ Check the existence of an alembic revision in the database. If the
    database is versioned, then return the revision.
    """
    # get setting from the pyramid config file
    settings = get_appsettings(config_uri)
    alembic_cfg = Config()
    alembic_cfg.set_main_option(
        'script_location',
        settings['alembic.script_location'])
    script = ScriptDirectory.from_config(alembic_cfg)
    head_revision = script.get_current_head()
    if head_revision:
        return head_revision
