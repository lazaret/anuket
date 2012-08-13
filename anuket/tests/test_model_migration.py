# -*- coding: utf-8 -*-
""" Tests for the database migration model."""
import transaction

from sqlalchemy.exc import OperationalError

from anuket.tests import AnuketTestCase
from anuket.models import Base
from anuket.models.migration import Migration, version_table


class ModelMigrationTests(AnuketTestCase):
    """ Tests for the ``Migration`` model class."""
    def setUp(self):
        super(ModelMigrationTests, self).setUp()
        Base.metadata.drop_all()
        # drop the alembic_version table
        try:
            version_table.drop(self.engine)
        except OperationalError:  # pragma: no cover
            pass
        # create an alembic table fixture
        version_table.create(self.engine)
        with transaction.manager:
            alembic_version = Migration()
            alembic_version.version_num = 'revid'
        self.DBSession.add(alembic_version)

    def tearDown(self):
        super(ModelMigrationTests, self).tearDown()
        Base.metadata.drop_all()
        # drop the alembic_version table
        try:
            version_table.drop(self.engine)
        except OperationalError:  # pragma: no cover
            pass

    def test_Migration_columns(self):
        """ Test the ``Migration`` model class columns and types."""
        migration = self.DBSession.query(Migration).filter_by().first()
        if self.engine.dialect.name == 'sqlite':  # pragma: no cover
            # pysqlite driver always convert the strings collumns to unicode
            self.assertIsInstance(migration.version_num, unicode)
        else:  # pragma: no cover
            self.assertIsInstance(migration.version_num, str)
