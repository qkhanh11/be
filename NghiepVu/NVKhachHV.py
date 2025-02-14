from model import  KhachModel, KhachHocVienModel, HocVienModel
from datetime import datetime, timedelta
from django.utils import timezone






def ThemKhach(HoTenKhach,SoDinhDanh):
    try:

        khach,created = KhachModel.KhachModel.objects.get_or_create(
            HoTenKhach=HoTenKhach,
            SoDinhDanh=SoDinhDanh
        )
        return khach
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}

def TiepKhachHV(HV,HoTenKhach,SoDinhDanh,NgayBD, GioBD,NgayKT,GioKT,GhiChu):
    try:
        khach = ThemKhach(HoTenKhach, SoDinhDanh)
        HV = HocVienModel.HocVienModel.objects.get(MaQuanNhan=HV)
        if not HV:
            return {"status": "error", "message": "Không tồn tại mã quân nhân"}
        TGBD = datetime.strptime(f"{NgayBD} {GioBD}", '%Y-%m-%d %H:%M')
        TGKT = datetime.strptime(f"{NgayKT} {GioKT}", '%Y-%m-%d %H:%M') if NgayKT and GioKT else None

        # Cộng thêm 7 giờ
        tiepkhach = KhachHocVienModel.KhachHocVienModel.objects.create(
            HV=HV,
            Khach=khach,
            ThoiGianBatDau=TGBD,
            ThoiGianKetThuc=TGKT,
            GhiChu=GhiChu
        )
        return {"status": "success", "data": 'Thêm thành công'}
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
    

def TraKhach(id):
    try:
        banghi = KhachHocVienModel.KhachHocVienModel.objects.get(pk=id)
        thoigian = timezone.now() + timedelta(hours=7)
        # Cộng thêm 7 giờ
        banghi.ThoiGianKetThuc=thoigian
        banghi.save()
        return {"status": "success", "data": 'Trả khách thành công'}
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
    

def SuaTiepKhachHV(id,HV,HoTenKhach,SoDinhDanh,NgayBD, GioBD,NgayKT,GioKT,GhiChu):
    try:
        khach = ThemKhach(HoTenKhach, SoDinhDanh)
        HV = HocVienModel.HocVienModel.objects.get(MaQuanNhan=HV)
        if not HV:
            return {"status": "error", "message": "Không tồn tại mã quân nhân"}
        TGBD = datetime.strptime(f"{NgayBD} {GioBD}", '%Y-%m-%d %H:%M')
        TGKT = datetime.strptime(f"{NgayKT} {GioKT}", '%Y-%m-%d %H:%M') if NgayKT and GioKT else None

        # Cộng thêm 7 giờ
        tiepkhach = KhachHocVienModel.KhachHocVienModel.objects.get(pk=id)
        tiepkhach.HV=HV
        tiepkhach.Khach=khach
        tiepkhach.ThoiGianBatDau=TGBD
        tiepkhach.ThoiGianKetThuc=TGKT
        tiepkhach.GhiChu=GhiChu
        tiepkhach.save()
        return {"status": "success", "data": 'Sửa thành công'}
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
    

def XoaTiepKhachHV(id):
    try:

        # Cộng thêm 7 giờ
        tiepkhach = KhachHocVienModel.KhachHocVienModel.objects.get(pk=id)
        tiepkhach.delete()
        return {"status": "success", "data": 'Xóa thành công'}
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
    

def DangTiepKhach():
    try:
        tiepkhach = KhachHocVienModel.KhachHocVienModel.objects.filter(ThoiGianKetThuc__isnull=True)
        data = []
        for ksq in tiepkhach:
            data.append({
                'id': ksq.id,
                'HocVien__HoTen': ksq.HV.HoTen,
                'HocVien__MaHV': ksq.HV.MaQuanNhan,
                'Khach__HoTenKhach': ksq.Khach.HoTenKhach,
                'Khach__CanCuoc': ksq.Khach.SoDinhDanh,
                'ThoiGianBatDau': ksq.ThoiGianBatDau.strftime('%H:%M %d-%m-%Y'),  # Định dạng ngày giờ
                'GhiChu': ksq.GhiChu,
            })

    # Trả về JsonResponse
        return {"status": "success", "data": data}
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
    

def DanhSachTiepKhach():
    try:
        tiepkhach = KhachHocVienModel.KhachHocVienModel.objects.all()
        data = []
        for ksq in tiepkhach:
            data.append({
                'id': ksq.id,
                'HocVien__HoTen': ksq.HV.HoTen,
                'HocVien__MaHV': ksq.HV.MaQuanNhan,
                'Khach__HoTenKhach': ksq.Khach.HoTenKhach,
                'Khach__CanCuoc': ksq.Khach.SoDinhDanh,
                'ThoiGianBatDau': ksq.ThoiGianBatDau.strftime('%H:%M %d-%m-%Y'),  # Định dạng ngày giờ
                'GhiChu': ksq.GhiChu,
            })

    # Trả về JsonResponse
        return {"status": "success", "data": data}
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}