from model import NhomDonViModel
from model import NhomDonViModel,CapNhomDonViModel


def ThemCapNhomDonVi(NhomDonVi,Ten,CapTren):
    try:
        NhomDV = NhomDonViModel.NhomDonViModel.objects.get(pk=NhomDonVi)
        Them = CapNhomDonViModel.CapNhomDonViModel(
            id_NhomDonVi = NhomDV,
            CapTren = CapTren,
            Ten = Ten
        )
        Them.save()
        return {"status": "success", "message": "Thêm thành công."}
    except:
        return {"status": "error", "message": "Thêm thất bại."}
    

def SuaCapNhomDonVi(id,NhomDonVi,Ten,Cap):
    try:
        NhomDV = NhomDonViModel.NhomDonViModel.objects.get(pk=NhomDonVi)
        CapNhom = CapNhomDonViModel.CapNhomDonViModel.objects.get(pk=id)
        CapNhom.id_NhomDonVi = NhomDV
        CapNhom.Cap= Cap
        CapNhom.Ten= Ten
        
        # Lưu các thay đổi vào cơ sở dữ liệu
        CapNhom.save()

        return {"status": "success", "message": "Cập nhật thành công."}

    except CapNhomDonViModel.CapNhomDonViModel.DoesNotExist:
        return {"status": "error", "message": "id được cung cấp không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaCapNhomDonVi(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        CapNhom = CapNhomDonViModel.CapNhomDonViModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CapNhom.delete()

        return {"status": "success", "message": "Xóa thành công."}

    except CapNhomDonViModel.CapNhomDonViModel.DoesNotExist:
        return {"status": "error", "message": "id được cung cấp không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TimKiemTheoNhom(id_nhom):
    try:
        # Tìm các đối tượng CapNhomDonVi liên quan đến id_nhom
        cap_list = CapNhomDonViModel.CapNhomDonViModel.objects.filter(id_NhomDonVi_id=id_nhom)

        # Chuyển đổi dữ liệu thành dạng có thể trả về
        data = list(cap_list.values("id", "Ten", "CapTren__Ten"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThongTin(id):
    try:
        # Tìm đối tượng CapNhomDonViModel theo id
        cap_nhom = CapNhomDonViModel.CapNhomDonViModel.objects.get(pk=id)

        # Chuyển đổi dữ liệu thành dạng từ điển
        data = {
            "id": cap_nhom.id,
            "Ten": cap_nhom.Ten,
            "CapTren": cap_nhom.CapTren.Ten if cap_nhom.CapTren else None  # Xử lý trường hợp CapTren có thể là None
        }

        return {"status": "success", "data": data}

    except CapNhomDonViModel.CapNhomDonViModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy đối tượng với id này."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def ThongTinChiTiet(id):
    try:
        # Lấy thông tin nhóm đơn vị dựa trên id
        cap_nhom_don_vi = CapNhomDonViModel.CapNhomDonViModel.objects.get(id=id)
        
        # Lấy tên của id_NhomDonVi
        ten_id_nhom_don_vi = cap_nhom_don_vi.id_NhomDonVi.Ten if cap_nhom_don_vi.id_NhomDonVi else None
        
        # Lấy tên của đơn vị cấp trên nếu có
        ten_don_vi_cap_tren = cap_nhom_don_vi.CapTren.Ten if cap_nhom_don_vi.CapTren else None
        
        # Trả về thông tin chi tiết
        return {
            "status": "success",
            "data": {
                "TenNhomDonVi": cap_nhom_don_vi.Ten,
                "TenIDNhomDonVi": ten_id_nhom_don_vi,
                "TenDonViCapTren": ten_don_vi_cap_tren
            }
        }

    except CapNhomDonViModel.CapNhomDonViModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy nhóm đơn vị với id này"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def CapTrenThemCNDV(id_nhom):
    try:
        # Tìm các đối tượng CapNhomDonVi liên quan đến id_nhom
        cap_list = CapNhomDonViModel.CapNhomDonViModel.objects.filter(id_NhomDonVi_id=id_nhom)

        # Chuyển đổi dữ liệu thành dạng có thể trả về
        data = [{"id": "", "Ten": "Không có đơn vị cấp trên"}]  # Thêm dòng mặc định
        data += list(cap_list.values("id", "Ten"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}