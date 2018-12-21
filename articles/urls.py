from django.urls import path
from articles.views import *

urlpatterns = [
    path('', last_articles, name="last_articles_url"),
    path('articles/', articles_list, name="articles_url"),
    path('articles/<int:pk>/', article_detail, name="article_detail_url"),
    path('tags/', tags_list, name="tags_list"),
    path('tags/<int:pk>/', tag_detail, name="tag_detail_url"),
]