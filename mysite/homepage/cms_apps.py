from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

@apphook_pool.register
class HomepageApp(CMSApp):
    #app_name = 'homepage'
    name = _("Home Page App")
    #urls = ["worldchannel2.apps.homepage.urls"]
    
    def get_urls(self, page=None, language=None, **kwargs):
        return ["worldchannel2.apps.homepage.urls"]