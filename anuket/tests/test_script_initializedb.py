# -*- coding: utf-8 -*-
""" Tests for the `initializedb` script."""
import os

from sqlalchemy.exc import OperationalError

from anuket.models import Base
from anuket.models.migration import version_table
from anuket.tests import AnuketScriptTestCase


class TestInitializeDBCommand(AnuketScriptTestCase):
    """ Tests for the `initialize_db` and `run` methods."""
    def setUp(self):
        super(TestInitializeDBCommand, self).setUp()
        Base.metadata.drop_all()
        # drop the alembic_version table
        try:
            version_table.drop(self.engine)
        except OperationalError:  # pragma: no cover
            pass

    def tearDown(self):
        super(TestInitializeDBCommand, self).tearDown()
        Base.metadata.drop_all()
        # drop the alembic_version table
        try:
            version_table.drop(self.engine)
        except OperationalError:  # pragma: no cover
            pass

    def _getTargetClass(self):
        from anuket.scripts.initializedb import InitializeDBCommand
        return InitializeDBCommand

    def _makeOne(self):
        cmd = self._getTargetClass()([])
        return cmd

    def test_run_no_args(self):
        """ Test the `run` method without positional argument."""
        # no args must error code 2 (and display an help message)
        command = self._makeOne()
        result = command.run()
        self.assertEqual(result, 2)
        self.assertEqual(self.output.getvalue()[0:6], "usage:")

    def test_run_config_uri(self):
        """ Test the `run` method with a `config_uri` positional argument."""
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        result = command.run()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database initialization done.")

    def test_initialize_db_config_uri(self):
        """ Test than the `initialize_db` method create the database."""
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        result = command.initialize_db()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database initialization done.")

    def test_initialize_db_default_values(self):
        """ Test than the `initialize_db` method add the default values to the
        initialized database.
        """
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        command.initialize_db()
        from anuket.models.auth import AuthUser
        user = self.DBSession.query(AuthUser).filter_by().first()
        self.assertEqual(user.username, u'admin')
        self.assertTrue(AuthUser.check_password(u'admin', u'admin'))
        self.assertEqual(user.group.groupname, u'admins')

    def test_initialize_db_with_revision(self):
        """ Test than the `initialize_db` method fail if the database is
        already versioned.
        """
        import transaction
        from anuket.models.migration import Migration
        version_table.create(self.engine)
        with transaction.manager:
            alembic_version = Migration()
            alembic_version.version_num = u'revid'
            self.DBSession.add(alembic_version)
        self.DBSession.remove()

        command = self._makeOne()
        command.args.config_uri = self.config_uri
        result = command.initialize_db()
        self.assertEqual(result, 1)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "This database is versioned. "
                         "Use the upgrade script instead!")

    def test_initialize_db_integrity_error(self):
        """ Test than the `initialize_db` method fail if an ``IntegrityError``
        occur because there is already an `admins` group in the database.
        """
        import transaction
        from anuket.models.auth import AuthGroup
        Base.metadata.create_all()
        with transaction.manager:
            admins_group = AuthGroup()
            admins_group.groupname = u'admins'
            self.DBSession.add(admins_group)
        self.DBSession.remove()

        command = self._makeOne()
        command.args.config_uri = self.config_uri
        result = command.initialize_db()
        self.assertEqual(result, 1)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "There is already a database. "
                         "Use the upgrade script instead!")


class TestInitializeDBmain(AnuketScriptTestCase):
    """ Test for the `main` function of the `initializedb` the script."""
    def _callFUT(self, argv):
        from anuket.scripts.initializedb import main
        return main(argv)

    def test_main(self):
        """ Test than the `main` function return the help message by default.
        """
        # same as the `run` method without argument
        result = self._callFUT([])
        self.assertEqual(result, 2)
        self.assertEqual(self.output.getvalue()[0:6], "usage:")
