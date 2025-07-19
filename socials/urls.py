from django.urls import path
from .views import feed

app_name = "socials"

urlpatterns = [
    path("", feed, name="feed"),
]
