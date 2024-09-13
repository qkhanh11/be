from django.db import models
from .QNCNModel import QNCNModel
from .CVQNCNModel import CVQNCNModel


class QNCN_CVModel(models.Model):
    QNCN = models.ForeignKey(QNCNModel,on_delete=models.CASCADE)
    CV = models.ForeignKey(CVQNCNModel,on_delete=models.PROTECT)
    TuNgay = models.DateField()
    DenNgay = models.DateField(null=True)