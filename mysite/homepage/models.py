from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
import pytz
from gatekeeper.models import GatekeeperSerialAbstractModel

class Homepage(GatekeeperSerialAbstractModel):
    title = models.CharField (
        _('Title'),
        max_length = 200,
        null = False
    )
    date_created = models.DateTimeField (
        _('Date Created'),
        auto_now_add = True
    )
    
    date_modified = models.DateTimeField (
        _('Last Updated'),
        auto_now = True
    )

    def get_absolute_url(self):
        return reverse('homepage-detail', args=(self.pk))    
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'
   
    



