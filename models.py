# proctoring/models.py

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def _str_(self):
        return f"{self.user.username} - {self.role}"

class Violation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    frame = models.ImageField(upload_to='violations/')

    def _str_(self):
        return f"{self.user.username} - {self.reason} at {self.timestamp}"