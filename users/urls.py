from django.contrib.auth import views as auth_views
from django.urls import path
from .views import settings_view, profile_view

app_name = "users"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("settings/", settings_view, name="settings"),
    path("profile/<str:username>/", profile_view, name="profile"),
]
