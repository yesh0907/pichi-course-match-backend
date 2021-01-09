from django.urls import path

from pichicm_backend.authentication.apis import (
    UserCreateApi,
    UserDestroyApi,
    UserLoginApi,
)

urlpatterns = [
    path("create/", UserCreateApi.as_view()),
    path("delete/", UserDestroyApi.as_view()),
    path("login/", UserLoginApi.as_view()),
]