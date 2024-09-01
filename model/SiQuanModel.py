from django.db import models
from .NhomSQModel import NhomSQModel
from .DonViModel import DonViModel
from .CVSiQuanModel import CVSiQuanModel
from .CapBacModel import CapBacModel



class SiQuanModel(models.Model):
    HoTen = models.CharField(max_length=50)
    NgaySinh = models.DateField()
    MaQuanNhan =  models.CharField(max_length=20)
    DonVi = models.ForeignKey(DonViModel,on_delete=models.PROTECT)
    ChucVu = models.ForeignKey(CVSiQuanModel,on_delete=models.PROTECT)
    CapBac = models.ForeignKey(CapBacModel,on_delete=models.PROTECT)
    NhomSQ = models.ForeignKey(NhomSQModel,on_delete=models.PROTECT)
    NgayNhapNgu = models.DateField()
    SoCanCuoc = models.CharField(max_length=20)
    QueQuan = models.CharField(max_length=60)
    NoiO = models.CharField(max_length=60)

