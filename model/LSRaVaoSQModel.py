from django.db import models
from .SiQuanModel import SiQuanModel
from .TheSiQuanModel import TheSiQuanModel
from .CongGacModel import CongGacModel


class LSRaVaoSQModel(models.Model):
    SiQuan = models.ForeignKey(SiQuanModel,on_delete=models.CASCADE)
    SoThe = models.ForeignKey(TheSiQuanModel,on_delete=models.PROTECT)
    ThoiGian = models.DateTimeField()
    TrangThai = models.BooleanField()   #1 là Ra 0 là Vào
    Cong = models.ForeignKey(CongGacModel,on_delete=models.PROTECT)