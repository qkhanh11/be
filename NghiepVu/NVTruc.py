from model import CongGacModel, PCTrucBanModel, CaGacVBModel, PCVeBinhModel, PCVeBinhChiTietModel,ChienSiModel
from .NVSiQuan import LaySQTuMa
from .NVChienSi import LayChienSiTuMa
from datetime import date


def ThemCong(TenCong, ViTri):
    try:
        cong = CongGacModel.CongGacModel.objects.create(
            TenCong=TenCong,
            ViTri=ViTri
        )
        return {"status": "success", "data": 'Thêm thành công'}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def SuaCong(id,TenCong,ViTri):
    try:
        cong = CongGacModel.CongGacModel.objects.get(pk=id)
        
        cong.TenCong=TenCong
        cong.ViTri=ViTri
        cong.save()
        return {"status": "success", "data": 'Thêm thành công'}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaCong(id):
    try:
        cong = CongGacModel.CongGacModel.objects.get(pk=id)
        
        cong.TrangThai=False
        cong.save()
        return {"status": "success", "data": 'Thành công'}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def LayDanhSachCong():
    try:
        ds_cong = CongGacModel.CongGacModel.objects.filter(TrangThai=True).values('id', 'TenCong', 'ViTri')
        data = list(ds_cong)
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}



def ThemTrucBan(ngay,TBTruong,TBPho):
    try:
        if isinstance(ngay, str):
            ngay = date.fromisoformat(ngay) 
        if date.today() > ngay:
            return {"status": "error", "message": "Không thể thêm trực ban vào quá khứ"}
        banghi= PCTrucBanModel.PCTrucBanModel.objects.filter(Ngay=ngay).exists()
        if banghi:
            return {"status": "error", "message": "Đã có danh sách trực ban ngày này"}
        SQ1 = LaySQTuMa(TBTruong)
        if not SQ1:
            return {"status": "error", "message": "Không tồn tại mã quân nhân của trực ban trưởng"}
        SQ2 = LaySQTuMa(TBPho)
        if not SQ2:
            return {"status": "error", "message": "Không tồn tại mã quân nhân của trực ban phó"}
        if TBTruong == TBPho:
            return {"status": "error", "message": "Một người chỉ trực một vị trí một ngày"}
        
        PCTrucBanModel.PCTrucBanModel.objects.create(
            Ngay=ngay,
            TBTruong=SQ1,
            TBPho=SQ2
        )
        return {"status": "success", "data": 'Thành công'}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def SuaTrucBan(id, ngay,TBTruong,TBPho):
    try:
        if isinstance(ngay, str):
            ngay = date.fromisoformat(ngay) 
        if date.today() > ngay:
            return {"status": "error", "message": "Không thể sửa trực ban vào quá khứ"}
        SQ1 = LaySQTuMa(TBTruong)
        if not SQ1:
            return {"status": "error", "message": "Không tồn tại mã quân nhân của trực ban trưởng"}
        SQ2 = LaySQTuMa(TBPho)
        if not SQ2:
            return {"status": "error", "message": "Không tồn tại mã quân nhân của trực ban phó"}
        
        if TBTruong == TBPho:
            return {"status": "error", "message": "Một người chỉ trực một vị trí một ngày"}
        
        pctrucban = PCTrucBanModel.PCTrucBanModel.objects.get(pk=id)
        pctrucban.Ngay=ngay
        pctrucban.TBTruong=SQ1
        pctrucban.TBPho=SQ2
        pctrucban.save()
        return {"status": "success", "data": 'Thành công'}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaTrucBan(id):
    try:
        pctrucban = PCTrucBanModel.PCTrucBanModel.objects.get(pk=id)
        pctrucban.delete()
        return {"status": "success", "data": 'Thành công'}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def ThemCaGac(Ca,TGBatDau,TGKetThuc):
    try:
        cagac = CaGacVBModel.CaGacVBModel.objects.create(
            Ca=Ca,
            TGBatDau=TGBatDau,
            TGKetThuc=TGKetThuc
        )
        return {"status": "success", "data": 'Thêm thành công'}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaCaGac(id):
    try:
        cagac = CaGacVBModel.CaGacVBModel.objects.get(pk=id)
        cagac.TrangThai=False
        cagac.save()
        return {"status": "success", "data": 'Thêm thành công'}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
        

