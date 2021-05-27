from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import DeviceData
User = get_user_model()

class DeviceDataSerializer(ModelSerializer):
    class Meta:
        model = DeviceData
        fields = ('user','architecture','hostname','platform','release','version','timesOpened','mac_pc',)
