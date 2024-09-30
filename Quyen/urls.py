from django.urls import path
from . import views

app_name = "Quyen"

urlpatterns = [
    path('ThemQuyen/',views.ThemQuyen,name="ThemQuyen"),
    path('SuaQuyen/<int:id>',views.SuaQuyen,name="SuaQuyen"),
    path('XoaQuyen/<int:id>',views.XoaQuyen,name="XoaQuyen"),
    path('TatCaQuyen/',views.TatCaQuyen,name="TatCaQuyen"),
    path('ThemThoiGianQuyen/',views.ThemThoiGianQuyen,name="ThemThoiGianQuyen"),
    path('XemChiTietQuyen/<int:id>',views.XemChiTietQuyen,name="XemChiTietQuyen"),
    path('SuaThoiGianQuyen/<int:id>',views.SuaThoiGianQuyen,name="SuaThoiGianQuyen"),
    path('ChiTietThoiGianQuyen/<int:id>',views.ChiTietThoiGianQuyen,name="ChiTietThoiGianQuyen"),
    # path('TimTrucBanTheoKhoangNgay/',views.TimTrucBanTheoKhoangNgay,name="TimTrucBanTheoKhoangNgay"),
    # path('LayThongTinTrucBanTheoID/<int:id>',views.LayThongTinTrucBanTheoID,name="LayThongTinTrucBanTheoID"),
    # path('LayTatCaCaGac/',views.LayTatCaCaGac,name="LayTatCaCaGac"),
    # path('SuaCong/<int:id>',views.SuaCong,name="SuaCong"),
    # path('XoaCong/<int:id>',views.XoaCong,name="XoaCong"),
    # path('ThemCong/',views.ThemCong,name="ThemCong"),
    # path('ThemCaGac/',views.ThemCaGac,name="ThemCaGac"),
    # path('SuaCaGac/<int:id>',views.SuaCaGac,name="SuaCaGac"),
    # path('XoaCaGac/<int:id>',views.XoaCaGac,name="XoaCaGac"),
    # path('ThemPCCaGac/',views.ThemPCCaGac,name="ThemPCCaGac"),
    # path('lay_ngay_theo_cong/<int:id>',views.lay_ngay_theo_cong,name="lay_ngay_theo_cong"),
    # path('LayCaGacTrongNgayCong/<int:id>',views.LayCaGacTrongNgayCong,name="LayCaGacTrongNgayCong"),
    # path('ThemPhanCongChiTiet/',views.ThemPhanCongChiTiet,name="ThemPhanCongChiTiet"),
    # path('xem_phan_cong_chi_tiet/<int:id>',views.xem_phan_cong_chi_tiet,name="xem_phan_cong_chi_tiet"),
    # path('xoa_phan_cong_chi_tiet/<int:id>',views.xoa_phan_cong_chi_tiet,name="xoa_phan_cong_chi_tiet"),
    
]