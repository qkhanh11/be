from django.urls import path
from . import views

app_name = "Truc"

urlpatterns = [
    path('ThemTrucBan/',views.ThemTrucBan,name="ThemTrucBan"),
    path('SuaTrucBan/<int:id>',views.SuaTrucBan,name="SuaTrucBan"),
    path('XoaTrucBan/<int:id>',views.XoaTrucBan,name="XoaTrucBan"),
    path('XemTatCaTrucBan/',views.XemTatCaTrucBan,name="XemTatCaTrucBan"),
    path('XemChiTietTrucBan/<int:id>',views.XemChiTietTrucBan,name="XemChiTietTrucBan"),
    path('LayDanhSachCong/',views.LayDanhSachCong,name="LayDanhSachCong"),
    path('TimTrucBanTheoKhoangNgay/',views.TimTrucBanTheoKhoangNgay,name="TimTrucBanTheoKhoangNgay"),
    path('LayThongTinTrucBanTheoID/<int:id>',views.LayThongTinTrucBanTheoID,name="LayThongTinTrucBanTheoID"),
    path('LayTatCaCaGac/',views.LayTatCaCaGac,name="LayTatCaCaGac"),
    path('SuaCong/<int:id>',views.SuaCong,name="SuaCong"),
    path('XoaCong/<int:id>',views.XoaCong,name="XoaCong"),
    path('ThemCong/',views.ThemCong,name="ThemCong"),
    path('ThemCaGac/',views.ThemCaGac,name="ThemCaGac"),
    path('SuaCaGac/<int:id>',views.SuaCaGac,name="SuaCaGac"),
    path('XoaCaGac/<int:id>',views.XoaCaGac,name="XoaCaGac"),
    path('ThemPCCaGac/',views.ThemPCCaGac,name="ThemPCCaGac"),
    path('lay_ngay_theo_cong/<int:id>',views.lay_ngay_theo_cong,name="lay_ngay_theo_cong"),
    path('LayCaGacTrongNgayCong/<int:id>',views.LayCaGacTrongNgayCong,name="LayCaGacTrongNgayCong"),
    path('ThemPhanCongChiTiet/',views.ThemPhanCongChiTiet,name="ThemPhanCongChiTiet"),
    path('xem_phan_cong_chi_tiet/<int:id>',views.xem_phan_cong_chi_tiet,name="xem_phan_cong_chi_tiet"),
    path('xoa_phan_cong_chi_tiet/<int:id>',views.xoa_phan_cong_chi_tiet,name="xoa_phan_cong_chi_tiet"),
    
]