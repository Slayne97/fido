# Internal
from apps.evaluations.models import Evaluation

# Django and DRF
from rest_framework import serializers


class EvaluationSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    score = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Evaluation
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
