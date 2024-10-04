from django.urls import path
from . import views

app_name = "ViPhamSQ"

urlpatterns = [
    path('ThemViPhamSQ/',views.ThemViPhamSQ,name="ThemViPhamSQ"),
    # path('RaVaoSQDacBiet/',views.RaVaoSQDacBiet,name="RaVaoSQDacBiet"),
    path('TatCaViPhamSQ/',views.TatCaViPhamSQ,name="TatCaViPhamSQ"),
    path('SuaViPhamSQ/<int:id>',views.SuaViPhamSQ,name="LSRaVaSuaViPhamSQoSQ"),
    path('XoaViPhamSQ/<int:id>',views.XoaViPhamSQ,name="XoaViPhamSQ"),
    path('ChiTietViPhamSQ/<int:id>',views.ChiTietViPhamSQ,name="ChiTietViPhamSQ"),
    path('ViPhamSQ/<int:id>',views.ViPhamSQ,name="ViPhamSQ"),
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