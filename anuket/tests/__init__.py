# -*- coding: utf-8 -*-
import os
from unittest import TestCase

from paste.deploy.loadwsgi import appconfig
from sqlalchemy import engine_from_config

from anuket.models import DBSession, Base


here = os.path.dirname(__file__)
settings = appconfig('config:' + os.path.join(here, '../../', 'test.ini'))


class AnuketTestCase(TestCase):
    """ TestCase class for integration tests."""
    def setUp(self):
        self.settings = settings
        engine = engine_from_config(self.settings, prefix='sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        self.DBSession = DBSession

    def tearDown(self):
        self.DBSession.remove()

    def dummy_group_fixture(self):
        """ Create a dummy auth group test fixture in the database."""
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

    def dummy_user_fixture(self):
        """ Create a dummy auth user test fixture in the database."""
        try:
            from anuket.models import AuthUser
            group = self.dummy_group_fixture()
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
        """ Random valid password generator fixture."""
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
                except ValueError:  # pragma: no cover
                    # the generated password did not pass cracklib check
                    pass
            return password
        except:  # pragma: no cover
            # cracklib is probably missing
            raise AssertionError


class AnuketFunctionalTestCase(AnuketTestCase):
    """ TestCase class for functional tests."""
    def setUp(self):
        super(AnuketFunctionalTestCase, self).setUp()
        from anuket import main
        app = main({}, **self.settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        super(AnuketFunctionalTestCase, self).tearDown()
        del self.testapp

    def _admin_group_fixture(self):
        """ Create an admin group test fixture in the database."""
        try:
            from anuket.models import AuthGroup
            group = AuthGroup()
            group.groupname = u'admins'
            self.DBSession.add(group)
            self.DBSession.flush()
            return group
        except:  # pragma: no cover
            self.DBSession.rollback()
            raise AssertionError

    def _admin_user_fixture(self):
        """ Create an admin auth user test fixture in the database."""
        try:
            from anuket.models import AuthUser
            group = self._admin_group_fixture()
            user = AuthUser()
            user.username = u'admin'
            user.password = u'admin'
            user.group = group
            self.DBSession.add(user)
            self.DBSession.flush()
            return user
        except:  # pragma: no cover
            self.DBSession.rollback()
            raise AssertionError

    def connect_admin_user_fixture(self):
        """ Connect the test admin user with the login form.

        This create an admin user in the database, and then connect him with
        the login form. This set up an userid cookie inside the testing browser
        available for further tests."""
        self._admin_user_fixture()
        response = self.testapp.get('/login', status=200)
        csrf_token = response.form.fields['_csrf'][0].value
        params = {
            'form_submitted': u'',
            '_csrf': csrf_token,
            'username': u'admin',
            'password': u'admin',
            'submit': True}
        response = self.testapp.post('/login', params)
        return response

    def connect_dummy_user_fixture(self):
        """ Connect the test dummy user with the login form.

        This create a dummy user in the database, and then connect him with
        the login form. This set up an userid cookie inside the testing browser
        available for further tests."""
        self.dummy_user_fixture()
        response = self.testapp.get('/login', status=200)
        csrf_token = response.form.fields['_csrf'][0].value
        params = {
            'form_submitted': u'',
            '_csrf': csrf_token,
            'username': u'username',
            'password': u'password',
            'submit': True}
        response = self.testapp.post('/login', params)
        return response