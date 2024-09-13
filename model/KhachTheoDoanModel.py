from django.db import models
from .DonViModel import DonViModel
from .KhachModel import KhachModel


class KhachTheoDoanModel(models.Model):
    DonVi = models.ForeignKey(DonViModel,on_delete=models.CASCADE)
    KhachDaiDien = models.ForeignKey(KhachModel,on_delete=models.PROTECT)
    TinhTrang = models.BooleanField(default=True)