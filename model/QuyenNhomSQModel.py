from django.db import models
from .NhomSQModel import NhomSQModel
from .QuyenModel import QuyenModel


class QuyenNhomSQModel(models.Model):
    NhomSQ = models.ForeignKey(NhomSQModel,on_delete=models.CASCADE)
    Quyen = models.ForeignKey(QuyenModel,on_delete=models.CASCADE)