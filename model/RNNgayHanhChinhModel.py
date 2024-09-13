from django.db import models
from .HocVienModel import HocVienModel


class RNNgayHanhChinhModel(models.Model):
    HocVien = models.ForeignKey(HocVienModel,on_delete=models.CASCADE)
    LyDo = models.CharField(max_length=50)
    DiaDiem = models.CharField(max_length=255)
    TinhTrang = models.BooleanField(default=True)
    