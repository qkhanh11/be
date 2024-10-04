from django.urls import path
from . import views

app_name = "RaVaoQNCN"

urlpatterns = [
    path('RaVaoQNCN/',views.RaVaoQNCN,name="RaVaoQNCN"),
    path('RaVaoSQDacBiet/',views.RaVaoQNCNDacBiet,name="RaVaoSQDacBiet"),
    path('lay_lich_su_ra_vao/',views.lay_lich_su_ra_vao,name="lay_lich_su_ra_vao"),
    path('LSRaVaoQNCN/<int:id>',views.LSRaVaoQNCN,name="LSRaVaoQNCN"),
    path('ChiTiet/<int:id>',views.ChiTiet,name="ChiTiet"),
    path('XoaRaVaoQNCN/<int:id>',views.XoaRaVaoQNCN,name="XoaRaVaoQNCN"),
    path('SuaRaVaoQNCN/<int:id>',views.SuaRaVaoQNCN,name="SuaRaVaoQNCN"),
    path('ThemBanGhi/',views.ThemBanGhi,name="ThemBanGhi"),
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