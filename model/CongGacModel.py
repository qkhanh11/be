from django.db import models


class CongGacModel(models.Model):
    TenCong = models.CharField(max_length=20)
    ViTri = models.CharField(max_length=50)