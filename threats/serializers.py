from rest_framework.serializers import ModelSerializer
from .models import Threat

class ThreatSerializer(ModelSerializer):
    class Meta:
        model = Threat
        fields = ('user','threat_name', 'month')