from django.urls import path
from search.views import SearchView

urlpatterns = [
    path('search/', SearchView.as_view(), name="search"),
]