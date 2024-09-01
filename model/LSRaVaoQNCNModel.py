from django.db import models
from .QNCNModel import QNCNModel
from .TheQNCNModel import TheQNCNModel
from .CongGacModel import CongGacModel


class LSRaVaoQNCNModel(models.Model):
    QNCN = models.ForeignKey(QNCNModel,on_delete=models.CASCADE)
    SoThe = models.ForeignKey(TheQNCNModel,on_delete=models.PROTECT)
    ThoiGian = models.DateTimeField()
    TrangThai = models.BooleanField()
    Cong = models.ForeignKey(CongGacModel,on_delete=models.PROTECT)