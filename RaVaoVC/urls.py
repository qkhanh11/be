from django.urls import path
from . import views

app_name = "RaVaoVC"

urlpatterns = [
    path('RaVaoVC/',views.RaVaoVC,name="RaVaoVC"),
    path('RaVaoVCDacBiet/',views.RaVaoVCDacBiet,name="RaVaoVCDacBiet"),
    path('lay_lich_su_ra_vao/',views.lay_lich_su_ra_vao,name="lay_lich_su_ra_vao"),
    path('LSRaVaoVC/<int:id>',views.LSRaVaoVC,name="LSRaVaoVC"),
    path('ChiTiet/<int:id>',views.ChiTiet,name="ChiTiet"),
    path('XoaRaVaoVC/<int:id>',views.XoaRaVaoVC,name="XoaRaVaoVC"),
    path('SuaRaVaoVC/<int:id>',views.SuaRaVaoVC,name="SuaRaVaoVC"),
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