from django.db import models

class Inquiry(models.Model):
    contact_name = models.CharField(max_length=50, blank=False)
    contact_email = models.EmailField(blank=False)
    contact_subject = models.CharField(max_length=100, blank=False)
    contact_message = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return f"{contact_name}'s Question"
