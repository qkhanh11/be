from model import CongGacModel, PCTrucBanModel, CaGacVBModel, PCGacNgayModel, PCVeBinhModel, PCVeBinhChiTietModel,ChienSiModel
from .NVSiQuan import LaySQTuMa
from .NVChienSi import LayChienSiTuMa
from datetime import date,time
from datetime import datetime



def ChuyenDinhDangNgay(ngay):
    try:
        # Chuyển đổi chuỗi ngày vào định dạng datetime
        ngay_obj = datetime.strptime(ngay, '%Y-%m-%d').date()
        
        # Chuyển đổi datetime thành chuỗi ngày với định dạng hai chữ số cho tháng và ngày
        # ngay_dinh_dang = ngay_obj.strftime('%Y-%m-%d')
        
        return ngay_obj
    except ValueError:
        return {"status": "error", "message": "Ngày không hợp lệ"}


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
        ngay = ChuyenDinhDangNgay(ngay)
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
    

def SuaTrucBan(id,TBTruong,TBPho):
    try:
    
        
        pctrucban = PCTrucBanModel.PCTrucBanModel.objects.get(pk=id)

        
        # Kiểm tra xem ngày của bản ghi có phải là ngày trong quá khứ hay không
        if date.today() > pctrucban.Ngay:
            return {"status": "error", "message": "Không thể sửa trực ban vào ngày đã qua"}
        SQ1 = LaySQTuMa(TBTruong)
        if not SQ1:
            return {"status": "error", "message": "Không tồn tại mã quân nhân của trực ban trưởng"}
        SQ2 = LaySQTuMa(TBPho)
        if not SQ2:
            return {"status": "error", "message": "Không tồn tại mã quân nhân của trực ban phó"}
        
        if TBTruong == TBPho:
            return {"status": "error", "message": "Một người chỉ trực một vị trí một ngày"}
        
        pctrucban = PCTrucBanModel.PCTrucBanModel.objects.get(pk=id)
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


def ThemCaGac(Ca,ThoiGianBatDau,ThoiGianKetThuc):
    try:
        cagac = CaGacVBModel.CaGacVBModel.objects.create(
            Ca=Ca,
            TGBatDau=ThoiGianBatDau,
            TGKetThuc=ThoiGianKetThuc,
        )
        return {"status": "success", "data": 'Thêm thành công'}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def SuaCaGac(id,Ca,ThoiGianBatDau,ThoiGianKetThuc):
    try:
        cagac = CaGacVBModel.CaGacVBModel.objects.get(pk=id)
        cagac.Ca=Ca
        cagac.TGBatDau=ThoiGianBatDau
        cagac.TGKetThuc=ThoiGianKetThuc
        return {"status": "success", "data": 'Sửa thành công'}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

    

def XoaCaGac(id):
    try:
        cagac = CaGacVBModel.CaGacVBModel.objects.get(pk=id)
        cagac.TrangThai=False
        cagac.save()
        return {"status": "success", "data": 'Xóa thành công'}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
        

