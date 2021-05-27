from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import Pseudousers
User = get_user_model()

class PseudoSerializer(ModelSerializer):
    class Meta:
        model = Pseudousers
        fields = ('id','username','password','first_name','last_name','user')
