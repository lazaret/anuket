# -*- coding: utf-8 -*-
import os

from anuket.models import Base
from anuket.tests import AnuketTestCase


here = os.path.dirname(__file__)
config_uri = os.path.join(here, '../../', 'test.ini')
initializedb_script = os.path.join(here, '../scripts/', 'initializedb.py')


class ScriptInitializedbTests(AnuketTestCase):
    """ Tests for the `initializedb` script."""

    def setUp(self):
        super(ScriptInitializedbTests, self).setUp()
        Base.metadata.drop_all()

    def tearDown(self):
        super(ScriptInitializedbTests, self).tearDown()
        Base.metadata.drop_all()

    def test_01_default_datas(self):
        """ Test than the `initialize_db` function create default values."""
        from anuket.scripts.initializedb import initialize_db
        initialize_db(config_uri)
        from anuket.models import AuthUser
        user = self.DBSession.query(AuthUser).filter_by().first()
        self.assertEqual(user.username, u'admin')
        self.assertTrue(AuthUser.check_password(u'admin', u'admin'))
        self.assertEqual(user.group.groupname, u'admins')
