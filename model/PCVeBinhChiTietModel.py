from django.db import models
from .PCVeBinhModel import PCVeBinhModel
from .ChienSiModel import ChienSiModel


class PCVeBinhChiTietModel(models.Model):
    PCVB = models.ForeignKey(PCVeBinhModel, on_delete=models.PROTECT)
    ChienSi = models.ForeignKey(ChienSiModel, on_delete=models.PROTECT)

