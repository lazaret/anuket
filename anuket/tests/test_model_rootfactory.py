# -*- coding: utf-8 -*-
from pyramid.security import Allow, Authenticated, ALL_PERMISSIONS

from anuket.tests import AnuketTestCase


class ModelRootFactoryTests(AnuketTestCase):
    """ Tests for the `RootFactory` model class."""

    def test_rootfactory(self):
        """ Test ACLs of the route factory."""
        from anuket.models import RootFactory
        view_acl = (Allow, Authenticated, 'view')
        admin_acl = (Allow, 'group:admins', ALL_PERMISSIONS)
        self.assertIn(view_acl, RootFactory.__acl__)
        self.assertIn(admin_acl, RootFactory.__acl__)



    #TODO also add tests for form schema
    #TODO finish view user tests
