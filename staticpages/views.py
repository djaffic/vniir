from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import Page, File

# Create your views here.
def get_page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    pages = Page.objects.all().filter(category=page.category).order_by("id")
    files = page.file_set.all().order_by("id")
    context = {
        "pages": pages,
        "page": page,
        "files": files
    }
    return  render(request, "staticpages/page_detail.html", context)

# def get_file(request, slug):
#     page = get_object_or_404(Page, slug=slug)
#     files = page.file_set.all().order_by("id")
#     context = {
#         'files': files
#     }
#     return render(request, "staticpages/page_detail.html", context)