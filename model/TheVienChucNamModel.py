from django.db import models
from .TheVienChucModel import TheVienChucModel


class TheVienChucNamModel(models.Model):
    The = models.ForeignKey(TheVienChucModel,on_delete=models.CASCADE)
    Nam =  models.CharField(max_length=5)