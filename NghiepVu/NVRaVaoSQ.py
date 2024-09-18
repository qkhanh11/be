from .NVQuyen import ThoiGianTrongNgay_NhomSQ
# from NVSiQuan import LaySQTuMa
from model import LSRaVaoSQModel,CongGacModel,TheSiQuanModel
from django.utils import timezone
from datetime import timedelta
from be.settings import SoDoiTuongMoiTrang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta



def RaVaoSQ(sothe,trangthai,cong):
    tg_ra_va_tg_vao = ThoiGianTrongNgay_NhomSQ(sothe)
    try:
        if tg_ra_va_tg_vao['status'] == 'error':
            return tg_ra_va_tg_vao  # Trả về thông báo lỗi nếu không tìm thấy nhóm sĩ quan
    except: 
        pass
    thoigian = timezone.now() + timedelta(hours=7)
    thoigian_gio = thoigian.time()
    the = TheSiQuanModel.TheSiQuanModel.objects.get(SoThe=sothe, TrangThai= True)
    SQ = the.SiQuan
    Cong = CongGacModel.CongGacModel.objects.get(pk=cong)
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
        'id',
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

                     
    
def LSRaVaoSQ(id, NgayBD=None, NgayKT=None):
    try:
        if NgayBD:
            NgayBD = datetime.strptime(NgayBD, '%Y-%m-%d').date()
        if NgayKT:
            NgayKT = datetime.strptime(NgayKT, '%Y-%m-%d').date()
        # Truy vấn cơ bản theo id của sĩ quan
        print(NgayBD,NgayKT)
        ls_ravao = LSRaVaoSQModel.LSRaVaoSQModel.objects.filter(SiQuan_id=id)

        if NgayBD:
            NgayBD_start = datetime.combine(NgayBD, datetime.min.time())  # Bắt đầu từ 00:00:00 của ngày đó
            ls_ravao = ls_ravao.filter(ThoiGian__gte=NgayBD_start)
        
        # Nếu NgayKT không None, lọc các khách có ThoiGianKetThuc đến hết ngày NgayKT
        if NgayKT:
            NgayKT_end = datetime.combine(NgayKT, datetime.max.time())  # Kết thúc ở 23:59:59 của ngày đó
            ls_ravao = ls_ravao.filter(ThoiGian__lte=NgayKT_end)
        result = []
        for ravao in ls_ravao:
            result.append({
                'SoThe': ravao.SoThe.SoThe,  # Tên khách
                'ngay': ravao.ThoiGian.date().strftime('%d/%m/%Y'),  # Ngày tháng năm bắt đầu
                'thoigian': ravao.ThoiGian.time().strftime('%H:%M'),  # Giờ phút bắt đầu
                'cong': ravao.Cong.TenCong,
                'trangthai': "Ra" if ravao.TrangThai else "Vào"
            })
        
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}


