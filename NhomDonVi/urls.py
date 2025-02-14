from django.urls import path
from . import views

app_name = "NhomDonVi"

urlpatterns = [
    path('them/',views.ThemNhomDonVi,name="ThemNhomDonVi"),
    path('sua/<int:id>',views.SuaNhomDonVi,name="SuaNhomDonVi"),
    path('xoa/<int:id>',views.XoaNhomDonVi,name="XoaNhomDonVi"),
    # path('tim/',views.NhomDonVi,name="TimNhomDonVi"),
    path('',views.NhomDonVi,name="TatCaNhomDonVi"),
    path('thongtin/<int:id>',views.ThongTinNhomDonVi,name="ThongTinNhomDonVi"),
    # path('lsravao/<int:id>',views.XemLichSuRaVao,name="XemLichSuRaVao"),
]