#Internal
from apps.vacancies.models import Vacancy
from apps.vacancies.serializers import VacancySerializer

# Create your views here.
from rest_framework import generics

class VacanciesListCreateView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer