from django.db import models
from .CaGacVBModel import CaGacVBModel
from .PCGacNgayModel  import PCGacNgayModel


class PCVeBinhModel(models.Model):
    Ca = models.ForeignKey(CaGacVBModel,on_delete=models.PROTECT)
    NgayCong = models.ForeignKey(PCGacNgayModel,on_delete=models.CASCADE)

