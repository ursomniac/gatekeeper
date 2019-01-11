from django.views.generic import DetailView

from .models import Homepage
from gatekeeper.mixins import GatekeeperSerialMixin

class HomepageDetailView(DetailView, GatekeeperSerialMixin):
    model = Homepage
    template_name = 'homepage/homepage_detail.html'
    context_object_name = 'homepage'
    
    def get_object(self, queryset=None):
        return super(HomepageDetailView, self).get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super(HomepageDetailView, self).get_context_data(**kwargs)
        context['i_am_the_home_page'] = True
        return context
        