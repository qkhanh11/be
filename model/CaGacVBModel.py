from django.db import models


class CaBacVCModel(models.Model):
    Ca = models.IntegerField()
    TGBatDau = models.TimeField()
    TGKetThuc = models.TimeField()