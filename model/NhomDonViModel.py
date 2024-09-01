from django.db import models


class NhomDonViModel(models.Model):
    TenNhom = models.CharField(max_length=50)
    GhiChu = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.TenNhom