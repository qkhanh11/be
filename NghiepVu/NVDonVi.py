from model import NhomDonViModel
from model import NhomDonViModel,CapNhomDonViModel,DonViModel


def ThemDonVi(TenDonVi, DiaDiem, MaDonVi, id_DonViCapTren, SoDienThoai, CapNhomDonVi):
    DonViCapTren = None
    try:
        DonViCapTren = DonViModel.DonViModel.objects.get(pk=id_DonViCapTren)
    except:
        pass
    try:
        # Tạo đối tượng DonViModel mới
        CapNhom = CapNhomDonViModel.CapNhomDonViModel.objects.get(pk=CapNhomDonVi)
        don_vi = DonViModel.DonViModel(
            TenDonVi=TenDonVi,
            DiaDiem=DiaDiem,
            MaDonVi=MaDonVi,
            id_DonViCapTren=DonViCapTren,  # Sử dụng đối tượng DonViCapTren trực tiếp
            SoDienThoai=SoDienThoai,
            CapNhomDonVi=CapNhom  # Sử dụng đối tượng CapNhom trực tiếp
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        don_vi.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaDonVi(id,TenDonVi, DiaDiem, MaDonVi, id_DonViCapTren, SoDienThoai, CapNhomDonVi):
    DonViCapTren = None
    try:
        DonViCapTren = DonViModel.DonViModel.objects.get(pk=id_DonViCapTren)
    except:
        pass
    try:
        # Tạo đối tượng DonViModel mới
        CapNhom = CapNhomDonViModel.CapNhomDonViModel.objects.get(pk=CapNhomDonVi)

        don_vi = DonViModel.DonViModel.objects.get(pk=id)
        don_vi.TenDonVi=TenDonVi,
        don_vi.DiaDiem=DiaDiem,
        don_vi.MaDonVi=MaDonVi,
        don_vi.id_DonViCapTren=DonViCapTren,  # Sử dụng đối tượng DonViCapTren trực tiếp
        don_vi.SoDienThoai=SoDienThoai,
        don_vi.CapNhomDonVi=CapNhom  # Sử dụng đối tượng CapNhom trực tiếp
        

        # Lưu đối tượng vào cơ sở dữ liệu
        don_vi.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Sửa thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def XoaDonVi(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        DonVi = DonViModel.DonViModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        DonVi.delete()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TimDVCapTren(id_CapNhomDV):
    CapHienTai = CapNhomDonViModel.CapNhomDonViModel.objects.get(pk=id)

        # Tìm đối tượng CapNhomDonViModel có Cap nhỏ hơn 1 đơn vị
    CapTren = CapHienTai.CapTren

    # Tìm tất cả các đơn vị có cấp nhóm là CapTren
    don_vi_list = DonViModel.DonViModel.objects.filter(CapNhomDonVi=CapTren)

    # Chuyển đổi dữ liệu thành danh sách các từ điển chứa id, tên, và mã đơn vị
    data = list(don_vi_list.values("id", "TenDonVi", "MaDonVi"))

    return {"status": "success", "data": data}

def TimDonVi(TimKiem):
    try:
        # Tìm tất cả các đơn vị có tên hoặc mã đơn vị chứa từ khóa tìm kiếm
        don_vi_list = DonViModel.DonViModel.objects.filter(
            TenDonVi__icontains=TimKiem
        ) | DonViModel.DonViModel.objects.filter(
            MaDonVi__icontains=TimKiem
        )

        # Chuyển đổi dữ liệu thành danh sách các từ điển chứa id, tên, và mã đơn vị
        data = list(don_vi_list.values("id", "TenDonVi", "MaDonVi"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}


def CacDonViCon(id):
    try:
        # Tìm tất cả các đơn vị có id_DonViCapTren là id của đơn vị cha
        don_vi_con_list = DonViModel.DonViModel.objects.filter(id_DonViCapTren_id=id)

        # Chuyển đổi dữ liệu thành danh sách các từ điển chứa id, tên, và mã đơn vị
        data = list(don_vi_con_list.values("id", "TenDonVi", "MaDonVi"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThongTinDonVi(id):
    try:
        # Lấy đối tượng DonViModel với id cụ thể
        don_vi = DonViModel.DonViModel.objects.get(pk=id)

        # Lấy thông tin cấp nhóm đơn vị
        cap_nhom_don_vi = don_vi.CapNhomDonVi
        id_cap_nhom = cap_nhom_don_vi.id if cap_nhom_don_vi else None
        ten_cap_nhom = cap_nhom_don_vi.Ten if cap_nhom_don_vi else None

        # Lấy thông tin nhóm đơn vị từ cấp nhóm đơn vị
        nhom_don_vi = cap_nhom_don_vi.id_NhomDonVi if cap_nhom_don_vi else None
        id_nhom_don_vi = nhom_don_vi.id if nhom_don_vi else None
        ten_nhom_don_vi = nhom_don_vi.TenNhom if nhom_don_vi else None

        # Lấy thông tin đơn vị cấp trên nếu có
        don_vi_cap_tren = don_vi.id_DonViCapTren
        ten_don_vi_cap_tren = don_vi_cap_tren.TenDonVi if don_vi_cap_tren else None

        # Chuyển đổi dữ liệu thành dạng từ điển chứa thông tin chi tiết của đơn vị
        data = {
            "id": don_vi.id,
            "TenDonVi": don_vi.TenDonVi,
            "DiaDiem": don_vi.DiaDiem,
            "MaDonVi": don_vi.MaDonVi,
            "TenDonViCapTren": ten_don_vi_cap_tren,
            "SoDienThoai": don_vi.SoDienThoai,
            "CapNhomDonVi": {
                "id": id_cap_nhom,
                "Ten": ten_cap_nhom
            },
            "NhomDonVi": {
                "id": id_nhom_don_vi,
                "Ten": ten_nhom_don_vi
            }
        }

        return {"status": "success", "data": data}

    except DonViModel.DonViModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy đơn vị với id này"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def DropDownDV(id_CapDonVi):
    try:
        # Lọc các đơn vị dựa trên id_CapDonVi
        don_vi_list = DonViModel.DonViModel.objects.filter(CapNhomDonVi__id=id_CapDonVi).values('id', 'TenDonVi', 'MaDonVi')
        
        # Nếu không có đơn vị nào được tìm thấy
        if not don_vi_list:
            return {"status": "error", "message": "Không tìm thấy đơn vị với id này"}
        
        # Trả về dữ liệu với status success
        return {"status": "success", "data": list(don_vi_list)}

    except DonViModel.DonViModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy đơn vị với id này"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def DonViCon(id):
    try:
        # Tìm đơn vị cha dựa trên id
        don_vi_cha = DonViModel.DonViModel.objects.get(pk=id)

        # Lấy tất cả các đơn vị con liên quan
        don_vi_con_list = don_vi_cha.don_vi_con.all()

        # Tạo danh sách kết quả đơn vị con
        results = [{"id": dv.id, "TenDonVi": dv.TenDonVi, "MaDonVi": dv.MaDonVi} for dv in don_vi_con_list]

        return {
            "status": "success",
            "data": results
        }
    except DonViModel.DonViModel.DoesNotExist:
        return {"status": "error", "message": "Đơn vị không tồn tại"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def DonViChaTheoNhom(id):
    try:
        # Lọc tất cả các đối tượng CapNhomDonViModel có CapTren là None và id_NhomDonVi là id
        cap_nhom_don_vi = CapNhomDonViModel.CapNhomDonViModel.objects.filter(id_NhomDonVi=id, CapTren__isnull=True)

        # Lọc tất cả các đối tượng DonViModel có CapNhomDonVi nằm trong danh sách cap_nhom_don_vi
        don_vi_list = DonViModel.DonViModel.objects.filter(CapNhomDonVi__in=cap_nhom_don_vi)

        # Tạo danh sách kết quả đơn vị
        results = [{"id": dv.id, "TenDonVi": dv.TenDonVi, "MaDonVi": dv.MaDonVi} for dv in don_vi_list]

        return {
            "status": "success",
            "data": results
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TimDonVi(Nhom, TimKiem=None):
    # Lọc các đơn vị theo id_NhomDonVi của lớp CapNhomDonViModel
    don_vi_list = DonViModel.DonViModel.objects.filter(CapNhomDonVi__id_NhomDonVi=Nhom)
    
    # Nếu TimKiem không phải là None, thêm điều kiện lọc theo tên hoặc mã đơn vị
    if TimKiem:
        don_vi_list = don_vi_list.filter(TenDonVi__icontains=TimKiem) | don_vi_list.filter(MaDonVi__icontains=TimKiem)
    
    # Chuyển đổi QuerySet thành danh sách các dictionary chỉ chứa các trường cần thiết
    results = list(don_vi_list.values('id', 'MaDonVi', 'TenDonVi', 'DiaDiem', 'SoDienThoai'))
    
    # Trả về JsonResponse với kết quả
    return {
        "status": "success",
        "data": results
    }


def DropdownDonViCha(id_capdonvi):
    try:
        # Tìm cấp nhóm đơn vị con dựa trên id_capdonvi
        cap_don_vi_con = CapNhomDonViModel.CapNhomDonViModel.objects.get(id=id_capdonvi)

        # Tìm cấp nhóm đơn vị cha của cấp nhóm đơn vị con
        cap_don_vi_cha = cap_don_vi_con.CapTren

        # Tìm các đơn vị có cấp nhóm đơn vị bằng với cấp nhóm đơn vị cha
        don_vi_cha = DonViModel.DonViModel.objects.filter(CapNhomDonVi=cap_don_vi_cha).values('id', 'TenDonVi')

        # Trả về danh sách id và tên của các đơn vị cha
        return {
            "status": "success",
            "data": list(don_vi_cha)
        }

    except CapNhomDonViModel.CapNhomDonViModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy cấp nhóm đơn vị với id đã cho."}
    except Exception as e:
        return {"status": "error", "message": str(e)}