from django.db import models
from .LoaiKhachModel import LoaiKhachModel


class KhachModel(models.Model):
    HoTenKhach = models.CharField(max_length=30)
    SoDinhDanh = models.CharField(max_length=15)
    Loai = models.ForeignKey(LoaiKhachModel, on_delete=models.CASCADE)
