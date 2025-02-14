from model import NhomDonViModel
from model import NhomDonViModel,CapDonViModel


def ThemCapNhomDonVi(NhomDonVi,Ten,CapTren):
    try:
        # Lấy đối tượng NhomDonVi từ id
        NhomDV = NhomDonViModel.NhomDonViModel.objects.get(pk=NhomDonVi)
        
        # Nếu CapTren không rỗng, lấy đối tượng CapNhomDonVi từ id
        CapNhomTren = None
        if CapTren:
            CapNhomTren = CapDonViModel.CapDonViModel.objects.get(pk=CapTren)
        
        # Tạo đối tượng CapNhomDonVi mới
        Them = CapDonViModel.CapDonViModel(
            id_NhomDonVi=NhomDV,
            Ten=Ten,
            CapTren=CapNhomTren
        )
        
        # Lưu đối tượng vào database
        Them.save()
        return {"status": "success", "message": "Thêm thành công."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def SuaCapNhomDonVi(id,NhomDonVi,Ten,Cap):
    try:
        NhomDV = NhomDonViModel.NhomDonViModel.objects.get(pk=NhomDonVi)
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id)
        CapNhom.id_NhomDonVi = NhomDV
        CapNhom.Cap= Cap
        CapNhom.Ten= Ten
        
        # Lưu các thay đổi vào cơ sở dữ liệu
        CapNhom.save()

        return {"status": "success", "message": "Cập nhật thành công."}

    except CapDonViModel.CapDonViModel.DoesNotExist:
        return {"status": "error", "message": "id được cung cấp không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaCapNhomDonVi(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        CapNhom = CapDonViModel.CapDonViModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CapNhom.delete()

        return {"status": "success", "message": "Xóa thành công."}

    except CapDonViModel.CapDonViModel.DoesNotExist:
        return {"status": "error", "message": "id được cung cấp không tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TimKiemTheoNhom(id_nhom):
    try:
        # Tìm các đối tượng CapNhomDonVi liên quan đến id_nhom
        cap_list = CapDonViModel.CapDonViModel.objects.filter(id_NhomDonVi_id=id_nhom)

        # Chuyển đổi dữ liệu thành dạng có thể trả về
        data = []
        for cap in cap_list:
            ten_cap = cap.Ten
            cap_tren_ten = cap.CapTren.Ten if cap.CapTren else ""
            ten = f"{ten_cap} ({cap_tren_ten})"
            data.append({
                "id": cap.id,
                "Ten": ten,
                "CapTren__Ten": cap_tren_ten
            })
        # for cap in cap_list:
        #     ten = cap.Ten + ' ('+ cap.CapTren + ') '
        #     data.append({
        #         "id": cap.id,
        #         "Ten": ten,
        #         "CapTrenTen": cap.CapTren.Ten if cap.CapTren else None
        #     })
        # data = list(cap_list.values("id", "Ten", "CapTren__Ten"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}

    try:
        # Tìm các đối tượng CapNhomDonVi liên quan đến id_nhom
        cap_list = CapDonViModel.CapDonViModel.objects.filter(id_NhomDonVi_id=id_nhom)

        # Chuyển đổi dữ liệu thành dạng có thể trả về
        data = []
        for cap in cap_list:
            data.append({
                "id": cap.id,
                "Ten": cap.Ten,
                "CapTrenTen": cap.CapTren.Ten if cap.CapTren else None
            })

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThongTin(id):
    try:
        # Tìm đối tượng CapDonViModel theo id
        cap_nhom = CapDonViModel.CapDonViModel.objects.get(pk=id)

        # Chuyển đổi dữ liệu thành dạng từ điển
        data = {
            "id": cap_nhom.id,
            "Ten": cap_nhom.Ten,
            "CapTren": cap_nhom.CapTren.Ten if cap_nhom.CapTren else None  # Xử lý trường hợp CapTren có thể là None
        }

        return {"status": "success", "data": data}

    except CapDonViModel.CapDonViModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy đối tượng với id này."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def ThongTinChiTiet(id):
    try:
        # Lấy thông tin nhóm đơn vị dựa trên id
        cap_nhom_don_vi = CapDonViModel.CapDonViModel.objects.get(id=id)
        
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

    except CapDonViModel.CapDonViModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy nhóm đơn vị với id này"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def CapTrenThemCNDV(id_nhom):
    try:
        # Tìm các đối tượng CapNhomDonVi liên quan đến id_nhom
        cap_list = CapDonViModel.CapDonViModel.objects.filter(id_NhomDonVi_id=id_nhom)

        # Chuyển đổi dữ liệu thành dạng có thể trả về
        data = [{"id": "", "Ten": "Không có đơn vị cấp trên"}]  # Thêm dòng mặc định
        for cap in cap_list:
            ten_cap = cap.Ten
            cap_tren_ten = cap.CapTren.Ten if cap.CapTren else ""
            ten = f"{ten_cap} ({cap_tren_ten})"
            data.append({
                "id": cap.id,
                "Ten": ten
            })

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

