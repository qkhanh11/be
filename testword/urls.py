from django.urls import path
from . import views

app_name = "testword"

urlpatterns = [
    path('export/',views.generate_word_file,name="generate_word_file"),
    # path('sua/<int:id>',views.SuaSiQuan,name="SuaSiQuan"),
    # path('xoa/<int:id>',views.XoaSiQuan,name="SuaSiQuan"),
    # path('timsq/',views.TimSiQuan,name="TimSiQuan"),
    # path('xemlsdv/<int:id>',views.LSDV,name="LichSuDonViSQ"),
    # path('xemlscv/<int:id>',views.LSCV,name="LichSuChucVuSQ"),
    # path('thongtinchitiet/<int:id>',views.ThongTinChiTiet,name="ThongTinChiTietSQ"),
    # path('LayTenSQTuMa/',views.LayTenSQTuMa,name="LayTenSQTuMa"),
    # path('DSTiepKhachSQ/<int:id>',views.DSTiepKhachSQ,name="DSTiepKhachSQ"),
]