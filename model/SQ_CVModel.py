from django.db import models
from .SiQuanModel import SiQuanModel
from .CVSiQuanModel import CVSiQuanModel


class SQ_CVModel(models.Model):
    SQ = models.ForeignKey(SiQuanModel,on_delete=models.CASCADE)
    CV = models.ForeignKey(CVSiQuanModel,on_delete=models.PROTECT)
    TuNgay = models.DateField()
    DenNgay = models.DateField(null=True)