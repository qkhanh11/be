from django.db import models
from .LoiViPhamModel import LoiViPhamModel
from .SiQuanModel import SiQuanModel
from .CongGacModel import CongGacModel


class ViPhamSQModel(models.Model):
    LoiViPham = models.ForeignKey(LoiViPhamModel,on_delete=models.CASCADE)
    SiQuan = models.ForeignKey(SiQuanModel,on_delete=models.CASCADE)
    ThoiGian = models.DateTimeField()
    Cong = models.ForeignKey(CongGacModel,on_delete=models.PROTECT)
    GhiChu = models.CharField(max_length=255)