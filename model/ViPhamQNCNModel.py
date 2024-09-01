from django.db import models
from .LoiViPhamModel import LoiViPhamModel
from .QNCNModel import QNCNModel
from .CongGacModel import CongGacModel


class ViPhamQNCNModel(models.Model):
    LoiViPham = models.ForeignKey(LoiViPhamModel,on_delete=models.CASCADE)
    QNCN = models.ForeignKey(QNCNModel,on_delete=models.CASCADE)
    ThoiGian = models.DateTimeField()
    Cong = models.ForeignKey(CongGacModel,on_delete=models.PROTECT)
    GhiChu = models.CharField(max_length=255)