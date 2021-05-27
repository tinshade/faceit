from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
class FilezData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_id = models.PositiveIntegerField(blank=True, null=True)
    file_owner = models.CharField(max_length=100, blank=False, null=False)
    file_name = models.CharField(max_length=1000, blank=False, null=False)
    file_ext = models.CharField(max_length=90, blank=False, null=False)
    file_size = models.FloatField(blank=False, null=False)
    file_og_location = models.CharField(max_length=2000, blank=False, null=False)
    file_og_checksum = models.CharField(max_length=70, blank=False, null=False)
    file_enc_checksum = models.CharField(max_length=70, blank=False, null=False)
    date_secured = models.CharField(max_length = 100, blank=True)
    purge_scheduled = models.BooleanField(default=0, blank=False, null=False)
    enc_level = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.file_owner}'s_Files"
class FilesData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_id = models.PositiveIntegerField(blank=True, null=True)
    file_owner = models.CharField(max_length=100, blank=False, null=False)
    file_name = models.CharField(max_length=1000, blank=False, null=False)
    file_ext = models.CharField(max_length=90, blank=False, null=False)
    file_size = models.FloatField(blank=False, null=False)
    file_og_location = models.CharField(max_length=2000, blank=False, null=False)
    file_og_checksum = models.CharField(max_length=70, blank=False, null=False)
    file_enc_checksum = models.CharField(max_length=70, blank=False, null=False)
    date_secured = models.CharField(max_length = 100, blank=True)
    purge_scheduled = models.BooleanField(default=0, blank=False, null=False)
    enc_level = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.file_owner}'s_Files"