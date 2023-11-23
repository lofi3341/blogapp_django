from django.urls import path
from .views import ArticleListview, ArticleCreateview

urlpatterns = [
    path("", ArticleListview.as_view(), name="articles.list"),
    path("create/", ArticleCreateview.as_view(), name="articles.create"),
]