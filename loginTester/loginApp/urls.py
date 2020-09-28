# from django.urls import path
from django.urls import include, path
from .views import HomePageView
# from django.views.generic.base import TemplateView

urlpatterns = [
    path('accounts', include('django.contrib.auth.urls')),
    path('', HomePageView.as_view(), name='home'), #class_based => as_view
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]