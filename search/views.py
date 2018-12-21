from django.shortcuts import render

# Create your views here.
from itertools import chain

from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView

from articles.models import Article
from standards.models import Standard
from departments.models import Department, Management


class SearchView(ListView):
    template_name = 'search/search.html'
    paginate_by = 10
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        print(query)
        if query is not None:
            articles_results = Article.objects.search(query)
            departments_results = Department.objects.search(query)
            managements_results = Management.objects.search(query)
            standards_results = Standard.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                articles_results,
                departments_results,
                managements_results,
                standards_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Article.objects.none()  # just an empty queryset as default