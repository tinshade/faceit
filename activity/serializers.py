from rest_framework.serializers import ModelSerializer
from .models import ActivityLog

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = ('user','month', 'times_used')