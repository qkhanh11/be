from django.urls import path
from . import views

app_name = "ViPhamQNCN"

urlpatterns = [
    path('ThemViPhamQNCN/',views.ThemViPhamQNCN,name="ThemViPhamQNCN"),
    # path('RaVaoSQDacBiet/',views.RaVaoSQDacBiet,name="RaVaoSQDacBiet"),
    path('TatCaViPhamQNCN/',views.TatCaViPhamQNCN,name="TatCaViPhamQNCN"),
    path('SuaViPhamQNCN/<int:id>',views.SuaViPhamQNCN,name="SuaViPhamQNCN"),
    path('XoaViPhamQNCN/<int:id>',views.XoaViPhamQNCN,name="XoaViPhamQNCN"),
    path('ChiTietViPhamQNCN/<int:id>',views.ChiTietViPhamQNCN,name="ChiTietViPhamQNCN"),
    path('ViPhamQNCN/<int:id>',views.ViPhamQNCN,name="ViPhamQNCN"),
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