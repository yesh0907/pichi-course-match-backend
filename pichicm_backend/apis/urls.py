from django.conf.urls import include
from django.urls import path

# All routes will fall under /api/ namespace
urlpatterns = [
    path("auth/", include("pichicm_backend.authentication.urls")),
    path("profile/", include("pichicm_backend.profiles.urls")),
]