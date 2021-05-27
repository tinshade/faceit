from rest_framework import serializers
from .models import Inquiry

class AskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'
