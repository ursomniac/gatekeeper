from django.db import models
from django.utils.translation import ugettext_lazy as _
from gatekeeper.models import GatekeeperAbstractModel, GatekeeperSerialAbstractModel

class GateTestParallel(GatekeeperAbstractModel):
    title = models.CharField (
        _('Title'), max_length = 100, null = False
    )
    
class GateTestSerial(GatekeeperSerialAbstractModel):
    title = models.CharField (
        _('Title'), max_length = 100, null = False
    )