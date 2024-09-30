from django.db import models
from .NhomQNCNModel import NhomQNCNModel
from .DonViModel import DonViModel
from .CVQNCNModel import CVQNCNModel
from .CapBacModel import CapBacModel



class QNCNModel(models.Model):
    HoTen = models.CharField(max_length=50)
    NgaySinh = models.DateField()
    MaQuanNhan =  models.CharField(max_length=20)
    DonVi = models.ForeignKey(DonViModel,on_delete=models.PROTECT)
    ChucVu = models.ForeignKey(CVQNCNModel,on_delete=models.PROTECT)
    CapBac = models.ForeignKey(CapBacModel,on_delete=models.PROTECT)
    NhomQNCN = models.ForeignKey(NhomQNCNModel,on_delete=models.PROTECT)
    NgayNhapNgu = models.DateField()
    SoCanCuoc = models.CharField(max_length=20)
    QueQuan = models.CharField(max_length=60)
    NoiO = models.CharField(max_length=60)
    TrangThai = models.BooleanField(default=True)

