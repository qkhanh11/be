from django.db import models
from .NhomQNCNModel import NhomQNCNModel
from .QuyenModel import QuyenModel


class QuyenNhomQNCNModel(models.Model):
    NhomQNCN = models.ForeignKey(NhomQNCNModel,on_delete=models.CASCADE)
    Quyen = models.ForeignKey(QuyenModel,on_delete=models.CASCADE)