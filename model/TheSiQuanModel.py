from django.db import models
from .SiQuanModel import SiQuanModel


class TheSiQuanModel(models.Model):
    SoThe = models.CharField(max_length=5, unique=True)
    SiQuan = models.ForeignKey(SiQuanModel,on_delete=models.CASCADE)
    TrangThai = models.BooleanField(default=True)