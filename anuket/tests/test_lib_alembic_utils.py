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
        from alembic.config import Config
        from pyramid.paster import get_appsettings
        from anuket.lib.alembic_utils import get_alembic_settings
        alembic_cfg = get_alembic_settings(config_uri)
        # test the config object
        self.assertIsInstance(alembic_cfg, Config)
        # test the script_location option
        script_location = alembic_cfg.get_section_option(
            'alembic',
            'script_location')
        self.assertEqual(script_location, 'anuket:scripts/alembic')
        # test the sqlalchemy.url option
        sqlalchemy_url = alembic_cfg.get_section_option(
            'alembic',
            'sqlalchemy.url')
        pyramid_sqlalchemy_url = get_appsettings(config_uri)['sqlalchemy.url']
        self.assertEqual(sqlalchemy_url, pyramid_sqlalchemy_url)

#TODO add a test for alembic revision
