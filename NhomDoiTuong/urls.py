from django.urls import path
from . import views

app_name = "NhomDoiTuong"

urlpatterns = [
    path('themnhomsq/',views.ThemNhomSQ,name="ThemNhomSQ"),
    path('themnhomqncn/',views.ThemNhomQNCN,name="ThemNhomSQ"),
    path('themnhomvc/',views.ThemNhomVC,name="ThemNhomVC"),
    path('suasq/<int:id>',views.SuaNhomSQ,name="SuaNhomSQ"),
    path('suaqncn/<int:id>',views.SuaNhomQNCN,name="SuaNhomQNCN"),
    path('suavc/<int:id>',views.SuaNhomVC,name="SuaNhomVC"),
    path('xoasq/<int:id>',views.XoaNhomSQ,name="XoaNhomSQ"),
    path('xoaqncn/<int:id>',views.XoaNhomQNCN,name="XoaNhomQNCN"),
    path('xoavc/<int:id>',views.XoaNhomVC,name="XoaNhomQNCN"),
    path('sq/',views.NhomSQ,name="NhomSQ"),
    path('qncn/',views.NhomQNCN,name="NhomQNCN"),
    path('vc/',views.NhomVC,name="NhomVC"),
]