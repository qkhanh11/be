from django.db import models
from .SiQuanModel import SiQuanModel
from .TheKhachModel import TheKhachModel
from .KhachModel import KhachModel


class KhachSiQuanModel(models.Model):
    SiQuan = models.ForeignKey(SiQuanModel,on_delete=models.CASCADE)
    TheKhach = models.ForeignKey(TheKhachModel,on_delete=models.PROTECT)
    Khach = models.ForeignKey(KhachModel,on_delete=models.PROTECT)
    ThoiGianBatDau = models.DateTimeField()
    ThoiGianKetThuc = models.DateTimeField(null=True)
    GhiChu = models.CharField(max_length=255,null=True)
    TraTheKhach = models.BooleanField(default=False)