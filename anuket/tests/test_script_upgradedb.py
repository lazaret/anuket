# -*- coding: utf-8 -*-
import os
import sys

from StringIO import StringIO
from unittest import TestCase


here = os.path.dirname(__file__)
config_uri = os.path.join(here, '../../', 'test.ini')


class TestUpgradeDBCommand(TestCase):
    """ Tests for the `upgradedb` script."""

    def setUp(self):
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

        self.dummy_file_path = None

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout
        # delete the fixture file if any
        if self.dummy_file_path:
            try:
                os.remove(self.dummy_file_path)
            except OSError:
                pass

    def _getTargetClass(self):
        from anuket.scripts.upgradedb import UpgradeDBCommand
        return UpgradeDBCommand

    def _makeOne(self):
        cmd = self._getTargetClass()([])
        return cmd

    def _create_file_fixture(self):
        from datetime import date
        from pyramid.paster import get_appsettings
        settings = get_appsettings(config_uri)
        name = settings['anuket.brand_name']
        directory = settings['anuket.backup_directory']
        today = date.today().isoformat()
        filename = '{0}-{1}.sql.bz2'.format(name, today)
        self.dummy_file_path = os.path.join(directory, filename)
        dummy_file = open(self.dummy_file_path, 'w')
        dummy_file.close()

#TODO move fixture/setup/teardown to a testcase class

    def test_run_no_args(self):
        # no args must error code 2 (and display an help message)
        command = self._makeOne()
        result = command.run()
        self.assertEqual(result, 2)
        self.assertEqual(self.output.getvalue()[0:6], "usage:")

    def test_run_config_uri(self):
        self._create_file_fixture()
        command = self._makeOne()
        command.args.config_uri = config_uri
        result = command.run()
        self.assertEqual(result, 0)

    def test_upgrade_config_uri(self):
        self._create_file_fixture()
        command = self._makeOne()
        command.args.config_uri = config_uri
        result = command.upgrade_db()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database upgrade done.")

    def test_upgrade_no_backup(self):
        command = self._makeOne()
        command.args.config_uri = config_uri
        result = command.upgrade_db()
        self.assertEqual(result, 1)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "There is no up to date backup for the database. "
                         "Please use the backup script before upgrading!")

    def test_upgrade_force(self):
        self._create_file_fixture()
        command = self._makeOne()
        command.args.config_uri = config_uri
        command.args.force = True
        result = command.upgrade_db()
        self.assertEqual(result, 0)
        self.assertEqual(self.output.getvalue().rstrip("\n"),
                         "Database upgrade done.")


class Test_main(TestCase):
    def _callFUT(self, argv):
        from anuket.scripts.upgradedb import main
        return main(argv)

    def test_main(self):
        result = self._callFUT([])
        self.assertEqual(result, 2)
