from django.db import models
from .QNCNModel import QNCNModel
from .KhachModel import KhachModel
from .TheKhachModel import TheKhachModel


class KhachQNCNModel(models.Model):
    QNCN = models.ForeignKey(QNCNModel,on_delete=models.CASCADE)
    TheKhach = models.ForeignKey(TheKhachModel,on_delete=models.PROTECT)
    Khach = models.ForeignKey(KhachModel,on_delete=models.PROTECT)
    ThoiGianBatDau = models.DateTimeField()
    ThoiGianKetThuc = models.DateTimeField(null=True)
    GhiChu = models.CharField(max_length=255,null=True)
    TraTheKhach = models.BooleanField(default=False)