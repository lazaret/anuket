# -*- coding: utf-8 -*-
from unittest import TestCase



class testBackupDBCommand(TestCase):
    """ Tests for the `updatedb` script."""
#
#    def setUp(self):
#        pass
#
#    def tearDown(self):
#        pass
#
#
    def _getTargetClass(self):
        from anuket.scripts.backupdb import BackupDBCommand
        return BackupDBCommand

    def _makeOne(self, *args):
        cmd = self._getTargetClass()([])
        return cmd

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
        #TODO hide the help message

#    def test_backup_no_args(self):
#        command = self._makeOne()
#        backup = command.backup_db()
