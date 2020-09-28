from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Django!")

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'