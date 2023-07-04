from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Home.urls")),
    path('', include("Supervisor.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
