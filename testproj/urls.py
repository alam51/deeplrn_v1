from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("pwa.urls", namespace="pwa")),
    path("", include("pwa.urls")),
    path("", include("testproj.core.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]