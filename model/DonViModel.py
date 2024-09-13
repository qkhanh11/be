from django.db import models
from .CapDonViModel import CapDonViModel


class DonViModel(models.Model):
    TenDonVi = models.CharField(max_length=255)
    DiaDiem = models.CharField(max_length=50)
    MaDonVi = models.CharField(max_length=20, unique=True)
    id_DonViCapTren = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='don_vi_con')
    SoDienThoai = models.CharField(max_length=15)
    id_CapDonVi = models.ForeignKey(CapDonViModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.TenDonVi