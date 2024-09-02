from django.urls import path
from . import views

app_name = "Truc"

urlpatterns = [
    path('ThemTrucBan/',views.ThemTrucBan,name="ThemTrucBan"),
    path('SuaTrucBan/<int:id>',views.SuaTrucBan,name="SuaTrucBan"),
    path('XoaTrucBan/<int:id>',views.XoaTrucBan,name="XoaTrucBan"),
    path('XemTatCaTrucBan/',views.XemTatCaTrucBan,name="XemTatCaTrucBan"),
    path('XemChiTietTrucBan/<int:id>',views.XemChiTietTrucBan,name="XemChiTietTrucBan"),
    # path('ThemTheVC/',views.ThemTheVC,name="ThemTheVC"),
    # path('KTTheSQ/<int:id>',views.KTTheSQ,name="KTTheSQ"),
    # path('KTTheQNCN/<int:id>',views.KTTheQNCN,name="KTTheQNCN"),
    # path('KTTheVC/<int:id>',views.KTTheVC,name="KTTheVC"),
    # path('HuyTheSQ/<int:id>',views.HuyTheSQ,name="HuyTheSQ"),
    # path('HuyTheQNCN/<int:id>',views.HuyTheQNCN,name="HuyTheQNCN"),
    # path('HuyThevc/<int:id>',views.HuyThevc,name="HuyThevc"),
    # path('ThemNamTheSQ/',views.ThemNamTheSQ,name="ThemNamTheSQ"),
    # path('xemlsdv/<int:id>',views.LSDV,name="LichSuDonViSQ"),
    # path('xemlscv/<int:id>',views.LSCV,name="LichSuChucVuSQ"),
    # path('thongtinchitiet/<int:id>',views.ThongTinChiTiet,name="ThongTinChiTietSQ"),
]