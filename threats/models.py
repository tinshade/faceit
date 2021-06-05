from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Threat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    threat_name = models.CharField(max_length=200, blank=True)
    month = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user}'s Threats"