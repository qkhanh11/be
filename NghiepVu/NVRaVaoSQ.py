from .NVQuyen import ThoiGianTrongNgay_NhomSQ
# from NVSiQuan import LaySQTuMa
from model import LSRaVaoSQModel,CongGacModel,TheSiQuanModel
from django.utils import timezone
from datetime import timedelta
from be.settings import SoDoiTuongMoiTrang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta



def RaVaoSQ(sothe,trangthai,cong, ngay, gio):
    try:
        tg_ra_va_tg_vao = ThoiGianTrongNgay_NhomSQ(ngay,sothe)
        try:
            if tg_ra_va_tg_vao['status'] == 'error':
                return tg_ra_va_tg_vao  # Trả về thông báo lỗi nếu không tìm thấy nhóm sĩ quan
        except: 
            pass
        ngay_gio_str = ngay + " " + gio
        thoigian_gio = datetime.strptime(ngay_gio_str, "%Y-%m-%d %H:%M")
        the = TheSiQuanModel.TheSiQuanModel.objects.get(SoThe=sothe, TrangThai= True)
        SQ = the.SiQuan
        Cong = CongGacModel.CongGacModel.objects.get(pk=cong)
        for tg_ra,tg_vao in tg_ra_va_tg_vao:
                tg_vao_datetime = datetime.combine(datetime.strptime(ngay, "%Y-%m-%d"), tg_vao)
                tg_ra_datetime = datetime.combine(datetime.strptime(ngay, "%Y-%m-%d"), tg_ra)
            
                if thoigian_gio > tg_vao_datetime and thoigian_gio < tg_ra_datetime:
                    if trangthai == 0:
                        
                        return {"status": "success1", "message": "Vào muộn"}
                    else:
                        
                        return {"status": "success1", "message": "Ra trước thời gian quy định"}


        ls_ravao = LSRaVaoSQModel.LSRaVaoSQModel.objects.create(
            SiQuan = SQ,
            SoThe = the,
            ThoiGian = thoigian_gio,
            TrangThai = trangthai,
            Cong = Cong
        )
        return {"status": "success", "message": "Đã lưu"}
    except TheSiQuanModel.TheSiQuanModel.DoesNotExist:
        return {"status": "error", "message": 'Không tồn tại thẻ này'}


def RaVaoSQDacBiet( sothe, trangthai,cong, ngay, gio):
    try:
        ngay_gio_str = ngay + " " + gio
        ngay_gio = datetime.strptime(ngay_gio_str, "%Y-%m-%d %H:%M")
        the = TheSiQuanModel.TheSiQuanModel.objects.get(SoThe=sothe, TrangThai= True)
        SQ = the.SiQuan
        Cong = CongGacModel.CongGacModel.objects.get(pk=cong)
        banghi = LSRaVaoSQModel.LSRaVaoSQModel.objects.create(
            SiQuan = SQ,
            SoThe = the,
            Cong = Cong,
            ThoiGian=ngay_gio,
            TrangThai = trangthai
        )
        

# Chuyển đổi thành đối tượng datetime
        
        
        

        return {"status": "success", "data": "Thêm thành công"}
    except TheSiQuanModel.TheSiQuanModel.DoesNotExist:
        return {"status": "error", "message": 'Không tồn tại thẻ này'}
    except Exception as e:
        return {"status": "error", "message": str(e)}



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
    
    for record in ls_ra_vao_list:
        thoigian = record['ThoiGian']
        if thoigian:
            # Định dạng thành %H:%M %d-%m-%Y
            record['ThoiGian'] = thoigian.strftime("%H:%M %d-%m-%Y")
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



def SuaRaVaoSQ(id, sothe, trangthai,cong, ngay, gio):
    try:
        banghi = LSRaVaoSQModel.LSRaVaoSQModel.objects.get(pk = id)
        ngay_gio_str = ngay + " " + gio

# Chuyển đổi thành đối tượng datetime
        ngay_gio = datetime.strptime(ngay_gio_str, "%Y-%m-%d %H:%M")
        banghi.TrangThai = trangthai
        the = TheSiQuanModel.TheSiQuanModel.objects.get(SoThe=sothe, TrangThai= True)
        SQ = the.SiQuan
        Cong = CongGacModel.CongGacModel.objects.get(pk=cong)
        banghi.SiQuan = SQ
        banghi.SoThe = the
        banghi.Cong = Cong
        banghi.ThoiGian=ngay_gio
        banghi.save()
        return {"status": "success", "data": "Sửa thành công"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def XoaRaVaoSQ(id):
    try:
        banghi = LSRaVaoSQModel.LSRaVaoSQModel.objects.get(pk = id)
        banghi.delete()
        return {"status": "success", "data": "Xóa thành công"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ChiTiet(id):
    try:
        banghi = LSRaVaoSQModel.LSRaVaoSQModel.objects.get(pk = id)
        sothe = banghi.SoThe.SoThe
        SiQuan = banghi.SiQuan.HoTen
        tencong = banghi.Cong.TenCong
        cong = banghi.Cong.id
        thoigian = banghi.ThoiGian
        ngay = thoigian.strftime("%Y-%m-%d")
        gio = thoigian.strftime("%H:%M")
        TrangThai = banghi.TrangThai
        response_data = {
        "sothe": sothe,
        "si_quan": SiQuan,
        "tencong": tencong,
        "cong": cong,
        "ngay": ngay,
        "gio": gio,
        "trangthai": TrangThai,
        "TenTrangThai": "Vào" if TrangThai == 0 else "Ra"
    }

        return {"status": "success", "data": response_data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThemBanGhi( sothe, trangthai,cong, ngay, gio):
    try:
        ngay_gio_str = ngay + " " + gio
        ngay_gio = datetime.strptime(ngay_gio_str, "%Y-%m-%d %H:%M")
        the = TheSiQuanModel.TheSiQuanModel.objects.get(SoThe=sothe, TrangThai= True)
        SQ = the.SiQuan
        Cong = CongGacModel.CongGacModel.objects.get(pk=cong)
        banghi = LSRaVaoSQModel.LSRaVaoSQModel.objects.create(
            SiQuan = SQ,
            SoThe = the,
            Cong = Cong,
            ThoiGian=ngay_gio,
            TrangThai = trangthai
        )
        

# Chuyển đổi thành đối tượng datetime
        
        
        

        return {"status": "success", "data": "Thêm thành công"}
    except Exception as e:
        return {"status": "error", "message": str(e)}