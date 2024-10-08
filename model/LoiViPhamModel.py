from django.db import models


class LoiViPhamModel(models.Model):
    TenLoi = models.CharField(max_length=50)
    GiaiThich = models.CharField(max_length=255)
    TinhTrang = models.BooleanField(default=True)


    def __str__(self):
        return self.TenLoi