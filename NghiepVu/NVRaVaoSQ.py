from NVQuyen import ThoiGianTrongNgay_NhomSQ
from NVSiQuan import LaySQTuMa
from model import LSRaVaoSQModel,CongGacModel,TheSiQuanModel
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator



def RaVaoSQ(sothe,trangthai,cong):
    tg_ra_va_tg_vao = ThoiGianTrongNgay_NhomSQ(sothe)
    if tg_ra_va_tg_vao['status'] == 'error':
            return tg_ra_va_tg_vao
    thoigian = timezone.now() + timedelta(hours=7)
    thoigian_gio = thoigian.time()
    for tg_ra, tg_vao in tg_ra_va_tg_vao:
           if thoigian_gio > tg_vao and thoigian_gio < tg_ra:
                if trangthai == 0:
                    return {"status": "error", "message": "Vào muộn"}
                else:
                    return {"status": "error", "message": "Ra trước thời gian quy định"}
    the = TheSiQuanModel.TheSiQuanModel.objects.get(SoThe=sothe, TrangThai= True)
    SQ = the.SiQuan
    Cong = CongGacModel.CongGacModel.objects.get(pk=cong)
    ls_ravao = LSRaVaoSQModel.LSRaVaoSQModel.objects.create(
        SiQuan = SQ,
        SoThe = the,
        ThoiGian = thoigian,
        TrangThai = trangthai,
        Cong = Cong
    )
    return {"status": "success", "message": "Đã lưu"}


def RaVaoSQDacBiet(sothe,trangthai,cong):
    thoigian = timezone.now() + timedelta(hours=7)
    thoigian_gio = thoigian.time()
    the = TheSiQuanModel.TheSiQuanModel.objects.get(SoThe=sothe, TrangThai= True)
    SQ = the.SiQuan
    Cong = CongGacModel.CongGacModel.objects.get(pk=cong)
    ls_ravao = LSRaVaoSQModel.LSRaVaoSQModel.objects.create(
        SiQuan = SQ,
        SoThe = the,
        ThoiGian = thoigian,
        TrangThai = trangthai,
        Cong = Cong
    )
    return {"status": "success", "message": "Đã lưu"}



def lay_tat_ca_lich_su_ra_vao(page=1, so_mau_tin_mot_trang=10):
    # Lấy tất cả bản ghi từ LSRaVaoSQModel
    ls_ra_vao = LSRaVaoSQModel.objects.select_related('SiQuan', 'SoThe', 'Cong')

    # Tạo một đối tượng Paginator với số lượng mẫu tin mỗi trang
    paginator = Paginator(ls_ra_vao, so_mau_tin_mot_trang)

    try:
        # Lấy trang hiện tại
        trang_hien_tai = paginator.page(page)
    except EmptyPage:
        # Trả về trang cuối nếu trang yêu cầu không tồn tại
        trang_hien_tai = paginator.page(paginator.num_pages)
    
    # Dùng list comprehension để định dạng kết quả theo yêu cầu
    ket_qua = [{
        'HoTen': record.SiQuan.HoTen,
        'TenDonVi': record.SiQuan.DonVi.TenDonVi,
        'TenCong': record.Cong.TenCong,
        'ThoiGian': record.ThoiGian,
        'TrangThai': 'Ra' if record.TrangThai else 'Vao'
    } for record in trang_hien_tai]

    return{"status": "success", "data": ket_qua}

                     
    
    
