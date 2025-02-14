from model import NhomDonViModel



def ThemNhomDonVi(TenNhom,GhiChu):
    try:
        Them = NhomDonViModel.NhomDonViModel(
            TenNhom = TenNhom,
            GhiChu = GhiChu
        )
        Them.save()
        return {"status": "success"}
    except:
        return {"status": "error"}
    

def SuaNhomDonVi(id,TenNhom,GhiChu):
    try:
        Nhom = NhomDonViModel.NhomDonViModel.objects.get(pk=id)
        Nhom.TenNhom = TenNhom
        Nhom.GhiChu = GhiChu
        
        # Lưu các thay đổi vào cơ sở dữ liệu
        Nhom.save()

        return {"status": "success", "message": "Cập nhật Nhóm Đơn Vị thành công."}

    except NhomDonViModel.NhomDonViModel.DoesNotExist:
        return {"status": "error", "message": "Nhóm Đơn Vị với id được cung cấp không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaNhomDonVi(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        Nhom = NhomDonViModel.NhomDonViModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        Nhom.delete()

        return {"status": "success", "message": "Nhóm Đơn Vị đã được xóa thành công."}

    except NhomDonViModel.NhomDonViModel.DoesNotExist:
        return {"status": "error", "message": "Nhóm Đơn Vị với id được cung cấp không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TimNhomDonVi(TenNhom):
    try:
        # Tìm kiếm các đối tượng có tên nhóm tương ứng
        NhomList = NhomDonViModel.NhomDonViModel.objects.filter(TenNhom__icontains=TenNhom)

        if NhomList.exists():
            # Nếu có kết quả, trả về danh sách các đối tượng
            return {"status": "success", "data": list(NhomList.values())}
        else:
            # Nếu không tìm thấy kết quả nào
            return {"status": "success", "data": list()}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TatCaNhomDonVi():
    try:
        # Lấy tất cả các đối tượng từ mô hình
        nhom_list = NhomDonViModel.NhomDonViModel.objects.all()

        # Chuyển đổi dữ liệu thành dạng có thể trả về
        data = list(nhom_list.values())  # Chuyển đổi queryset thành danh sách dict

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThongTinNhomDonVi(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        nhom = NhomDonViModel.NhomDonViModel.objects.get(pk=id)

        # Chuyển đổi đối tượng thành dict
        data = {
            "id": nhom.id,
            "TenNhom": nhom.TenNhom,
            "GhiChu": nhom.GhiChu
        }

        return {"status": "success", "data": data}

    except NhomDonViModel.NhomDonViModel.DoesNotExist:
        return {"status": "error", "message": "Nhóm Đơn Vị với id được cung cấp không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
