from django.db import models
from django import forms
from Session.models import Session
# Create your models here.


class Interview(models.Model):
    title=models.CharField(max_length=500)
    date=models.DateField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    def __str__(self):
        return self.title