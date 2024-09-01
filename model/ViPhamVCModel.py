from django.db import models
from .LoiViPhamModel import LoiViPhamModel
from .VienChucQPModel import VienChucQPModel
from .CongGacModel import CongGacModel


class ViPhamVCModel(models.Model):
    LoiViPham = models.ForeignKey(LoiViPhamModel,on_delete=models.CASCADE)
    VienChuc = models.ForeignKey(VienChucQPModel,on_delete=models.CASCADE)
    ThoiGian = models.DateTimeField()
    Cong = models.ForeignKey(CongGacModel,on_delete=models.PROTECT)
    GhiChu = models.CharField(max_length=255)