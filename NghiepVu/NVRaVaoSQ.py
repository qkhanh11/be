from .NVQuyen import ThoiGianTrongNgay_NhomSQ
# from NVSiQuan import LaySQTuMa
from model import LSRaVaoSQModel,CongGacModel,TheSiQuanModel
from django.utils import timezone
from datetime import timedelta
from be.settings import SoDoiTuongMoiTrang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def RaVaoSQ(sothe,trangthai,cong):
    tg_ra_va_tg_vao = ThoiGianTrongNgay_NhomSQ(sothe)
    try:
        if tg_ra_va_tg_vao['status'] == 'error':
            return tg_ra_va_tg_vao  # Trả về thông báo lỗi nếu không tìm thấy nhóm sĩ quan
    except: 
        pass
    thoigian = timezone.now() + timedelta(hours=7)
    thoigian_gio = thoigian.time()
    for tg_vao, tg_ra in tg_ra_va_tg_vao:
           print(tg_ra,tg_vao)
           if thoigian_gio > tg_vao and thoigian_gio < tg_ra:
                
                if trangthai == 0:
                    ls_ravao = LSRaVaoSQModel.LSRaVaoSQModel.objects.create(
                    SiQuan = SQ,
                    SoThe = the,
                    ThoiGian = thoigian,
                    TrangThai = trangthai,
                    Cong = Cong
    )
                    return {"status": "error", "message": "Vào muộn"}
                else:
                    ls_ravao = LSRaVaoSQModel.LSRaVaoSQModel.objects.create(
                    SiQuan = SQ,
                    SoThe = the,
                    ThoiGian = thoigian,
                    TrangThai = trangthai,
                    Cong = Cong
                )
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



def lay_lich_su_ra_vao():
    # Lấy tất cả bản ghi từ LSRaVaoSQModel
    ls_ra_vao_list = LSRaVaoSQModel.LSRaVaoSQModel.objects.select_related('SiQuan', 'SoThe', 'Cong').values(
        'SiQuan__HoTen', 
        'SiQuan__DonVi__TenDonVi',
        'SiQuan__NhomSQ__TenNhom',
        'Cong__TenCong', 
        'ThoiGian', 
        'TrangThai'
    )

    if not ls_ra_vao_list.exists():
        # Nếu không có bản ghi nào, trả về thông báo và danh sách trống
        return {
            "status": "success",
            "data": []
        }
    

    # Định dạng kết quả để chuyển đổi thành JSON
    ket_qua = list(ls_ra_vao_list)
    for item in ket_qua:
        item['TrangThai'] = 'Ra' if item['TrangThai'] else 'Vào'

    # Trả về kết quả dạng JSON
    return {
        "status": "success",
        "data": ket_qua
    }

                     
    
    