def ThemPCCaGac(Ngay,CongGac):
    try:
        if isinstance(ngay, str):
            ngay = date.fromisoformat(ngay)
        if date.today() > Ngay:
            return {"status": "error", "message": "Không thể phân công gác cho quá khứ"}
        
        cong_gac = CongGacModel.CongGacModel.objects.get(id=CongGac)



        # Lấy danh sách tất cả các ca gác có TrangThai là True
        ca_gac_list = CongGacModel.CongGacModel.objects.filter(TrangThai=True)

        # Tạo các bản ghi phân công vệ binh
        for ca in ca_gac_list:
            PCVeBinhModel.PCVeBinhModel.objects.create(Ngay=Ngay, Ca=ca, CongGac=cong_gac)

        return {"status": "success", "message": "Phân công vệ binh đã được tạo thành công."}

    except CongGacModel.CongGacModel.DoesNotExist:
        return {"status": "error", "message": "Cổng gác không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}


def XoaPCCaGac(Ngay,CongGac):
    try:
        if isinstance(ngay, str):
            ngay = date.fromisoformat(ngay)
        if date.today() > Ngay:
            return {"status": "error", "message": "Không thể xóa lịch sử gác"}
        
        cong_gac = CongGacModel.CongGacModel.objects.get(id=CongGac)
        pccagac = PCVeBinhModel.PCVeBinhModel.objects.filter(Ngay=Ngay, CongGac=cong_gac)
        for i in pccagac:
            i.delete()
        return {"status": "success", "message": "Xóa thành công."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThemPhanCongChiTiet(PCCaGac,MaCS):
    try:
        pccagac = PCVeBinhModel.PCVeBinhModel.objects.get(pk=PCCaGac)
        ca_gac_id = pccagac.Ca.id
        CS = LayChienSiTuMa(MaCS)
        if not CS:
            return {"status": "error", "message": "Mã không hợp lệ"}
        cong_trung = tim_ten_cong(MaCS,ca_gac_id,pccagac.Ngay)
        if not cong_trung:
            {"status": "error", "message": f"Chiến sĩ này đã gác ca này tại cổng {cong_trung[0]}"}
        PCVeBinhChiTietModel.PCVeBinhChiTietModel.objects.create(
            PCVB=pccagac,
            ChienSi=CS
        )
        return {"status": "success", "message": "Thêm thành công."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def tim_ten_cong(ma_chien_si, ca_gac_id, ngay):
    try:
        # Lấy đối tượng chiến sĩ dựa trên mã
        chien_si = ChienSiModel.ChienSiModel.objects.get(Ma=ma_chien_si)
        

        # Tìm tất cả các bản ghi phân công vệ binh chi tiết
        pccb_chi_tiet = PCVeBinhChiTietModel.PCVeBinhChiTietModel.objects.filter(
            ChienSi=chien_si,
            PCVB__Ca_id=ca_gac_id,
            PCVB__Ngay=ngay
        ).select_related('PCVB__CongGac')

        # Kiểm tra nếu không có bản ghi nào thì trả về None
        if not pccb_chi_tiet.exists():
            return None

        # Tạo danh sách tên cổng
        ten_cac_cong = [pcvb_chi_tiet.PCVB.CongGac.TenCong for pcvb_chi_tiet in pccb_chi_tiet]

        return ten_cac_cong

    except ChienSiModel.ChienSiModel.DoesNotExist:
        return {"status": "error", "message": "Mã không hợp lệ"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def lay_ngay_theo_cong(cong_gac_id):
    try:
        # Lấy danh sách các ngày duy nhất có bản ghi với id cổng đã cho
        ngay_danh_sach = (
            PCVeBinhModel.PCVeBinhModel.objects.filter(CongGac_id=cong_gac_id)
            .order_by('Ngay')  # Sắp xếp theo ngày
            .values('id', 'Ngay')
            .distinct()  # Loại bỏ các ngày trùng lặp
        )
        
        # Chuyển đổi QuerySet thành danh sách
        ngay_danh_sach = list(ngay_danh_sach)

        return {"status": "error", "data": ngay_danh_sach}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def laycagaccong(ngay, cong_id):
    try:
        # Lấy tất cả các bản ghi có ngày và id cổng trùng khớp
        ca_gac_list = (
            PCVeBinhModel.PCVeBinhModel.objects.filter(Ngay=ngay, CongGac_id=cong_id)
            .select_related('Ca')  # Tối ưu hóa truy vấn để lấy thông tin Ca
            .values('Ca__id', 'Ca__Ca')  # Trích xuất tên ca gác
        )

        # Chuyển đổi QuerySet thành danh sách
        ca_gac_list = list(ca_gac_list)

        return {"status": "error", "data": ca_gac_list}


    except Exception as e:
        return {"status": "error", "message": str(e)}


def xem_phan_cong_chi_tiet(pcvebinh_id):
    try:
        # Lấy danh sách các chi tiết phân công liên quan đến PCVeBinh
        phan_cong_chi_tiet = (
            PCVeBinhChiTietModel.PCVeBinhChiTietModel.objects.filter(PCVB_id=pcvebinh_id)
            .select_related('ChienSi')  # Tối ưu hóa truy vấn để lấy thông tin ChienSi
            .values('id', 'ChienSi__HoTen', 'ChienSi__Ma')  # Lấy thông tin cần thiết của ChienSi và id phân công chi tiết
        )

        # Chuyển đổi QuerySet thành danh sách
        phan_cong_chi_tiet_list = list(phan_cong_chi_tiet)

        return {"status": "success", "data": phan_cong_chi_tiet_list}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def xoa_phan_cong_chi_tiet(id):
    try:
        # Tìm bản ghi phân công chi tiết theo id
        phan_cong_chi_tiet = PCVeBinhChiTietModel.PCVeBinhChiTietModel.objects.select_related('PCVB').get(id=id)
        
        # Lấy ngày từ bản ghi PCVeBinh
        ngay = phan_cong_chi_tiet.PCVB.Ngay
        
        # Kiểm tra nếu ngày nhỏ hơn ngày hiện tại
        if ngay < date.today():
            return {"status": "error", "message": "Ngày của ca gác đã xảy ra trong quá khứ, không thể xóa."}

        # Nếu ngày không nhỏ hơn hiện tại, thực hiện xóa bản ghi
        phan_cong_chi_tiet.delete()
        return {"status": "success", "message": "Đã xóa thành công."}

    except PCVeBinhChiTietModel.PCVeBinhChiTietModel.DoesNotExist:
        return {"status": "error", "message": "Bản ghi không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XemTatCaTrucBan():
    try:
        # Lấy tất cả các bản ghi từ PCTrucBanModel và sắp xếp theo ngày giảm dần
        truc_ban_list = (
            PCTrucBanModel.PCTrucBanModel.objects.all()
            .order_by('-Ngay')  # Sắp xếp theo ngày giảm dần
            .values('id', 'Ngay')  # Lấy id và ngày của các bản ghi
        )
        
        # Chuyển đổi QuerySet thành danh sách
        truc_ban_list = list(truc_ban_list)

        return {"status": "success", "data": truc_ban_list}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def XemChiTietTrucBan(id):
    try:
        # Tìm bản ghi theo id
        truc_ban = PCTrucBanModel.PCTrucBanModel.objects.get(id=id)
        
        # Chuyển đổi bản ghi thành dictionary
        truc_ban_data = {
            "id": truc_ban.id,
            "Ngay": truc_ban.Ngay,
            "TBTruong": truc_ban.TBTruong.id if truc_ban.TBTruong else None,
            "TBPho": truc_ban.TBPho.id if truc_ban.TBPho else None,
            "TBTruong_HoTen": truc_ban.TBTruong.HoTen if truc_ban.TBTruong else None,
            "TBPho_HoTen": truc_ban.TBPho.HoTen if truc_ban.TBPho else None,
        }
        
        return {"status": "success", "data": truc_ban_data}

    except PCTrucBanModel.PCTrucBanModel.DoesNotExist:
        return {"status": "error", "message": "Bản ghi không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}

    


