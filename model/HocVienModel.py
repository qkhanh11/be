from django.db import models
from .DonViModel import DonViModel
from .CBHaSiQuanModel import CBHaSiQuanModel



class HocVienModel(models.Model):
    HoTen = models.CharField(max_length=50)
    NgaySinh = models.DateField()
    MaQuanNhan =  models.CharField(max_length=20)
    DonVi = models.ForeignKey(DonViModel,on_delete=models.PROTECT)
    CapBac = models.ForeignKey(CBHaSiQuanModel,on_delete=models.PROTECT)
    NgayNhapNgu = models.DateField()
    SoCanCuoc = models.CharField(max_length=20)
    QueQuan = models.CharField(max_length=60)
    NoiO = models.CharField(max_length=60)

