# Internal
from apps.candidates.models import Candidate
from apps.candidates.serializers import CandidateSerializer

# Django and DRF
from rest_framework import generics


class CandidateListCreateView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
