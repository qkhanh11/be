from django.db import models
from .QuyenModel import QuyenModel


class ThoiGianQuyenModel(models.Model):
    # Định nghĩa các lựa chọn cho trường Thu
    NGAY_CHOICES = [
        (0, 'Thứ 2'),
        (1, 'Thứ 3'),
        (2, 'Thứ 4'),
        (3, 'Thứ 5'),
        (4, 'Thứ 6'),
        (5, 'Thứ 7'),
        (6, 'Chủ nhật')
    ]

    Quyen = models.ForeignKey(QuyenModel, on_delete=models.CASCADE)
    Thu = models.IntegerField(choices=NGAY_CHOICES)
    TGRa = models.TimeField()
    TGVao = models.TimeField()