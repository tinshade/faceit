from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer, ImageField
from .models import UserProfile
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')



class UserProfileSerializer(ModelSerializer):
    #profile_image = ImageField(max_length=None, required=False, allow_empty_file=True, use_url = True)
    class Meta:
        model = UserProfile
        fields = ('phone','address','city','country','postal_code','bio','plan',)
