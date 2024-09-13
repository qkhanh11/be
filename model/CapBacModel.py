from django.db import models


class CapBacModel(models.Model):
    TenCapBac = models.CharField(max_length=15)
    TinhTrang = models.BooleanField(default=True)

    def __str__(self):
        return self.TenCapBac