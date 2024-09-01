from django.db import models
from .NhomVCQPModel import NhomVCQPModel
from .QuyenModel import QuyenModel


class QuyenNhomVCModel(models.Model):
    NhomVC = models.ForeignKey(NhomVCQPModel,on_delete=models.CASCADE)
    Quyen = models.ForeignKey(QuyenModel,on_delete=models.CASCADE)