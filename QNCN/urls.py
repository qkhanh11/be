from django.urls import path
from . import views

app_name = "QNCN"

urlpatterns = [
    path('them/',views.ThemQNCN,name="ThemSQ"),
    path('sua/<int:id>',views.SuaQNCN,name="SuaSiQuan"),
    path('xoa/<int:id>',views.XoaQNCN,name="SuaSiQuan"),
    path('timqncn/',views.TimQNCN,name="TimSiQuan"),
    path('xemlsdv/<int:id>',views.LSDV,name="LichSuDonViSQ"),
    path('xemlscv/<int:id>',views.LSCV,name="LichSuChucVuSQ"),
    path('thongtinchitiet/<int:id>',views.ThongTinChiTiet,name="ThongTinChiTietSQ"),
    path('LayTenQNCNTuMa/',views.LayTenQNCNTuMa,name="LayTenSQTuMa"),
    path('DSTiepKhachQNCN/<int:id>',views.DSTiepKhachQNCN,name="DSTiepKhachSQ"),
]