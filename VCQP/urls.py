from django.urls import path
from . import views

app_name = "VC"

urlpatterns = [
    path('them/',views.ThemVC,name="ThemVC"),
    path('sua/<int:id>',views.SuaVC,name="SuaVC"),
    path('xoa/<int:id>',views.XoaVC,name="XoaVC"),
    path('timVC/',views.TimVC,name="TimVC"),
    path('xemlsdv/<int:id>',views.LSDV,name="LichSuDonViVC"),
    path('thongtinchitiet/<int:id>',views.ThongTinChiTiet,name="ThongTinChiTietVC"),
    path('LayTenVCTuMa/',views.LayVCTuMa,name="LayTenSQTuMa"),
    path('DSTiepKhachVC/<int:id>',views.DSTiepKhachVC,name="DSTiepKhachSQ"),
]