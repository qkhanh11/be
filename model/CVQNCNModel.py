from django.db import models
from .CapNhomDonViModel import CapNhomDonViModel
from .NhomQNCNModel import NhomQNCNModel


class CVQNCNModel(models.Model):
    TenChucVu = models.CharField(max_length=50)
    id_CapNhomDonVi = models.ForeignKey(CapNhomDonViModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.TenChucVu