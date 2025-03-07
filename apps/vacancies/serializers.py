# Internal
from apps.vacancies.models import Vacancy

# Django and DRF
from rest_framework import serializers


class VacancySerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    salary = serializers.CharField(required=False)
    company = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Vacancy
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
