# -*- coding: utf-8 -*-
""" Anuket test cases and fixtures."""
import os
import shutil
import sys
from unittest import TestCase
from StringIO import StringIO

from paste.deploy.loadwsgi import appconfig
from pyramid.request import Request
from pyramid.testing import DummyRequest
from sqlalchemy import engine_from_config

from anuket.models import DBSession, Base


here = os.path.dirname(__file__)
config_uri = os.path.abspath(os.path.join(here, 'test.ini'))
settings = appconfig('config:' + config_uri)


class AnuketDummyRequest(DummyRequest):
    """ Extend the ``pyramid.testing.DummyRequest`` class.

    * Add a fake ``request.tranlate`` object atribute.
    * Add the ``WebOb`` `accept_language` attribute.
    """
    def _fake_translation(self, string):
        """ Fake translation who return the original string."""
        return string

    translate = _fake_translation
    accept_language = Request.accept_language


class AnuketTestCase(TestCase):
    """ ``TestCase`` class for integration tests."""
    def setUp(self):
        self.settings = settings
        self.config_uri = config_uri
        self.engine = engine_from_config(self.settings, prefix='sqlalchemy.')
        DBSession.configure(bind=self.engine)
        Base.metadata.bind = self.engine
        Base.metadata.create_all(self.engine)
        self.DBSession = DBSession

    def tearDown(self):
        self.DBSession.remove()

    def dummy_group_fixture(self):
        """ Create a dummy auth group test fixture in the database."""
        try:
            from anuket.models.auth import AuthGroup
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
            from anuket.models.auth import AuthUser
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

    def admin_group_fixture(self):
        """ Create an admin group test fixture in the database."""
        try:
            from anuket.models.auth import AuthGroup
            group = AuthGroup()
            group.groupname = u'admins'
            self.DBSession.add(group)
            self.DBSession.flush()
            return group
        except:  # pragma: no cover
            self.DBSession.rollback()
            raise AssertionError

    def admin_user_fixture(self):
        """ Create an admin auth user test fixture in the database."""
        try:
            from anuket.models.auth import AuthUser
            group = self.admin_group_fixture()
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
    """ ``TestCase`` class for functional tests."""
    def setUp(self):
        super(AnuketFunctionalTestCase, self).setUp()
        from anuket import main
        app = main({}, **self.settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        super(AnuketFunctionalTestCase, self).tearDown()
        del self.testapp

    def connect_admin_user_fixture(self):
        """ Connect the test admin user with the login form.

        This create an admin user in the database, and then connect him with
        the login form. This set up an `userid` cookie inside the testing
        browser available for further tests.
        """
        self.admin_user_fixture()
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
        the login form. This set up an `userid` cookie inside the testing
        browser available for further tests.
        """
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


class AnuketScriptTestCase(AnuketTestCase):
    """ ``TestCase`` class for testing Anuket scripts. """
    def setUp(self):
        super(AnuketScriptTestCase, self).setUp()
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output
        self.file_fixture_path = None

    def tearDown(self):
        super(AnuketScriptTestCase, self).tearDown()
        self.output.close()
        sys.stdout = self.saved_stdout
        # delete the directory and file fixtures if any
        directory = self.settings['anuket.backup_directory']
        if os.path.exists(directory):
            try:
                shutil.rmtree(directory)
            except:  # pragma: no cover
                raise

    def backup_directory_fixture(self):
        """ Create a directory where SQL dump files would be saved."""
        directory = self.settings['anuket.backup_directory']
        if not os.path.exists(directory):
            try:
                os.makedirs(directory, 0775)
            except OSError:  # pragma: no cover
                raise

    def backup_file_fixture(self):
        """ Create an empty SQL dump file."""
        self.backup_directory_fixture()

        from datetime import date
        name = self.settings['anuket.brand_name']
        directory = self.settings['anuket.backup_directory']
        today = date.today().isoformat()
        filename = '{0}-{1}.sql.bz2'.format(name, today)
        self.file_fixture_path = os.path.join(directory, filename)
        backup_file = open(self.file_fixture_path, 'w')
        backup_file.close()
