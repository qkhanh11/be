from django.db import models
from .DonViModel import DonViModel


class LSRaVaoHVModel(models.Model):
    DonVi = models.ForeignKey(DonViModel,on_delete=models.CASCADE)
    So = models.CharField(max_length=2)
    TGRa = models.DateTimeField()
    TGVao = models.DateTimeField(null=True)