from django.urls import path
from standards.views import *

urlpatterns = [
    path('standards/', standards_and_standards_types_list, name="standards_and_standards_types_list_url"),
    path('standards/<slug:slug>/', standard_detail, name="standard_detail_url"),
    # path('standards-types/<slug:slug>/', standards_type_detail, name="standards_type_detail_url"),
]