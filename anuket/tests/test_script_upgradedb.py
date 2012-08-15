# -*- coding: utf-8 -*-
""" Tests for the upgradedb script."""
import os

from anuket.tests import AnuketScriptTestCase


class TestUpgradeDBCommand(AnuketScriptTestCase):
    """ Tests for the `upgrade_db` and `run` methods."""
    def _getTargetClass(self):
        from anuket.scripts.upgradedb import UpgradeDBCommand
        return UpgradeDBCommand

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
        self.backup_file_fixture()
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        result = command.run()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database upgrade done.")

    def test_upgrade_db_config_uri(self):
        """ Test than `upgrade_db` method upgrade the database."""
        self.backup_file_fixture()
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        result = command.upgrade_db()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database upgrade done.")

    def test_upgrade_db_no_backup(self):
        """ Test than `upgrade_db` method fail if there is no database backup
        file.
        """
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        result = command.upgrade_db()
        self.assertEqual(result, 1)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "There is no up to date backup for the database. "
                         "Please use the backup script before upgrading!")

    def test_upgrade_db_force(self):
        """ Test than `upgrade_db` method upgrade the database if there is no
        database backup file and if the `force` option is set.
        """
        self.backup_file_fixture()
        command = self._makeOne()
        command.args.config_uri = self.config_uri
        command.args.force = True
        result = command.upgrade_db()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database upgrade done.")


class TestUpgradeDBmain(AnuketScriptTestCase):
    """ Test for the `main` function of the `upgradedb` the script."""
    def _callFUT(self, argv):
        from anuket.scripts.upgradedb import main
        return main(argv)

    def test_main(self):
        """ Test than the `main` function return the help message by default.
        """
        # same as the `run` method without argument
        result = self._callFUT([])
        self.assertEqual(result, 2)
        self.assertEqual(self.output.getvalue()[0:6], "usage:")
