from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import PrimaryDevice

class PrimaryDeviceSerializer(ModelSerializer):
    class Meta:
        model = PrimaryDevice
        fields = ('user','architecture','hostname','platform','release','version','timesOpened','mac_pc',)