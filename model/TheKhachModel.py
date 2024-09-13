from django.db import models


class TheKhachModel(models.Model):
    SoThe = models.CharField(max_length=5)
    TrangThai = models.BooleanField(default=True)
    DangSuDung = models.BooleanField(default=False)

    def __str__(self):
        return str(self.SoThe)