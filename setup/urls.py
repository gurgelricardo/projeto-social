from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("invite/", include("relations.urls")),
    path("accounts/", include("users.urls")),
    path("feed/", include("socials.urls")),
]
