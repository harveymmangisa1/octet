
from django.db import models
from django.utils.timezone import now

class Report(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]


class CyberReport(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.content[:50]  # Show first 50 characters


# Create your models here.
