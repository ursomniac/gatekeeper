from django.views.generic import DetailView, ListView
from .models import Article
from gatekeeper.mixins import GatekeeperListMixin, GatekeeperDetailMixin

class ArticleListView(GatekeeperListMixin, ListView):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = 'articles'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        return context
        
class ArticleDetailView(GatekeeperDetailMixin, DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['pk'] = self.object.pk
        return context

    