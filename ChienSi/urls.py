from django.urls import path
from . import views

app_name = "ChienSi"

urlpatterns = [
    path('ThemChienSi/',views.ThemChienSi,name="ThemChienSi"),
    path('SuaChienSi/<int:id>',views.SuaChienSi,name="SuaChienSi"),
    path('XoaChienSi/<int:id>',views.XoaChienSi,name="XoaChienSi"),
    path('ChiTietChienSi/<int:id>',views.ChiTietChienSi,name="ChiTietChienSi"),
    path('TatCaChienSi/',views.TatCaChienSi,name="TatCaChienSi"),
    path('LayTenCSTuMa/',views.LayTenCSTuMa,name="LayTenCSTuMa"),
    # path('DonViCon/',views.DonViCon,name="DonViCon"),
    # path('DonViChaTheoNhom/',views.DonViChaTheoNhom,name="DonViChaTheoNhom"),
    # path('TimDonVi/',views.TimDonVi,name="TimDonVi"),
]