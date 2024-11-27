from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('scorekeeper', 'Scorekeeper'),
        ('general_user', 'General User'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='general_user')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
