from django.db import models
from .VienChucQPModel import VienChucQPModel
from .NhomVCQPModel import NhomVCQPModel


class VC_NhomVCModel(models.Model):
    VienChuc = models.ForeignKey(VienChucQPModel,on_delete=models.CASCADE)
    NhomVC = models.ForeignKey(NhomVCQPModel,on_delete=models.CASCADE)