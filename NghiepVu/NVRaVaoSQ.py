from NVQuyen import ThoiGianTrongNgay_NhomSQ
# from NVSiQuan import LaySQTuMa
from model import LSRaVaoSQModel,CongGacModel,TheSiQuanModel
from django.utils import timezone
from datetime import timedelta
from be.settings import SoDoiTuongMoiTrang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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



def lay_lich_su_ra_vao(page=1):
    # Lấy tất cả bản ghi từ LSRaVaoSQModel
    ls_ra_vao_list = LSRaVaoSQModel.LSRaVaoSQModel.objects.select_related('SiQuan', 'SoThe', 'Cong').values(
        'SiQuan__HoTen', 
        'SiQuan__DonVi__TenDonVi', 
        'Cong__TenCong', 
        'ThoiGian', 
        'TrangThai'
    )

    if not ls_ra_vao_list.exists():
        # Nếu không có bản ghi nào, trả về thông báo và danh sách trống
        return {
            "status": "success",
            "data": [],
            "pagination": {
                "current_page": page,
                "total_pages": 0,
                "total_items": 0,
                "has_next": False,
                "has_previous": False,
            }
        }
    
    # Tạo Paginator object
    paginator = Paginator(ls_ra_vao_list, SoDoiTuongMoiTrang)
    
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    # Định dạng kết quả để chuyển đổi thành JSON
    ket_qua = list(results)
    for item in ket_qua:
        item['TrangThai'] = 'Ra' if item['TrangThai'] else 'Vao'

    # Trả về kết quả dạng JSON
    return {
        "status": "success",
        "data": ket_qua,
        "pagination": {
            "current_page": results.number,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
            "has_next": results.has_next(),
            "has_previous": results.has_previous(),
        }
    }

                     
    
    
