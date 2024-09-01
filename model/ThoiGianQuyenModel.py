from django.db import models
from .QuyenModel import QuyenModel


class ThoiGianQuyenModel(models.Model):
    # Định nghĩa các lựa chọn cho trường Thu
    NGAY_CHOICES = [
        (0, 'Thứ Hai'),
        (1, 'Thứ Ba'),
        (2, 'Thứ Tư'),
        (3, 'Thứ Năm'),
        (4, 'Thứ Sáu'),
        (5, 'Thứ Bảy'),
        (6, 'Chủ Nhật')
    ]

    Quyen = models.ForeignKey(QuyenModel, on_delete=models.CASCADE)
    Thu = models.IntegerField(choices=NGAY_CHOICES)
    TGRa = models.TimeField()
    TGVao = models.TimeField()