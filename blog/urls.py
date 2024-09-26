from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name="articles"),
    path('articles/<slug:slug>', views.article_detail, name="article_detail"),
    path('article-search/', views.search, name="search")
]