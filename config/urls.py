from django.contrib import admin
from django.urls import path
from relations.views import create_invite, register_by_invite
from users.views import login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("invite/", create_invite, name="create_invite"),
    path("invite/<uuid:invite_id>/", register_by_invite, name="register_by_invite"),
]
