from django.db import models


class LoaiKhachModel(models.Model):
    TenLoaiKhach = models.CharField(max_length=50)
    TrangThai = models.BooleanField(default=True)