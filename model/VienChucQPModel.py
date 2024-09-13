from django.db import models
from .NhomVCQPModel import NhomVCQPModel
from .DonViModel import DonViModel



class VienChucQPModel(models.Model):
    HoTen = models.CharField(max_length=50)
    NgaySinh = models.DateField()
    NhomVCQP = models.ForeignKey(NhomVCQPModel,on_delete=models.PROTECT)
    DonVi = models.ForeignKey(DonViModel,on_delete=models.PROTECT)
    NgayBatDauLamViec = models.DateField()
    SoCanCuoc = models.CharField(max_length=20)
    QueQuan = models.CharField(max_length=60)
    NoiO = models.CharField(max_length=60)
    TrangThai = models.BooleanField(default=True)

