from django.db import models
from .VienChucQPModel import VienChucQPModel
from .TheVienChucModel import TheVienChucModel
from .CongGacModel import CongGacModel


class LSRaVaoVCModel(models.Model):
    VienChuc = models.ForeignKey(VienChucQPModel,on_delete=models.CASCADE)
    SoThe = models.ForeignKey(TheVienChucModel,on_delete=models.PROTECT)
    ThoiGian = models.DateTimeField()
    TrangThai = models.BooleanField()
    Cong = models.ForeignKey(CongGacModel,on_delete=models.PROTECT)