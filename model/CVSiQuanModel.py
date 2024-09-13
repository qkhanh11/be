from django.db import models
from .CapDonViModel import CapDonViModel


class CVSiQuanModel(models.Model):
    TenChucVu = models.CharField(max_length=50)
    id_CapDonVi = models.ForeignKey(CapDonViModel, on_delete=models.CASCADE)
    TinhTrang = models.BooleanField(default=True)

    def __str__(self):
        return self.TenChucVu