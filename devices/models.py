from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
class DeviceDetail(models.Model):
	user = models.CharField(max_length=20, blank=True, null=True)   
	password = models.CharField(max_length=30, blank=True, null=True)
	device_os = models.CharField(max_length=30, blank=True, null=True)
	device_name = models.CharField(max_length=30, blank=True, null=True)
	device_build = models.CharField(max_length=30, blank=True, null=True)
	device_mac = models.CharField(max_length=25, blank=True, null=True)
	times_opened = models.PositiveIntegerField(default=1, blank=False, null=False)

	def __str__(self):
		return f"{self.user.username}'s_Details"