from django.db import models
from team.models import Team


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    teams = models.ManyToManyField(Team, related_name="members", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
