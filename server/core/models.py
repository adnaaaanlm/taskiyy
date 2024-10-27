from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Task(models.Model):
    title = models.CharField(max_length=100)  # Titre de la tâche
    description = models.TextField(blank=True)  # Description de la tâche
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)  # Date de mise à jour
    due_date = models.DateTimeField(null=True, blank=True)  # Date d'échéance
    completed = models.BooleanField(default=False)  # Indicateur de tâche terminée
    canceled = models.BooleanField(default=False)  # Indicateur de tâche annulée
    priority = models.CharField(max_length=10, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
