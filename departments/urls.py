from django.urls import path, include
from departments.views import *

urlpatterns = [
    path('departments/', departments_list, name="departments_list_url"),
    path('managements/', managements_list, name="managements_list_url"),
    path('managements/<slug:slug>', management_detail, name="management_detail_url"),
    path('departments/<slug:slug>/', department_detail, name="department_detail_url"),
]

