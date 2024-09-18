from django.urls import path
from . import views

app_name = "Khach"

urlpatterns = [
    path('ThemTheKhach/',views.ThemTheKhach,name="ThemTheKhach"),
    path('HuyTheKhach/<int:id>',views.HuyTheKhach,name="HuyTheKhach"),
    path('LayTheKhach/',views.LayTheKhach,name="LayTheKhach"),
    path('ThemLoaiKhach/',views.ThemLoaiKhach,name="ThemLoaiKhach"),
    path('SuaLoaiKhach/<int:id>',views.SuaLoaiKhach,name="SuaLoaiKhach"),
    path('HuyLoaiKhach/<int:id>',views.HuyLoaiKhach,name="HuyLoaiKhach"),
    path('LayLoaiKhach/',views.LayLoaiKhach,name="LayLoaiKhach"),
    path('TiepKhachSQ/',views.TiepKhachSQ,name="TiepKhachSQ"),
    path('DangTiepKhachSQ/',views.DangTiepKhachSQ,name="DangTiepKhachSQ"),
    path('TraKhachSQ/<int:id>',views.TraKhachSQ,name="TraKhachSQ"),
    path('DanhSachTiepKhachSiQuan/',views.DanhSachTiepKhachSiQuan,name="TraKhachSQ"),
    path('danh_sach_the_khach/',views.danh_sach_the_khach,name="danh_sach_the_khach"),
    path('SuaTheKhach/<int:id>',views.SuaTheKhach,name="SuaTheKhach"),
    path('TraTheKhach/<int:id>',views.TraTheKhach,name="TraTheKhach"),
]