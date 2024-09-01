from django.db import models
from .VienChucQPModel import VienChucQPModel


class TheVienChucModel(models.Model):
    SoThe = models.CharField(max_length=5, unique=True)
    VienChuc = models.ForeignKey(VienChucQPModel,on_delete=models.CASCADE)
    TrangThai = models.BooleanField(default=True)