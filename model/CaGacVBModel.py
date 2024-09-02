from django.db import models


class CaGacVBModel(models.Model):
    Ca = models.CharField(max_length=20)
    TGBatDau = models.TimeField()
    TGKetThuc = models.TimeField()
    TrangThai = models.BooleanField(default=True)