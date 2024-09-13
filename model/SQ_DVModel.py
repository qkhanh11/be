from django.db import models
from .SiQuanModel import SiQuanModel
from .DonViModel import DonViModel


class SQ_DVModel(models.Model):
    SQ = models.ForeignKey(SiQuanModel,on_delete=models.CASCADE)
    DV = models.ForeignKey(DonViModel,on_delete=models.PROTECT)
    TuNgay = models.DateField()
    DenNgay = models.DateField(null=True)