# Internal
from .views import EvaluationsListCreateView

# Django and DRF
from django.urls import path

urlpatterns = [
    path("evaluations/", EvaluationsListCreateView.as_view()),
]
