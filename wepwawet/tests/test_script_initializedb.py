# -*- coding: utf-8 -*-
import os

from wepwawet.models import Base
from wepwawet.tests import WepwawetTestCase


here = os.path.dirname(__file__)
filename = os.path.join(here, '../../', 'test.ini')


class ScriptInitializedbTests(WepwawetTestCase):
    """Tests for the `initializedb` script."""

    def setUp(self):
        super(ScriptInitializedbTests, self).setUp()
        Base.metadata.drop_all()

    def tearDown(self):
        super(ScriptInitializedbTests, self).tearDown()
        Base.metadata.drop_all()

    def test_01_default_datas(self):
        """ test than the script create the default values."""
        from wepwawet.scripts.initializedb import initialize_db
        initialize_db(filename)
        from wepwawet.models import AuthUser
        user = self.DBSession.query(AuthUser).filter_by().first()
        self.assertEqual(user.username, u'admin')
        self.assertTrue(AuthUser.check_password(u'admin', u'admin'))
        self.assertEqual(user.group.groupname, u'admins')
