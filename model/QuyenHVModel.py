from django.db import models
from .QuyenModel import QuyenModel


class QuyenHVModel(models.Model):
    Quyen = models.OneToOneField(QuyenModel,on_delete=models.CASCADE)