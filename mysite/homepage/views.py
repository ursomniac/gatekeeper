from django.views.generic import DetailView, TemplateView, View

from .models import Homepage
from gatekeeper.mixins import GatekeeperSerialMixin

class HomepageDetailView(GatekeeperSerialMixin, DetailView):
    model = Homepage
    template_name = 'homepage/homepage_detail.html'
    context_object_name = 'homepage'

    def get_context_data(self, **kwargs):
        context = super(HomepageDetailView, self).get_context_data(**kwargs)
        context['pk'] = self.object.pk
        context['i_am_the_home_page'] = True
        return context

    