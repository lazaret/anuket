# -*- coding: utf-8 -*-
""" Tests for the `backupdb` script."""
import os

from anuket.tests import AnuketScriptTestCase


class TestBackupDBCommand(AnuketScriptTestCase):
    """ Tests for the `backup_db` and `run` methods."""
    def _getTargetClass(self):
        from anuket.scripts.backupdb import BackupDBCommand
        return BackupDBCommand

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
                         "Database backup done.")

    def test_backup_db_config_uri(self):
        """ Test than `backup_db` method create a backup file."""
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        result = command.backup_db()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database backup done.")

    def test_backup_db_file_exist(self):
        """ Test than `backup_db` method exit if there is already  a backup
        file.
        """
        self.backup_file_fixture()
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        result = command.backup_db()
        self.assertEqual(result, 1)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
            "There is already a database backup with the same name!")

    def test_backup_db_overwrite(self):
        """ Test than `backup_db` method create a backup file if there is
        already a backup file and if the `overwrite` option is set.
        """
        self.backup_file_fixture()
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        command.args.overwrite = True
        result = command.backup_db()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database backup done.")

    def test_dump_sqlite(self):
        """ Test the `dump_sqlite` method."""
        from sqlalchemy import engine_from_config
        engine = engine_from_config(self.settings, 'sqlalchemy.')
        connect_args = engine.url.translate_connect_args()
        command = self._makeOne()
        result = command.dump_sqlite(connect_args)
        self.assertIsInstance(result, unicode)


class TestBackupDBmain(AnuketScriptTestCase):
    """ Test for the `main` function of the `backupdb` the script."""
    def _callFUT(self, argv):
        from anuket.scripts.backupdb import main
        return main(argv)

    def test_main(self):
        """ Test than the `main` function return the help message by default.
        """
        # same as the `run` method without argument
        result = self._callFUT([])
        self.assertEqual(result, 2)
        self.assertEqual(self.output.getvalue()[0:6], "usage:")
