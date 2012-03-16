# -*- coding: utf-8 -*-
from unittest import TestCase


class ModelsTestCase(TestCase):
    def setUp(self):
        from wepwawet.models import DBSession, Base
        from sqlalchemy import create_engine
        engine = create_engine('sqlite:///:memory:')
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        self.DBSession = DBSession

    def tearDown(self):
        self.DBSession.remove()


    def auth_group_fixture(self):
        """ Auth group test fixture."""
        try:
            from wepwawet.models import AuthGroup
            group = AuthGroup()
            group.groupname = u'groupname'
            self.DBSession.add(group)
            self.DBSession.flush()
            return group
        except:
            self.DBSession.rollback()
            raise

    def auth_user_fixture(self):
        """ Auth user test fixture."""
        try:
            from wepwawet.models import AuthUser, AuthGroup
            group = self.auth_group_fixture()
            user = AuthUser()
            user.username = u'username'
            user.first_name = u'first_name'
            user.last_name=u'lastname'
            user.email=u'email@email.com'
            user.password=u'password'
            user.group = group
            self.DBSession.add(user)
            self.DBSession.flush()
            return user
        except:
            self.DBSession.rollback()
            raise
