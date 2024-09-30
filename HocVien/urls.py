from django.urls import path
from . import views

app_name = "HocVien"

urlpatterns = [
    path('ThemHocVien/',views.ThemHocVien,name="ThemHocVien"),
    path('SuaHocVien/<int:id>',views.SuaHocVien,name="SuaHocVien"),
    path('XoaHocVien/<int:id>',views.XoaHocVien,name="SuaXoaHocVienSiQuan"),
    path('TatCaHocVien/',views.TatCaHocVien,name="TatCaHocVien"),
    path('TimHocVien/',views.TimHocVien,name="TimHocVien"),
    path('TimHVTrongDonVi/',views.TimHVTrongDonVi,name="TimHVTrongDonVi"),
    path('ChiTietHocVien/<int:id>',views.ChiTietHocVien,name="ChiTietHocVien"),
    # path('xemlscv/<int:id>',views.LSCV,name="LichSuChucVuSQ"),
    # path('thongtinchitiet/<int:id>',views.ThongTinChiTiet,name="ThongTinChiTietSQ"),
]