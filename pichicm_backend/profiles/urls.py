from django.urls import path

from pichicm_backend.profiles.apis import RetreiveUpdateProfileApi

urlpatterns = [
    path("", RetreiveUpdateProfileApi.as_view()),
]