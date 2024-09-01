from django.db import models
from .RNNgayHanhChinhModel import RNNgayHanhChinhModel


class RNNHCThoiGianModel(models.Model):
    RNNgayHanhChinh = models.ForeignKey(RNNgayHanhChinhModel,on_delete=models.CASCADE)
    DKRa = models.DateTimeField()
    DKVao = models.DateTimeField()
    TGRa = models.DateTimeField(null=True)
    TGVao = models.DateTimeField(null=True)