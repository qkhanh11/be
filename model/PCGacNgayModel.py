from django.db import models
from .CongGacModel  import CongGacModel


class PCGacNgayModel(models.Model):
    Ngay = models.DateField()
    CongGac = models.ForeignKey(CongGacModel,on_delete=models.CASCADE)