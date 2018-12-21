from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/', get_page, name="get_page_url"),
    # path('files/<slug:slug>', get_file, name="get_file_url")
]