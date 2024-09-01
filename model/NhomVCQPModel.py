from django.db import models


class NhomVCQPModel(models.Model):
    TenNhom = models.CharField(max_length=50)

    def __str__(self):
        return self.TenNhom