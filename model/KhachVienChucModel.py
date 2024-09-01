from django.db import models
from .VienChucQPModel import VienChucQPModel
from .TheKhachModel import TheKhachModel
from .KhachModel import KhachModel


class KhachVienChucModel(models.Model):
    VienChuc = models.ForeignKey(VienChucQPModel,on_delete=models.CASCADE)
    TheKhach = models.ForeignKey(TheKhachModel,on_delete=models.PROTECT)
    Khach = models.ForeignKey(KhachModel,on_delete=models.PROTECT)
    ThoiGianBatDau = models.DateTimeField()
    ThoiGianKetThuc = models.DateTimeField(null=True)
    GhiChu = models.CharField(max_length=255)