# -*- coding: utf-8 -*-
import unittest
import transaction
from pyramid import testing

from wepwawet.models import DBSession


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from ..models import (
            Base,
#            MyModel,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
#        with transaction.manager:
#            model = MyModel(name='one', value=55)
#            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_my_view(self):
        from wepwawet.views.root import root_view
        request = testing.DummyRequest()
        info = root_view(request)
#        self.assertEqual(info['one'].name, 'one')
        #TODO change this beacause brand_name can be modified
#        self.assertEqual(info['brand_name'], 'Wepwawet')
