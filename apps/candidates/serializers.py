# Internal
from apps.candidates.models import Candidate

# Django and DRF
from rest_framework import serializers


class CandidateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=False, allow_null=True)
    phone = serializers.CharField(required=False, allow_null=True)
    resume = serializers.FileField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Candidate
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
