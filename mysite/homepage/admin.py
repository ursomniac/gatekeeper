from django.contrib import admin
from .models import Homepage
from gatekeeper.admin import GatekeeperSerialAdmin

class HomepageAdmin(GatekeeperSerialAdmin):
    model = Homepage
    list_display = ['pk', 'title',]
    list_display_links = ['pk', 'title']
    
    fieldsets = [
        (None, {
            'fields': (
                'title',
            ),
        }),
    ]
    
admin.site.register(Homepage, HomepageAdmin)
