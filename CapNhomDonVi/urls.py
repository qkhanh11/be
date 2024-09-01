from django.urls import path
from . import views

app_name = "CapNhomDonVi"

urlpatterns = [
    path('them/',views.Them,name="ThemCapNhomDonVi"),
    path('sua/<int:id>',views.Sua,name="SuaCapNhomDonVi"),
    path('xoa/<int:id>',views.Xoa,name="XoaCapNhomDonVi"),
    path('<int:id>',views.TimKiemTheoNhom,name="TimKiemTheoNhom"),
    path('thongtin/<int:id>',views.ThongTin,name="ThongTinCapNhomDonVi"),
]