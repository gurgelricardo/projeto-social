from django.urls import path
from relations.views import create_invite, register_by_invite

app_name = "relations"

urlpatterns = [
    path("", create_invite, name="create_invite"),
    path("<uuid:invite_id>/", register_by_invite, name="register_by_invite"),
]
