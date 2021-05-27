from django.db import models

# Create your models here.
class PrimaryDevice(models.Model):
	user = models.CharField(max_length=20, blank=True, null=True)
	architecture = models.CharField(max_length=20, blank=True, null=True)
	hostname = models.CharField(max_length=20, blank=True, null=True)
	platform = models.CharField(max_length=20, blank=True, null=True)
	release = models.CharField(max_length=20, blank=True, null=True)
	version = models.CharField(max_length=50, blank=True, null=True)
	timesOpened = models.CharField(max_length=20, blank=True, null=True)
	mac_pc = models.CharField(max_length=20, blank=True, null=True)