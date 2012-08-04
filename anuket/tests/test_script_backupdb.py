# -*- coding: utf-8 -*-
import os

from unittest import TestCase


here = os.path.dirname(__file__)
config_uri = os.path.join(here, '../../', 'test.ini')


class testBackupDBCommand(TestCase):
    """ Tests for the `updatedb` script."""

    dummy_file_path = None
#
#    def setUp(self):
#        pass
#
    def tearDown(self):
        # delete the fixture file if any
        if self.dummy_file_path:
            try:
                os.remove(self.dummy_file_path)
            except OSError:
                pass
        #TODO, better do this as the file may stay after failed tests


    def _getTargetClass(self):
        from anuket.scripts.backupdb import BackupDBCommand
        return BackupDBCommand

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


#    def test_nothing(self):
#        command = self._makeOne()
#
#        result = command.run(quiet=True)
#        self.assertEqual(result, 2)
#
#

    def test_run_no_args(self):
        # no args must error code 2 (and display an help message)
        command = self._makeOne()
        result = command.run()
        self.assertEqual(result, 2)
#        #TODO hide the help message

#    def test_run_config_uri(self):
#        command = self._makeOne()
#        command.args.config_uri = config_uri
#        result = command.run()
#        self.assertEqual(result, 0)


#    def test_backup_no_args(self):
#        command = self._makeOne()
#        result = command.backup_db()
#        self.assertEqual(result, 0)
#TODO: take care of the case in the script ?

#    def test_backup_config_uri(self):
#        command = self._makeOne()
#        command.args.config_uri = config_uri
#        result = command.backup_db()
#        self.assertEqual(result, 0)

    def test_backup_file_exist(self):
        # test than back exit if there is already a file
        self._create_file_fixture()
        command = self._makeOne()
        command.args.config_uri = config_uri
        result = command.backup_db()
        self.assertEqual(result, 1)

    def test_backup_overwrite(self):
        # test the overwrite option if the re is already a file
        self._create_file_fixture()
        command = self._makeOne()
        command.args.config_uri = config_uri
        command.args.overwrite = True
        result = command.backup_db()
        self.assertEqual(result, 0)

#TODO: hide / check output messages
#TODO: test the verify_directory method
#TODO: test the sqlite dump method
#TODO: test an unsuported database engine
#TODO: test run
#TODO: test main

