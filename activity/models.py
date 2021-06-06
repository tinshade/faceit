from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=20, blank=True)
    times_used = models.IntegerField(blank=True)


    def __str__(self):
        return f"{self.user}'s Activity Log"