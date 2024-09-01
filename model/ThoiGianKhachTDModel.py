from django.db import models
from .KhachTheoDoanModel import KhachTheoDoanModel
from .SiQuanModel import SiQuanModel


class ThoiGianKhachTDModel(models.Model):
    DKVao = models.DateTimeField()
    DKRa = models.DateTimeField()
    TGVao = models.DateTimeField(null=True)
    TGRa = models.DateTimeField(null=True)
    SQDon = models.ForeignKey(SiQuanModel,on_delete=models.CASCADE,null=True)
    DoanKhach = models.ForeignKey(KhachTheoDoanModel,on_delete=models.PROTECT)