def ThemPCCaGac(Ngay,CongGac):
    try:
        ngay = ChuyenDinhDangNgay(Ngay)
        if date.today() > ngay:
            return {"status": "error", "message": "Không thể phân công gác cho quá khứ"}
        
        cong_gac = CongGacModel.CongGacModel.objects.get(id=CongGac)

        NgayCong = PCGacNgayModel.PCGacNgayModel.objects.create(Ngay=Ngay, CongGac=cong_gac)
        NgayCong.save()

        # Lấy danh sách tất cả các ca gác có TrangThai là True
        ca_gac_list = CaGacVBModel.CaGacVBModel.objects.filter(TrangThai=True)

        # Tạo các bản ghi phân công vệ binh
        for ca in ca_gac_list:
            PCVeBinhModel.PCVeBinhModel.objects.create(Ca=ca, NgayCong=NgayCong)

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
        cong_trung = tim_ten_cong(CS,pccagac.Ca,pccagac.NgayCong.Ngay)
        if cong_trung:
            return {"status": "error", "message": f"Chiến sĩ này đã gác ca này tại cổng {cong_trung}"}
        PCVeBinhChiTietModel.PCVeBinhChiTietModel.objects.create(
            PCVB=pccagac,
            ChienSi=CS
        )
        return {"status": "success", "message": "Thêm thành công."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def tim_ten_cong(ChienSi, Ca, Ngay):
    # Tìm các bản ghi trong PCVeBinhModel có cùng Ca và NgayCong
    Ngay_gac = PCGacNgayModel.PCGacNgayModel.objects.filter(Ngay=Ngay)
    for i in Ngay_gac:
        PCVeBinh = PCVeBinhModel.PCVeBinhModel.objects.filter(Ca=Ca,NgayCong=i)
        for j in PCVeBinh:
            PCChiTiet = PCVeBinhChiTietModel.PCVeBinhChiTietModel.objects.filter(ChienSi=ChienSi, PCVB=j).first()
            
            if PCChiTiet:
                print(j.NgayCong.CongGac.TenCong)
                return j.NgayCong.CongGac.TenCong
    return None
    


def lay_ngay_theo_cong(cong_gac_id):
    try:
        # Lấy danh sách các ngày duy nhất có bản ghi với id cổng đã cho
        ngay_danh_sach = (
            PCGacNgayModel.PCGacNgayModel.objects.filter(CongGac_id=cong_gac_id)
            .order_by('-Ngay')  # Sắp xếp theo ngày
            .values('id', 'Ngay')
            .distinct()  # Loại bỏ các ngày trùng lặp
        )
        
        # Chuyển đổi QuerySet thành danh sách
        ngay_danh_sach = list(ngay_danh_sach)

        return {"status": "success", "data": ngay_danh_sach}

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

        return {"status": "success", "data": ca_gac_list}


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
        ngay = phan_cong_chi_tiet.PCVB.NgayCong.Ngay
        
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
            .values(
                'id', 
                'Ngay', 
                'TBTruong__HoTen',  # Lấy tên của Trực Ban Trưởng
                'TBPho__HoTen'  # Lấy tên của Trực Ban Phó
            )  # Lấy id và ngày của các bản ghi
        )
        
        # Chuyển đổi QuerySet thành danh sách
        truc_ban_list = list(truc_ban_list)

        return {"status": "success", "data": truc_ban_list}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TimTrucBanTheoKhoangNgay(ngay_bat_dau, ngay_ket_thuc):
    try:
        # Chuyển đổi chuỗi ngày thành đối tượng datetime
        ngay_bat_dau = datetime.strptime(ngay_bat_dau, '%Y-%m-%d').date()
        ngay_ket_thuc = datetime.strptime(ngay_ket_thuc, '%Y-%m-%d').date()

        # Lấy các bản ghi từ PCTrucBanModel trong khoảng thời gian xác định và sắp xếp theo ngày giảm dần
        truc_ban_list = (
            PCTrucBanModel.PCTrucBanModel.objects.filter(Ngay__range=[ngay_bat_dau, ngay_ket_thuc])
            .order_by('-Ngay')  # Sắp xếp theo ngày giảm dần
            .values(
                'id', 
                'Ngay', 
                'TBTruong__HoTen',  # Lấy tên của Trực Ban Trưởng
                'TBPho__HoTen'  # Lấy tên của Trực Ban Phó
            )
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


def LayThongTinTrucBanTheoID(truc_ban_id):
    try:
        # Lấy bản ghi từ PCTrucBanModel dựa trên id được truyền vào
        truc_ban = PCTrucBanModel.PCTrucBanModel.objects.filter(id=truc_ban_id).values(
            'TBTruong__HoTen',  # Họ tên Trực Ban Trưởng
            'TBTruong__ChucVu__TenChucVu',  # Tên chức vụ Trực Ban Trưởng
            'TBTruong__DonVi__TenDonVi',  # Tên đơn vị Trực Ban Trưởng
            'TBTruong__DonVi__SoDienThoai',  # Số điện thoại Trực Ban Trưởng
            'TBPho__HoTen',  # Họ tên Trực Ban Phó
            'TBPho__ChucVu__TenChucVu',  # Tên chức vụ Trực Ban Phó
            'TBPho__DonVi__TenDonVi',  # Tên đơn vị Trực Ban Phó
            'TBPho__DonVi__SoDienThoai'  # Số điện thoại Trực Ban Phó
        ).first()

        if truc_ban:
            # Định dạng dữ liệu trả về theo mẫu
            result = {
                "TBTruong": {
                    "HoTen": truc_ban.get('TBTruong__HoTen', ''),
                    "ChucVu": truc_ban.get('TBTruong__ChucVu__TenChucVu', ''),
                    "DonVi": truc_ban.get('TBTruong__DonVi__TenDonVi', ''),
                    "SoDienThoai": truc_ban.get('TBTruong__DonVi__SoDienThoai', '')
                },
                "TBPho": {
                    "HoTen": truc_ban.get('TBPho__HoTen', ''),
                    "ChucVu": truc_ban.get('TBPho__ChucVu__TenChucVu', ''),
                    "DonVi": truc_ban.get('TBPho__DonVi__TenDonVi', ''),
                    "SoDienThoai": truc_ban.get('TBPho__DonVi__SoDienThoai', '')
                }
            }
            return {"status": "success", "data": result}
        else:
            return {"status": "error", "message": "Không tìm thấy ca trực ban với ID này"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def LayTatCaCaGac():
    try:
        # Lấy tất cả các bản ghi từ CaGacVBModel
        danh_sach_ca_gac = CaGacVBModel.CaGacVBModel.objects.filter(TrangThai=True)
        
        # Chuyển đổi QuerySet thành danh sách các bản ghi với các trường cần thiết
        data = list(danh_sach_ca_gac.values('id', 'Ca', 'TGBatDau', 'TGKetThuc'))

        return {"status": "success", "data": data}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def LayCaGacTrongNgayCong(id_NgayCong):
    try:
        # Tìm ngày công theo ID
        ngay_cong = PCGacNgayModel.PCGacNgayModel.objects.get(pk=id_NgayCong)
        
        # Lấy danh sách các ca gác trong ngày công đó
        ca_gac_list = PCVeBinhModel.PCVeBinhModel.objects.filter(NgayCong=ngay_cong).select_related('Ca')

        # Tạo danh sách các ca gác với thông tin chi tiết
        data = []
        for ca_gac in ca_gac_list:
            data.append({
                "id": ca_gac.id,
                "Ca": ca_gac.Ca.Ca,
                "TGBatDau": ca_gac.Ca.TGBatDau,
                "TGKetThuc": ca_gac.Ca.TGKetThuc
            })
        
        return {"status": "success", "data": data}

    except PCGacNgayModel.PCGacNgayModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy Ngày Công với ID này"}
    except Exception as e:
        return {"status": "error", "message": str(e)}



