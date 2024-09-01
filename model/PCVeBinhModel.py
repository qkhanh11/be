from django.db import models
from .CaGacVBModel import CaBacVCModel
from .CongGacModel  import CongGacModel


class PCVeBinhModel(models.Model):
    Ngay = models.DateField()
    Ca = models.ForeignKey(CaBacVCModel,on_delete=models.PROTECT)
    CongGac = models.ForeignKey(CongGacModel,on_delete=models.CASCADE)

