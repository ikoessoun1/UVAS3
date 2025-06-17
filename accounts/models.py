from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class TeamCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(TeamCategory, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('SUPER_ADMIN', 'Super Admin'),
        ('ADMIN', 'Admin'),
        ('LOW_LEVEL', 'Low Level'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='LOW_LEVEL')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
