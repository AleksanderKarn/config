
from django.urls import path
from catalog.views import home, contacts
from catalog.apps import CatalogConfig
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)