from django.db import models
from bars.models import Bar

class Event(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
