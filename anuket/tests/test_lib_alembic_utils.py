# -*- coding: utf-8 -*-
import os

from pyramid import testing

from anuket.tests import AnuketTestCase


here = os.path.dirname(__file__)
config_uri = os.path.join(here, '../../', 'test.ini')


class AlembicUtilsTests(AnuketTestCase):
    """ Tests for the alembic utilities library."""

    def setUp(self):
        super(AlembicUtilsTests, self).setUp()
        self.config = testing.setUp()

    def tearDown(self):
        super(AlembicUtilsTests, self).tearDown()
        testing.tearDown()


    def test_01_get_alembic_settings(self):
        """ Test the `get_ alembic_settings` utility."""
        from anuket.lib.alembic_utils import get_alembic_settings
        alembic_cfg = get_alembic_settings(config_uri)
        from alembic.config import Config
        self.assertIsInstance(alembic_cfg, Config)
        script_location = alembic_cfg.get_section_option(
            'alembic',
            'script_location')
        self.assertEqual(script_location, 'anuket:scripts/alembic')
        sqlalchemy_url = alembic_cfg.get_section_option(
            'alembic',
            'sqlalchemy.url')
#        self.assertEqual(sqlalchemy_url, 'sqlite:///'+testdb_uri)
#TODO: the above test


#    def test_02_get_alembic_revision(self):
#        """ Test the `get_alembic_revision` utility."""
#        from anuket.lib.alembic_utils import get_alembic_revision
#        revision = get_alembic_revision(config_uri)
#        self.assertEqual(revision, None)
#
#        from alembic.command import stamp
#        from anuket.lib.alembic_utils import get_alembic_settings
#        alembic_cfg = get_alembic_settings(config_uri)
#        stamp(alembic_cfg, 'head')
#        revision = get_alembic_revision(config_uri)
#        self.assertEqual(revision, 'revid')
