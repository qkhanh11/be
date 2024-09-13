from django.db import models
from .DonViModel import DonViModel
from .CVSiQuanModel import CVSiQuanModel
from .CBHaSiQuanModel import CBHaSiQuanModel



class ChienSiModel(models.Model):
    HoTen = models.CharField(max_length=50)
    Ma = models.CharField(max_length=20)
    NgaySinh = models.DateField()
    DonVi = models.ForeignKey(DonViModel,on_delete=models.PROTECT)
    CapBac = models.ForeignKey(CBHaSiQuanModel,on_delete=models.PROTECT)
    NgayNhapNgu = models.DateField()
    SoCanCuoc = models.CharField(max_length=20)
    QueQuan = models.CharField(max_length=60)
    NoiO = models.CharField(max_length=60)
    TinhTrang = models.BooleanField(default=True)

