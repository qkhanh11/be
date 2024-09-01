from django.db import models
from .SiQuanModel import SiQuanModel


class PCTrucBanModel(models.Model):
    Ngay = models.DateField()
    TBTruong = models.ForeignKey(SiQuanModel,on_delete=models.PROTECT, related_name='pctrucban_tbp')
    TBPho = models.ForeignKey(SiQuanModel,on_delete=models.PROTECT, related_name='pctrucban_tbt')