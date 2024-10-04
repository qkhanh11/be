from django.urls import path
from . import views

app_name = "TheRaVao"

urlpatterns = [
    path('ThemTheSQ/',views.ThemTheSQ,name="ThemTheSQ"),
    path('ThemTheQNCN/',views.ThemTheQNCN,name="ThemTheQNCN"),
    path('ThemTheVC/',views.ThemTheVC,name="ThemTheVC"),
    path('KTTheSQ/<int:id>',views.KTTheSQ,name="KTTheSQ"),
    path('KTTheQNCN/<int:id>',views.KTTheQNCN,name="KTTheQNCN"),
    path('KTTheVC/<int:id>',views.KTTheVC,name="KTTheVC"),
    path('HuyTheSQ/<int:id>',views.HuyTheSQ,name="HuyTheSQ"),
    path('HuyTheQNCN/<int:id>',views.HuyTheQNCN,name="HuyTheQNCN"),
    path('HuyTheVC/<int:id>',views.HuyThevc,name="HuyThevc"),
    path('ThemNamTheSQ/',views.ThemNamTheSQ,name="ThemNamTheSQ"),
    path('TenSQTuThe/',views.TenSQTuThe,name="TenSQTuThe"),
    # path('xemlsdv/<int:id>',views.LSDV,name="LichSuDonViSQ"),
    # path('xemlscv/<int:id>',views.LSCV,name="LichSuChucVuSQ"),
    # path('thongtinchitiet/<int:id>',views.ThongTinChiTiet,name="ThongTinChiTietSQ"),
]