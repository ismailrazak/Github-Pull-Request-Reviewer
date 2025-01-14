from rest_framework import serializers
from .models import AnalyzePRRequest


class AnalyzerPrRequestSerialzier(serializers.ModelSerializer):

    class Meta:
        model = AnalyzePRRequest
        fields = ['github_url','pr_number','github_token']