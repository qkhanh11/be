from django.db import models
from .TheQNCNModel import TheQNCNModel


class TheQNCNNamModel(models.Model):
    The = models.ForeignKey(TheQNCNModel,on_delete=models.CASCADE)
    Nam =  models.PositiveIntegerField()