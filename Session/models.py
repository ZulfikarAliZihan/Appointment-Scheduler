from django.db import models
from Application.models import Application

# Create your models here.

class Session(models.Model):
    title = models.CharField(max_length=100)
    date=  models.DateField()
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    def __str__(self):
        return self.title