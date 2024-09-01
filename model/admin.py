from django.contrib import admin
from .QuyenModel import QuyenModel
from .NhomSQModel import NhomSQModel
from .ThoiGianQuyenModel import ThoiGianQuyenModel
from .QuyenNhomSQModel import QuyenNhomSQModel
# Register your models here.



admin.site.register(QuyenModel)
admin.site.register(NhomSQModel)
admin.site.register(ThoiGianQuyenModel)
admin.site.register(QuyenNhomSQModel)