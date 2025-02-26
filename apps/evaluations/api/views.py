#Internal
from apps.evaluations.models import Evaluation
from apps.evaluations.serializers import EvaluationSerializer

# Create your views here.
from rest_framework import generics

class EvaluationsListCreateView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer