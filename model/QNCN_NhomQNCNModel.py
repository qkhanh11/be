from django.db import models
from .QNCNModel import QNCNModel
from .NhomQNCNModel import NhomQNCNModel


class QNCN_NhomQNCNModel(models.Model):
    QNCN = models.ForeignKey(QNCNModel,on_delete=models.CASCADE)
    NhomQNCN = models.ForeignKey(NhomQNCNModel,on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['QNCN', 'NhomQNCN'], name='unique_QNCN_NhomQNCN')
        ]


    