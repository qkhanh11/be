from model import CVQNCNModel,CVSiQuanModel,CapDonViModel


def ThemCVSQ(TenChucVu,id_CapDonVi):
    try:
        # Tạo đối tượng DonViModel mới
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id_CapDonVi)
        CVSQ = CVSiQuanModel.CVSiQuanModel(
            TenChucVu=TenChucVu,
            id_CapDonVi=CapNhom  # Sử dụng đối tượng CapNhom trực tiếp
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        CVSQ.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def ThemCVQNCN(TenChucVu,id_CapDonVi):
    try:
        # Tạo đối tượng DonViModel mới
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id_CapDonVi)
        CVQNCN = CVQNCNModel.CVQNCNModel(
            TenChucVu=TenChucVu,
            id_CapDonVi=CapNhom  # Sử dụng đối tượng CapNhom trực tiếp
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        CVQNCN.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaCVSQ(id,TenChucVu,id_CapDonVi):
    try:
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id_CapDonVi)
        CVSQ = CVSiQuanModel.CVSiQuanModel.objects.get(pk=id)
        CVSQ.TenChucVu=TenChucVu,
        CVSQ.id_CapDonVi=CapNhom
        

        # Lưu đối tượng vào cơ sở dữ liệu
        CVSQ.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Sửa thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaCVQNVN(id,TenChucVu,id_CapDonVi):
    try:
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id_CapDonVi)
        CVQNCN = CVQNCNModel.CVQNCNModel.objects.get(pk=id)
        CVQNCN.TenChucVu=TenChucVu,
        CVQNCN.id_CapDonVi=CapNhom
        

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
        CVSQ.TinhTrang=False
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CVSQ.save()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaCVQNCN(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        CVQNCN = CVQNCNModel.CVQNCNModel.objects.get(pk=id)
        CVQNCN.TinhTrang=False
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CVQNCN.save()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def CVSQ(id_CapDonVi):
    try:
        # Lấy tất cả các chức vụ sĩ quan có id_CapDonVi tương ứng
        chuc_vu_list = CVSiQuanModel.CVSiQuanModel.objects.filter(id_CapDonVi_id=id_CapDonVi,TinhTrang=True)

        # Chuyển đổi dữ liệu thành danh sách các từ điển chứa id và tên chức vụ
        data = list(chuc_vu_list.values("id", "TenChucVu"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}

def CVQNCN(id_CapDonVi):
    try:
        # Lấy tất cả các chức vụ sĩ quan từ mô hình CVQNCNModel
        chuc_vu_list = CVQNCNModel.CVQNCNModel.objects.filter(id_CapDonVi_id=id_CapDonVi,TinhTrang=True)

        # Chuyển đổi dữ liệu thành danh sách các từ điển chứa id và tên chức vụ
        data = list(chuc_vu_list.values("id", "TenChucVu"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XemCVSQTrongDV(id):
    try:
        # Lấy đối tượng CapDonViModel bằng id
        cap_nhom_don_vi = CapDonViModel.CapDonViModel.objects.get(pk=id)
        
        # Lọc tất cả các chức vụ sĩ quan dựa trên id_CapDonVi
        chuc_vu_list = CVSiQuanModel.CVSiQuanModel.objects.filter(id_CapDonVi=cap_nhom_don_vi,TinhTrang=True)
        
        # Chuyển đổi QuerySet thành danh sách các dictionary chỉ chứa các trường cần thiết
        results = list(chuc_vu_list.values('id', 'TenChucVu'))
        
        # Trả về JsonResponse với kết quả
        return {"status": "success", "data": results}
    
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
