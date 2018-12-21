from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def standards_and_standards_types_list(request):
    standards = Standard.objects.all()
    standards_types = Standarts_Type.objects.all().order_by("id")
    context = {
        "standards": standards,
        "standards_types": standards_types
    }
    return render(request, "standards/standards_list.html", context)


def standard_detail(request, slug):
    standard = get_object_or_404(Standard, slug=slug)
    # standards_type = get_object_or_404(Standarts_Type, title=standard.standards_type)
    filtered_standards = Standard.objects.filter(standards_type__exact=standard.standards_type).order_by("id")

    context = {
        "filtered_standards": filtered_standards,
        "standard": standard,
        # "standards_type": standards_type
    }
    return render(request, "standards/standard_detail.html", context)

# def standards_type_detail(request, slug):
#     standards_type = get_object_or_404(Standarts_Type, slug=slug)
#     context = {
#         "standards_type": standards_type
#     }
#     return render(request, "standards/standards_list.html", context)