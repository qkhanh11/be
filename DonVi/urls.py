from django.urls import path
from . import views

app_name = "DonVi"

urlpatterns = [
    path('them/',views.Them,name="ThemDonVi"),
    path('thongtin/<int:id>',views.ThongTin,name="ThongTinDonVi"),
    path('sua/<int:id>',views.Sua,name="SuaDonVi"),
    path('xoa/<int:id>',views.XoaDonVi,name="XoaDonVi"),
    path('timkiem/',views.TimKiemDonVi,name="TimKiemDonVi"),
    path('DropDownDV/',views.DropDownDV,name="DropDownDV"),
    path('DonViCon/',views.DonViCon,name="DonViCon"),
    path('DonViChaTheoNhom/',views.DonViChaTheoNhom,name="DonViChaTheoNhom"),
    path('TimDonVi/',views.TimDonVi,name="TimDonVi"),
    path('DropdownDonViCha/<int:id>',views.DropdownDonViCha,name="DropdownDonViCha"),
]