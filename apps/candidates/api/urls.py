# Internal
from .views import CandidateRetrieveUpdateDestroyView, CandidateListCreateView

# Django and DRF
from django.urls import path

urlpatterns = [
    path("candidates/", CandidateListCreateView.as_view()),
    path("candidates/<int:pk>/", CandidateRetrieveUpdateDestroyView.as_view()),
]
