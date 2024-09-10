from model import CVQNCNModel,CVSiQuanModel,CapDonViModel


def ThemCVSQ(TenChucVu,id_CapNhomDonVi):
    try:
        # Tạo đối tượng DonViModel mới
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id_CapNhomDonVi)
        CVSQ = CVSiQuanModel.CVSiQuanModel(
            TenChucVu=TenChucVu,
            id_CapNhomDonVi=CapNhom  # Sử dụng đối tượng CapNhom trực tiếp
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        CVSQ.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def ThemCVQNCN(TenChucVu,id_CapNhomDonVi):
    try:
        # Tạo đối tượng DonViModel mới
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id_CapNhomDonVi)
        CVQNCN = CVQNCNModel.CVQNCNModel(
            TenChucVu=TenChucVu,
            id_CapNhomDonVi=CapNhom  # Sử dụng đối tượng CapNhom trực tiếp
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        CVQNCN.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaCVSQ(id,TenChucVu,id_CapNhomDonVi):
    try:
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id_CapNhomDonVi)
        CVSQ = CVSiQuanModel.CVSiQuanModel.objects.get(pk=id)
        CVSQ.TenChucVu=TenChucVu,
        CVSQ.id_CapNhomDonVi=CapNhom
        

        # Lưu đối tượng vào cơ sở dữ liệu
        CVSQ.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Sửa thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaCVQNVN(id,TenChucVu,id_CapNhomDonVi):
    try:
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id_CapNhomDonVi)
        CVQNCN = CVQNCNModel.CVQNCNModel.objects.get(pk=id)
        CVQNCN.TenChucVu=TenChucVu,
        CVQNCN.id_CapNhomDonVi=CapNhom
        

        # Lưu đối tượng vào cơ sở dữ liệu
        CVQNCN.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Sửa thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def XoaCVSQ(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        CVSQ = CVSiQuanModel.CVSiQuanModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CVSQ.delete()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaCVQNCN(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        CVQNCN = CVQNCNModel.CVQNCNModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CVQNCN.delete()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def CVSQ(id_CapNhomDonVi):
    try:
        # Lấy tất cả các chức vụ sĩ quan có id_CapNhomDonVi tương ứng
        chuc_vu_list = CVSiQuanModel.CVSiQuanModel.objects.filter(id_CapNhomDonVi_id=id_CapNhomDonVi)

        # Chuyển đổi dữ liệu thành danh sách các từ điển chứa id và tên chức vụ
        data = list(chuc_vu_list.values("id", "TenChucVu"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}

def CVQNCN(id_CapNhomDonVi):
    try:
        # Lấy tất cả các chức vụ sĩ quan từ mô hình CVQNCNModel
        chuc_vu_list = CVQNCNModel.CVQNCNModel.objects.filter(id_CapNhomDonVi_id=id_CapNhomDonVi)

        # Chuyển đổi dữ liệu thành danh sách các từ điển chứa id và tên chức vụ
        data = list(chuc_vu_list.values("id", "TenChucVu"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XemCVSQTrongDV(id):
    try:
        # Lấy đối tượng CapDonViModel bằng id
        cap_nhom_don_vi = CapDonViModel.CapDonViModel.objects.get(pk=id)
        
        # Lọc tất cả các chức vụ sĩ quan dựa trên id_CapNhomDonVi
        chuc_vu_list = CVSiQuanModel.CVSiQuanModel.objects.filter(id_CapNhomDonVi=cap_nhom_don_vi)
        
        # Chuyển đổi QuerySet thành danh sách các dictionary chỉ chứa các trường cần thiết
        results = list(chuc_vu_list.values('id', 'TenChucVu'))
        
        # Trả về JsonResponse với kết quả
        return {"status": "success", "data": results}
    
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
