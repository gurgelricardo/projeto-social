from django.contrib import admin
from django.urls import path, include
from socials.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("invite/", include("relations.urls")),
    path("accounts/", include("users.urls")),
]
