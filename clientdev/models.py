from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
class PrimaryDevice(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	architecture = models.CharField(max_length=20, blank=True, null=True)
	hostname = models.CharField(max_length=20, blank=True, null=True)
	platform = models.CharField(max_length=20, blank=True, null=True)
	release = models.CharField(max_length=20, blank=True, null=True)
	version = models.CharField(max_length=50, blank=True, null=True)
	timesOpened = models.CharField(max_length=20, blank=True, null=True)
	mac_pc = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
	 return f"{self.user}'s Device Details"