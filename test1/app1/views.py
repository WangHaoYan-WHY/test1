from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HelloWorld(TemplateView):
    template_name = 'hello_word.html'