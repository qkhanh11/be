from django.db import models
from .KhachTheoDoanModel import KhachTheoDoanModel
from .KhachModel import KhachModel
from .TheKhachModel import TheKhachModel


class KhachTDChiTietModel(models.Model):
    TheKhach = models.ForeignKey(TheKhachModel,on_delete=models.PROTECT)
    Khach = models.ForeignKey(KhachModel,on_delete=models.PROTECT)
    DoanKhach = models.ForeignKey(KhachTheoDoanModel,on_delete=models.CASCADE)