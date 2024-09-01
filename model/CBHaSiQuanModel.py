from django.db import models


class CBHaSiQuanModel(models.Model):
    TenCapBac = models.CharField(max_length=15)

    def __str__(self):
        return self.TenCapBac