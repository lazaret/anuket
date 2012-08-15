# -*- coding: utf-8 -*-
""" Tests for the alembic utilities library."""
import os

from sqlalchemy.exc import OperationalError

from anuket.models import Base
from anuket.models.migration import version_table
from anuket.tests import AnuketTestCase


class AlembicUtilsTests(AnuketTestCase):
    """ Test the alembic utilities library."""
    def setUp(self):
        super(AlembicUtilsTests, self).setUp()
        Base.metadata.drop_all()
        # drop the alembic_version table
        try:
            version_table.drop(self.engine)
        except OperationalError:  # pragma: no cover
            pass

    def tearDown(self):
        super(AlembicUtilsTests, self).tearDown()
        Base.metadata.drop_all()
        # drop the alembic_version table
        try:
            version_table.drop(self.engine)
        except OperationalError:  # pragma: no cover
            pass

    def test_get_alembic_settings(self):
        """ Test the `get_alembic_settings` function."""
        from alembic.config import Config
        from pyramid.paster import get_appsettings
        from anuket.lib.alembic_utils import get_alembic_settings
        alembic_cfg = get_alembic_settings(self.config_uri)
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
        pyramid_sqlalchemy_url = self.settings['sqlalchemy.url']
        self.assertEqual(sqlalchemy_url, pyramid_sqlalchemy_url)

    def test_get_alembic_revision(self):
        """ Test the `get_alembic_revision` function with a revision."""
        import transaction
        from anuket.models.migration import Migration
        version_table.create(self.engine)
        with transaction.manager:
            alembic_version = Migration()
            alembic_version.version_num = u'revid'
            self.DBSession.add(alembic_version)
        self.DBSession.remove()

        from anuket.lib.alembic_utils import get_alembic_revision
        revision = get_alembic_revision(self.config_uri)
        self.assertEqual(revision[0], u'revid')

    def test_get_alembic_revision_empty(self):
        """ Test the `get_alembic_settings` function with an empty revision."""
        from anuket.lib.alembic_utils import get_alembic_revision
        revision = get_alembic_revision(self.config_uri)
        self.assertIsNone(revision)
