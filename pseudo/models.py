from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
class Pseudousers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.username}'s_Details"