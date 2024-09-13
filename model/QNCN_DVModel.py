from django.db import models
from .QNCNModel import QNCNModel
from .DonViModel import DonViModel


class QNCN_DVModel(models.Model):
    QNCN = models.ForeignKey(QNCNModel,on_delete=models.CASCADE)
    DV = models.ForeignKey(DonViModel,on_delete=models.PROTECT)
    TuNgay = models.DateField()
    DenNgay = models.DateField(null=True)