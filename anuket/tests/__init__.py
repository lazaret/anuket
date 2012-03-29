# -*- coding: utf-8 -*-
import os
from unittest import TestCase

from paste.deploy.loadwsgi import appconfig
from sqlalchemy import engine_from_config

from anuket.models import DBSession, Base


here = os.path.dirname(__file__)
settings = appconfig('config:' + os.path.join(here, '../../', 'test.ini'))


class AnuketTestCase(TestCase):
    def setUp(self):
        self.settings = settings
        engine = engine_from_config(self.settings, prefix='sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        self.DBSession = DBSession

    def tearDown(self):
        self.DBSession.remove()

    def auth_group_fixture(self):
        """ Auth group test fixture."""
        try:
            from anuket.models import AuthGroup
            group = AuthGroup()
            group.groupname = u'groupname'
            self.DBSession.add(group)
            self.DBSession.flush()
            return group
        except:  # pragma: no cover
            self.DBSession.rollback()
            raise AssertionError

    def auth_user_fixture(self):
        """ Auth user test fixture."""
        try:
            from anuket.models import AuthUser
            group = self.auth_group_fixture()
            user = AuthUser()
            user.username = u'username'
            user.first_name = u'firstname'
            user.last_name = u'lastname'
            user.email = u'email@email.com'
            user.password = u'password'
            user.group = group
            self.DBSession.add(user)
            self.DBSession.flush()
            return user
        except:  # pragma: no cover
            self.DBSession.rollback()
            raise AssertionError

    def password_fixture(self):
        """ Prandom password generator fixture."""
        from random import choice
        from string import letters
        try:
            from cracklib import VeryFascistCheck
            while True:
                # generate 8 letters random password
                password = u''.join([choice(letters) for i in range(8)])
                try:
                    VeryFascistCheck(password)
                    break
                except ValueError:
                    # the generated password is not secure
                    pass
            return password
        except:  # pragma: no cover
            # cracklib is probably missing
            raise AssertionError
