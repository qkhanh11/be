from django.db import models
from .SiQuanModel import SiQuanModel
from .NhomSQModel import NhomSQModel


class SQ_NhomSQModel(models.Model):
    SiQuan = models.ForeignKey(SiQuanModel,on_delete=models.CASCADE)
    NhomSiQuan = models.ForeignKey(NhomSQModel,on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['SiQuan', 'NhomSiQuan'], name='unique_SiQuan_NhomSiQuan')
        ]