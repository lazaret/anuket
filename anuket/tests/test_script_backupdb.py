# -*- coding: utf-8 -*-
import os

from anuket.tests import AnuketScriptTestCase


here = os.path.dirname(__file__)
config_uri = os.path.join(here, '../../', 'test.ini')


class TestBackupDBCommand(AnuketScriptTestCase):
    """ Tests for the `backup_db` and `run` methods."""

    def _getTargetClass(self):
        from anuket.scripts.backupdb import BackupDBCommand
        return BackupDBCommand

    def _makeOne(self):
        cmd = self._getTargetClass()([])
        return cmd


    def test_run_no_args(self):
        # no args must error code 2 (and display an help message)
        command = self._makeOne()
        result = command.run()
        self.assertEqual(result, 2)
        self.assertEqual(self.output.getvalue()[0:6], "usage:")

    def test_run_config_uri(self):
        command = self._makeOne()
        command.args.config_uri = config_uri
        result = command.run()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database backup done.")

#    def test_backup_no_args(self):
#        command = self._makeOne()
#        result = command.backup_db()
#        self.assertEqual(result, 0)
#TODO: take care of the case in the scripts

    def test_backup_config_uri(self):
        command = self._makeOne()
        command.args.config_uri = config_uri
        result = command.backup_db()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database backup done.")

    def test_backup_file_exist(self):
        # test than back exit if there is already a file
        self.backup_file_fixture()
        command = self._makeOne()
        command.args.config_uri = config_uri
        result = command.backup_db()
        self.assertEqual(result, 1)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
            "There is already a database backup with the same name!")

    def test_backup_overwrite(self):
        # test the overwrite option if the re is already a file
        self.backup_file_fixture()
        command = self._makeOne()
        command.args.config_uri = config_uri
        command.args.overwrite = True
        result = command.backup_db()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database backup done.")


class TestBackupDBmain(AnuketScriptTestCase):
    def _callFUT(self, argv):
        from anuket.scripts.backupdb import main
        return main(argv)

    def test_main(self):
        result = self._callFUT([])
        self.assertEqual(result, 2)
        self.assertEqual(self.output.getvalue()[0:6], "usage:")


#TODO: test the sqlite dump method
#TODO: test an unsuported database engine
