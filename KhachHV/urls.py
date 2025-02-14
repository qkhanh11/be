from django.urls import path
from . import views

app_name = "KhachHV"

urlpatterns = [
    path('TiepKhachHV/',views.TiepKhachHV,name="TiepKhachHV"),
    path('SuaTiepKhachHV/<int:id>',views.SuaTiepKhachHV,name="SuaTiepKhachSQ"),
    path('TraKhach/<int:id>',views.TraKhach,name="TraKhach"),
    path('DangTiepKhach/',views.DangTiepKhach,name="DangTiepKhach"),
    path('DanhSachTiepKhach/',views.DanhSachTiepKhach,name="DanhSachTiepKhach"),
    # path('SuaLoaiKhach/<int:id>',views.SuaLoaiKhach,name="SuaLoaiKhach"),
    path('XoaTiepKhachHV/<int:id>',views.XoaTiepKhachHV,name="XoaTiepKhachHV"),
    # path('LayLoaiKhach/',views.LayLoaiKhach,name="LayLoaiKhach"),
    # path('TiepKhachSQ/',views.TiepKhachSQ,name="TiepKhachSQ"),
    # path('DangTiepKhachSQ/',views.DangTiepKhachSQ,name="DangTiepKhachSQ"),
    # path('TraKhachSQ/<int:id>',views.TraKhachSQ,name="TraKhachSQ"),
    # path('DanhSachTiepKhachSiQuan/',views.DanhSachTiepKhachSiQuan,name="DanhSachTiepKhachSiQuan"),
    # path('danh_sach_the_khach/',views.danh_sach_the_khach,name="danh_sach_the_khach"),
    # path('SuaTheKhach/<int:id>',views.SuaTheKhach,name="SuaTheKhach"),
    # path('TraTheKhach/<int:id>',views.TraTheKhach,name="TraTheKhach"),
    # path('ThongKeKhachTrongNgay/',views.ThongKeKhachTrongNgay,name="ThongKeKhachTrongNgay"),
    # path('ThongKeTrongThang/',views.ThongKeTrongThang,name="ThongKeTrongThang"),
    # path('ThongKeTheoNam/',views.ThongKeTheoNam,name="ThongKeTheoNam"),
    # path('SuaTiepKhachSQ/<int:id>',views.SuaTiepKhachSQ,name="SuaTiepKhachSQ"),
    # path('ThemLSTiepKhachSQ/',views.ThemLSTiepKhachSQ,name="ThemLSTiepKhachSQ"),
    # path('TraTheKhachSQ/<int:id>',views.TraTheKhachSQ,name="TraTheKhachSQ"),
    # path('DaTraKhachSQ/',views.DaTraKhachSQ,name="DaTraKhachSQ"),
    # path('ChiTietTiepKhachSQ/<int:id>',views.ChiTietTiepKhachSQ,name="ChiTietTiepKhachSQ"),
]