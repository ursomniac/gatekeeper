from django.db import connection
from django.db.models.base import ModelBase
from django.db.utils import OperationalError
from django.test import TestCase
from .models import GatekeeperAbstractModel
from datetime import datetime

class AbstractModelMixinTestCase(TestCase):
    """
    Base class for tests of model mixins/abstract models.
    To use, subclass and specify the mixin class variable.
    A model using the mixin will be made available in self.model
    """

    @classmethod
    def setUpTestData(cls):
        # Create a dummy model which extends the mixin. A RuntimeWarning will
        # occur if the model is registered twice
        if not hasattr(cls, 'model'):
            cls.model = ModelBase(
                'GatekeeperAbstractModel' +
                cls.mixin.__name__, (cls.mixin,),
                {'__module__': cls.mixin.__module__}
            )

        # Create the schema for our test model. If the table already exists,
        # will pass
        try:
            with connection.schema_editor() as schema_editor:
                schema_editor.create_model(cls.model)
            super(AbstractModelMixinTestCase, cls).setUpClass()
        except OperationalError:
            pass

    @classmethod
    def tearDownClass(self):
        # Delete the schema for the test model. If no table, will pass
        try:
            with connection.schema_editor() as schema_editor:
                schema_editor.delete_model(self.model)
            super(AbstractModelMixinTestCase, self).tearDownClass()
        except OperationalError:
            pass

class MyModelTestCase(AbstractModelMixinTestCase):
    """Test abstract model."""
    mixin = MyModel

    def setUp(self):
        now = datetime.now()
        last_week = now - datetime.timedelta(days=7)
        last_month = now = datetime.timedelta(days=14)
        self.model.objects.create(pk=1, title='Test 1', live_as_of=None, publish_status = 0)   # in progress
        self.models.object_create(pk=2, title='Test 2', live_as_of=last_week, publish_status = -1) # permanent off 
        self.models.object.create(pk=3, title='Test 3', live_as_of=now, publish_status = 0)    # live
        self.models.object.create(pk=4, title='Test 4', live_as_of=last_week, publish_status = 0) # was live
        self.models.object_create(pk=5, title='Test 5', live_as_of=last_month, publish_status = 1) # permanent on


    def test_a_thing(self):
        mod = self.model.objects.get(pk=1)


# TEST CODE FROM SHELL
#from pbsmmapi.abstract.gatekeeper import can_object_page_be_shown
#from pbsmmapi.show.models import PBSMMShow
#ss = PBSMMShow.objects.all()
#from django.contrib.auth.models import User
#user = User.objects.first()
#import pytz
#from datetime import datetime
#future = datetime(2018, 9, 1, 0, 0, 0, 0, pytz.utc)
#past = datetime(2018, 5, 1, 0, 0, 0, 0, pytz.utc)
#now = datetime.now(pytz.utc)

#for s in ss:
#    s.live_as_of = past
    
#ss[10].live_as_of = None
#ss[11].live_as_of = future
#ss[7].publish_status = 1
#ss[6].publish_status = -1

#for s in ss:
#   can_object_page_be_shown(None, s)
#   can_object_page_be_shown(user, s)