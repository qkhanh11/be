from model import HocVienModel, ViPhamHVModel, CongGacModel, LoiViPhamModel
from datetime import datetime, timedelta



def ThemViPhamHV(mahv, LoiViPham, ngay, gio, cong, ghichu):
    SQ = None
    try:
        SQ = HocVienModel.HocVienModel.objects.get(MaQuanNhan = mahv,TrangThai=True)
    except:
        return {"status": "error", "message": "Không tồn tại mã học viên này"}
    try:
        Cong = CongGacModel.CongGacModel.objects.get(pk = cong)
        Loi = LoiViPhamModel.LoiViPhamModel.objects.get(pk = LoiViPham)
        ngay_gio_str = ngay + " " + gio
        thoigian_gio = datetime.strptime(ngay_gio_str, "%Y-%m-%d %H:%M")
        ViPhamHVModel.ViPhamHVModel.objects.create(
            LoiViPham=Loi,
            HocVien=SQ,
            ThoiGian=thoigian_gio,
            Cong=Cong,
            GhiChu=ghichu
            )
        return {"status": "success", "data": "Thêm vi phạm thành công"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def SuaViPhamHV(id, mahv, LoiViPham, ngay, gio, cong, ghichu):
    SQ = None
    try:
        SQ = HocVienModel.HocVienModel.objects.get(MaQuanNhan = mahv,TrangThai=True)
    except:
        return {"status": "error", "message": "Không tồn tại mã học viên này"}
    try:
        Cong = CongGacModel.CongGacModel.objects.get(pk = cong)
        Loi = LoiViPhamModel.LoiViPhamModel.objects.get(pk = LoiViPham)
        ngay_gio_str = ngay + " " + gio
        thoigian_gio = datetime.strptime(ngay_gio_str, "%Y-%m-%d %H:%M")
        banghi = ViPhamHVModel.ViPhamHVModel.objects.get(pk=id)
        banghi.LoiViPham=Loi
        banghi.HocVien=SQ
        banghi.ThoiGian=thoigian_gio
        banghi.Cong=Cong
        banghi.GhiChu=ghichu
        banghi.save()
        return {"status": "success", "data": "Sửa vi phạm thành công"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaViPhamHV(id):

    try:
        
        banghi = ViPhamHVModel.ViPhamHVModel.objects.get(pk=id)
        banghi.delete()
        return {"status": "success", "data": "Xóa vi phạm thành công"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ChiTietViPhamHV(id):
    try:
        banghi = ViPhamHVModel.ViPhamHVModel.objects.get(pk=id)
        SiQuan = banghi.HocVien.MaQuanNhan
        TenSQ = banghi.HocVien.HoTen
        ngay = banghi.ThoiGian.strftime("%Y-%m-%d")
        gio = banghi.ThoiGian.strftime("%H:%M")
        Cong = banghi.Cong.id
        TenCong = banghi.Cong.TenCong
        LoiViPham = banghi.LoiViPham.id
        TenLoi = banghi.LoiViPham.TenLoi
        GhiChu = banghi.GhiChu
        response_data = {
        "HV": SiQuan,
        "TenHV": TenSQ,
        "ngay": ngay,
        "gio": gio,
        "Cong": Cong,
        "TenCong": TenCong,
        "LoiViPham": LoiViPham,
        "TenLoi": TenLoi,
        "GhiChu": GhiChu
    }
        return {"status": "success", "data": response_data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TatCaViPhamHV(NgayBD=None, NgayKT=None):
    try:
        if NgayBD:
            NgayBD = datetime.strptime(NgayBD, '%Y-%m-%d').date()
        if NgayKT:
            NgayKT = datetime.strptime(NgayKT, '%Y-%m-%d').date()
        # Truy vấn cơ bản theo id của sĩ quan
        print(NgayBD,NgayKT)
        ls_vipham = ViPhamHVModel.ViPhamHVModel.objects.all()

        if NgayBD:
            NgayBD_start = datetime.combine(NgayBD, datetime.min.time())  # Bắt đầu từ 00:00:00 của ngày đó
            ls_vipham = ls_vipham.filter(ThoiGian__gte=NgayBD_start)
        
        # Nếu NgayKT không None, lọc các khách có ThoiGianKetThuc đến hết ngày NgayKT
        if NgayKT:
            NgayKT_end = datetime.combine(NgayKT, datetime.max.time())  # Kết thúc ở 23:59:59 của ngày đó
            ls_vipham = ls_vipham.filter(ThoiGian__lte=NgayKT_end)
        result = []
        ls_vipham = ls_vipham.order_by("-ThoiGian")
        for vipham in ls_vipham:
            result.append({
                # 'SoThe': ravao.SoThe.SoThe,  # Tên khách
                # 'ngay': ravao.ThoiGian.date().strftime('%d/%m/%Y'),  # Ngày tháng năm bắt đầu
                # 'thoigian': ravao.ThoiGian.time().strftime('%H:%M'),  # Giờ phút bắt đầu
                # 'cong': ravao.Cong.TenCong,
                # 'trangthai': "Ra" if ravao.TrangThai else "Vào"
                # "SiQuan": vipham.SiQuan.MaQuanNhan,
                "id": vipham.id,
                "TenHV": vipham.HocVien.HoTen,
                "DonVi" :vipham.HocVien.DonVi.TenDonVi,
                "thoigian": vipham.ThoiGian.strftime("%H:%M %Y-%m-%d"),
                # "gio": vipham.ThoiGian.strftime("%H:%M"),
                # "Cong": vipham.Cong.id,
                "TenCong": vipham.Cong.TenCong,
                # "LoiViPham": vipham.LoiViPham.id,
                "TenLoi": vipham.LoiViPham.TenLoi,
                "GhiChu": vipham.GhiChu
            })
        
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def ViPhamHV(id,NgayBD=None, NgayKT=None):
    try:
        if NgayBD:
            NgayBD = datetime.strptime(NgayBD, '%Y-%m-%d').date()
        if NgayKT:
            NgayKT = datetime.strptime(NgayKT, '%Y-%m-%d').date()
        QNCN = HocVienModel.HocVienModel.objects.get(pk=id)

        ls_vipham = ViPhamHVModel.ViPhamHVModel.objects.filter(HocVien__id=id)

        if NgayBD:
            NgayBD_start = datetime.combine(NgayBD, datetime.min.time())  # Bắt đầu từ 00:00:00 của ngày đó
            ls_vipham = ls_vipham.filter(ThoiGian__gte=NgayBD_start)
        
        # Nếu NgayKT không None, lọc các khách có ThoiGianKetThuc đến hết ngày NgayKT
        if NgayKT:
            NgayKT_end = datetime.combine(NgayKT, datetime.max.time())  # Kết thúc ở 23:59:59 của ngày đó
            ls_vipham = ls_vipham.filter(ThoiGian__lte=NgayKT_end)
        ls_vipham = ls_vipham.order_by("-ThoiGian")
        result = []
        for vipham in ls_vipham:
            result.append({
                # 'SoThe': ravao.SoThe.SoThe,  # Tên khách
                # 'ngay': ravao.ThoiGian.date().strftime('%d/%m/%Y'),  # Ngày tháng năm bắt đầu
                # 'thoigian': ravao.ThoiGian.time().strftime('%H:%M'),  # Giờ phút bắt đầu
                # 'cong': ravao.Cong.TenCong,
                # 'trangthai': "Ra" if ravao.TrangThai else "Vào"
                # "SiQuan": vipham.SiQuan.MaQuanNhan,
                # "id": vipham.id,
                # "TenSQ": vipham.QNCN.HoTen,
                # "DonVi" :vipham.QNCN.DonVi.TenDonVi,
                "thoigian": vipham.ThoiGian.strftime("%H:%M %Y-%m-%d"),
                # "gio": vipham.ThoiGian.strftime("%H:%M"),
                # "Cong": vipham.Cong.id,
                "TenCong": vipham.Cong.TenCong,
                # "LoiViPham": vipham.LoiViPham.id,
                "TenLoi": vipham.LoiViPham.TenLoi,
                "GhiChu": vipham.GhiChu
            })
        
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}