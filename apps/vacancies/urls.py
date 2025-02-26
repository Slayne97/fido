from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/", include("apps.vacancies.api.urls")),
]
