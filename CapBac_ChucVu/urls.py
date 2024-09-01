from django.urls import path
from . import views

app_name = "CapBac_ChucVu"

urlpatterns = [
    path('ThemCapBac/',views.ThemCapBac,name="ThemCapBac"),
    path('SuaCapBac/<int:id>',views.SuaCapBac,name="SuaCapBac"),
    path('XoaCapBac/<int:id>',views.XoaCapBac,name="XoaCapBac"),
    path('CapBac/',views.CapBac,name="CapBac"),
    path('ThemCapBacHSQ/',views.ThemCapBacHSQ,name="ThemCapBacHSQ"),
    path('SuaCapBacHSQ/<int:id>',views.SuaCapBacHSQ,name="SuaCapBacHSQ"),
    path('XoaCBHSQ/<int:id>',views.XoaCBHSQ,name="XoaCBHSQ"),
    path('CapBacHSQ/',views.CapBacHSQ,name="CapBacHSQ"),
    path('ThemCVSQ/',views.ThemCVSQ,name="ThemCVSQ"),
    path('SuaCVSQ/<int:id>',views.SuaCVSQ,name="SuaCVSQ"),
    path('XoaCVSQ/<int:id>',views.XoaCVSQ,name="XoaCVSQ"),
    path('CVSQ/',views.CVSQ,name="CVSQ"),
    path('ThemCVQNCN/',views.ThemCVQNCN,name="ThemCVQNCN"),
    path('SuaCVQNCN/<int:id>',views.SuaCVQNCN,name="SuaCVQNCN"),
    path('XoaCVQNCN/<int:id>',views.XoaCVQNCN,name="XoaCVQNCN"),
    path('CVQNCN/',views.CVQNCN,name="CVQNCN"),
    path('CVSQTrongDonVi/<int:id>',views.CVSQTrongDonVi,name="CVSQTrongDonVi"),
]