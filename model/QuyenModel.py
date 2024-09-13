from django.db import models


class QuyenModel(models.Model):
    TenQuyen = models.CharField(max_length=50)
    GiaiThich = models.CharField(max_length=255,null=True)
    TinhTrang = models.BooleanField(default=True)