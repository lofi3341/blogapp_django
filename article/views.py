from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Article
from .forms import ArticleForm

# Create your views here.
class ArticleListview(ListView):
    template_name = "articles/list.html"
    model = Article

class ArticleCreateview(CreateView):
    template_name = "articles/create.html"
    model = Article
    form_class = ArticleForm
    success_url = "/articles/"