from django.db import models
from .TheSiQuanModel import TheSiQuanModel


class TheSiQuanNamModel(models.Model):
    The = models.ForeignKey(TheSiQuanModel,on_delete=models.CASCADE)
    Nam =  models.PositiveIntegerField()