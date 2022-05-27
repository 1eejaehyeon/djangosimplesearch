
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from django.urls import path



urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "password_change/", PasswordChangeView.as_view(), name="password_change"
    ),
]