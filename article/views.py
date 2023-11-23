from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ArticleListview(TemplateView):
    template_name = "articles/list.html"

class ArticleCreateview(TemplateView):
    template_name = "articles/create.html"