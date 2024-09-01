from django.db import models


class TheKhachModel(models.Model):
    SoThe = models.IntegerField()
    TrangThai = models.BooleanField(default=True)
    DangSuDung = models.BooleanField(default=False)