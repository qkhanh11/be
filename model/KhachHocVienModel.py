from django.db import models
from .HocVienModel import HocVienModel
from .KhachModel import KhachModel


class KhachHocVienModel(models.Model):
    HV = models.ForeignKey(HocVienModel,on_delete=models.CASCADE)
    Khach = models.ForeignKey(KhachModel,on_delete=models.PROTECT)
    ThoiGianBatDau = models.DateTimeField()
    ThoiGianKetThuc = models.DateTimeField(null=True)
    GhiChu = models.CharField(max_length=255,null=True)