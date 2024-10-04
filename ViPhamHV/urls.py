from django.urls import path
from . import views

app_name = "ViPhamHV"

urlpatterns = [
    path('ThemViPhamHV/',views.ThemViPhamHV,name="ThemViPhamHV"),
    # path('RaVaoSQDacBiet/',views.RaVaoSQDacBiet,name="RaVaoSQDacBiet"),
    path('TatCaViPhamHV/',views.TatCaViPhamHV,name="TatCaViPhamHV"),
    path('SuaViPhamHV/<int:id>',views.SuaViPhamHV,name="SuaViPhamHV"),
    path('XoaViPhamHV/<int:id>',views.XoaViPhamHV,name="XoaViPhamHV"),
    path('ChiTietViPhamHV/<int:id>',views.ChiTietViPhamHV,name="ChiTietViPhamHV"),
    path('ViPhamHV/<int:id>',views.ViPhamHV,name="ViPhamVC"),
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