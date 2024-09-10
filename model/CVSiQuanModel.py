from django.db import models
from .CapDonViModel import CapDonViModel


class CVSiQuanModel(models.Model):
    TenChucVu = models.CharField(max_length=50)
    id_CapNhomDonVi = models.ForeignKey(CapDonViModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.TenChucVu