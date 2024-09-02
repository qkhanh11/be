from django.db import models
from .CaGacVBModel import CaGacVBModel
from .CongGacModel  import CongGacModel


class PCVeBinhModel(models.Model):
    Ngay = models.DateField()
    Ca = models.ForeignKey(CaGacVBModel,on_delete=models.PROTECT)
    CongGac = models.ForeignKey(CongGacModel,on_delete=models.CASCADE)

