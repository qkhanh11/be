from django.db import models
from .VienChucQPModel import VienChucQPModel
from .DonViModel import DonViModel


class VC_DVModel(models.Model):
    VC = models.ForeignKey(VienChucQPModel,on_delete=models.CASCADE)
    DV = models.ForeignKey(DonViModel,on_delete=models.PROTECT)
    TuNgay = models.DateField()
    DenNgay = models.DateField(null=True)