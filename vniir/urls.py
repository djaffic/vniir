from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from search.views import SearchView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
    path('', include('departments.urls')),
    path('', include('standards.urls')),
    path('', include('staticpages.urls')),
    path('', include('search.urls')),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)