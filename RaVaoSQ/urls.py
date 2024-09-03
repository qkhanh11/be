from django.urls import path
from . import views

app_name = "RaVaoSQ"

urlpatterns = [
    path('RaVaoSQ/',views.RaVaoSQ,name="RaVaoSQ"),
    path('RaVaoSQDacBiet/',views.RaVaoSQDacBiet,name="RaVaoSQDacBiet"),
    path('lay_lich_su_ra_vao/',views.lay_lich_su_ra_vao,name="lay_lich_su_ra_vao"),
    # path('XemTatCaTrucBan/',views.XemTatCaTrucBan,name="XemTatCaTrucBan"),
    # path('XemChiTietTrucBan/<int:id>',views.XemChiTietTrucBan,name="XemChiTietTrucBan"),
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