# -*- coding: utf-8 -*-
import os

from anuket.models import Base
from anuket.models.migration import version_table
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
        # drop then alembic_version table
        version_table.drop(self.engine)


    def test_01_database_initilization(self):
        """ Test than the `initialize_db` function create the database and add
        the default values.
        """
        from anuket.scripts.initializedb import initialize_db
        message = initialize_db(config_uri)
        from anuket.models import AuthUser
        user = self.DBSession.query(AuthUser).filter_by().first()
        self.assertEqual(user.username, u'admin')
        self.assertTrue(AuthUser.check_password(u'admin', u'admin'))
        self.assertEqual(user.group.groupname, u'admins')
        self.assertEqual(message, "Database initialization done.")


    def test_02_database_with_revision_must_fail(self):
        """ Test than the `initialize_db` fail if the database is versioned."""
        import transaction
        from anuket.models import Migration
        version_table.create(self.engine)
        with transaction.manager:
            alembic_version = Migration()
            alembic_version.version_num = 'revid'
            self.DBSession.add(alembic_version)
        self.DBSession.remove()

        from anuket.scripts.initializedb import initialize_db
        message = initialize_db(config_uri)
        self.assertEqual(message, "ERROR: This database is versioned. "
                        "Please use the upgrade script instead!")


    def test_03_database_integrity_error(self):
        """ Test than the `initialize_db` fail if an IntegrityError occur
        when there is already an 'admins' group in the database."""
        import transaction
        from anuket.models import AuthGroup
        Base.metadata.create_all()
        with transaction.manager:
            admins_group = AuthGroup()
            admins_group.groupname = u'admins'
            self.DBSession.add(admins_group)
        self.DBSession.remove()

        from anuket.scripts.initializedb import initialize_db
        message = initialize_db(config_uri)
        self.assertEqual(message, "ERROR: An IntegrityError have occured")
