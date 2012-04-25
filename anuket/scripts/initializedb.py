# -*- coding: utf-8 -*-
import os
import sys
import transaction

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings, setup_logging
from alembic.config import Config
from alembic import command

from anuket.models import DBSession, Base, AuthUser, AuthGroup


def usage(argv):  # pragma: no cover
    """ Display the usage command."""
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def initialize_db(config_uri=None):
    """ Initialize the database with default values."""
    if config_uri:
        setup_logging(config_uri)
        settings = get_appsettings(config_uri)
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            admins_group = AuthGroup(
                groupname=u'admins')
            DBSession.add(admins_group)
            admin_user = AuthUser(
                username=u'admin',
                password=u'admin',
                group=admins_group)
            DBSession.add(admin_user)

def alembic_stamp():
    """ Stamp the database with the most recent schema revision.

    Create a `alembic_version` in the database with a `version_num` field and
    set the version value to the last almebic revision."""
    alembic_cfg = Config("alembic.ini")
    command.stamp(alembic_cfg, "head")


def main(argv=sys.argv):  # pragma: no cover
    """ Create the database using the configuration from the ini file passed
    in argv. If no argv then dispaly the usage command.
    """
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    initialize_db(config_uri)
    alembic_stamp()
