from django.contrib import admin
from .models import Article
from gatekeeper.admin import GatekeeperGenericAdmin

class ArticleAdmin(GatekeeperGenericAdmin):
    model = Article
    list_display = ['pk', 'title',]
    list_display_links = ['pk', 'title']
    
    fieldsets = [
        (None, {
            'fields': (
                'title',
            ),
        }),
    ]
    
admin.site.register(Article, ArticleAdmin)
