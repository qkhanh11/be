from django.db import models
from .QNCNModel import QNCNModel


class TheQNCNModel(models.Model):
    SoThe = models.CharField(max_length=5, unique=True)
    QNCN = models.ForeignKey(QNCNModel,on_delete=models.CASCADE)
    TrangThai = models.BooleanField(default=True)