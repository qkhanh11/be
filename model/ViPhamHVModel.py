from django.db import models
from .LoiViPhamModel import LoiViPhamModel
from .HocVienModel import HocVienModel
from .CongGacModel import CongGacModel


class ViPhamHVModel(models.Model):
    LoiViPham = models.ForeignKey(LoiViPhamModel,on_delete=models.CASCADE)
    HocVien = models.ForeignKey(HocVienModel,on_delete=models.CASCADE)
    ThoiGian = models.DateTimeField()
    Cong = models.ForeignKey(CongGacModel,on_delete=models.PROTECT)
    GhiChu = models.CharField(max_length=255)