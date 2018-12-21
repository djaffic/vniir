from django.shortcuts import render, get_object_or_404
from departments.models import *


def department_detail(request, slug):
    departments = Department.objects.all()
    department = get_object_or_404(Department, slug=slug)
    context = {
        "departments": departments,
        "department": department
    }
    print()
    print(context)
    print()
    return render(request, "departments/department_detail.html", context)


def departments_list(request):
    departments = Department.objects.all()
    context = {
        "departments": departments
    }
    return render(request, "departments/departments_list.html", context)


def managements_list(request):
    managements = Management.objects.all().order_by("id")
    context = {
        "managements": managements
    }
    return render(request, "departments/managements_list.html", context)


def management_detail(request, slug):
    management = get_object_or_404(Management, slug=slug)
    context = {
        "management": management
    }
    return render(request, "departments/management_detail.html", context)
