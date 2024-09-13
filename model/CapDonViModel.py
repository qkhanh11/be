from django.db import models
from .NhomDonViModel import NhomDonViModel


class CapDonViModel(models.Model):
    id_NhomDonVi = models.ForeignKey(NhomDonViModel,on_delete=models.CASCADE)
    Ten = models.CharField(max_length=20)
    CapTren = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='CapNhomTren')
    TinhTrang = models.BooleanField(default=True)
    def __str__(self):
        return self.Ten