from django.urls import path
from .views import HomepageDetailView

urlpatterns = (
    path('', HomepageDetailView.as_view(), name='homepage-live'),
    path('homepage/<int:pk>/', HomepageDetailView.as_view(), name='homepage-detail'),
)
