from django.urls import path, re_path, include
from django.conf import settings
from .views import manifest, offline, service_worker

app_name = "pwa"

urlpatterns = [
    re_path(r"^serviceworker\.js$", service_worker, name="serviceworker"),
    re_path(r"^manifest\.json$", manifest, name="manifest"),
    path("offline/", offline, name="offline"),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
