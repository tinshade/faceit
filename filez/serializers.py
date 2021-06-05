from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import FilesData
User = get_user_model()

class FilezDataSerializer(ModelSerializer):
    class Meta:
        model = FilesData
        fields = ('user','file_id','file_owner','file_name','file_ext','file_size','file_og_location','file_og_checksum','file_enc_checksum','date_secured','purge_scheduled','enc_level', 'month')