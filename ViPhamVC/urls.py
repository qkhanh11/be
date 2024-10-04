from django.urls import path
from . import views

app_name = "ViPhamVC"

urlpatterns = [
    path('ThemViPhamVC/',views.ThemViPhamVC,name="ThemViPhamVC"),
    # path('RaVaoSQDacBiet/',views.RaVaoSQDacBiet,name="RaVaoSQDacBiet"),
    path('TatCaViPhamVC/',views.TatCaViPhamVC,name="TatCaViPhamVC"),
    path('SuaViPhamVC/<int:id>',views.SuaViPhamVC,name="SuaViPhamVC"),
    path('XoaViPhamVC/<int:id>',views.XoaViPhamVC,name="XoaViPhamVC"),
    path('ChiTietViPhamVC/<int:id>',views.ChiTietViPhamVC,name="ChiTietViPhamVC"),
    path('ViPhamVC/<int:id>',views.ViPhamVC,name="ViPhamVC"),
    # path('SuaRaVaoSQ/<int:id>',views.SuaRaVaoSQ,name="SuaRaVaoSQ"),
    # path('ThemBanGhi/',views.ThemBanGhi,name="ThemBanGhi"),
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