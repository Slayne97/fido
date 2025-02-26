# Internal
from .views import VacanciesListCreateView

# Django and DRF
from django.urls import path

urlpatterns = [
    path("vacancies/", VacanciesListCreateView.as_view()),
]
