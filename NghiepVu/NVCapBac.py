from model import CapBacModel,CBHaSiQuanModel


def Them(TenCapBac):
    try:

        cap_bac = CapBacModel.CapBacModel(
            TenCapBac=TenCapBac
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        cap_bac.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def Xoa(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        CapBac = CapBacModel.CapBacModel.objects.get(pk=id)
        CapBac.TinhTrang = False
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CapBac.save()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}


def Sua(id,TenCapBac):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        CapBac = CapBacModel.CapBacModel.objects.get(pk=id)
        CapBac.TenCapBac = TenCapBac
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CapBac.save()

        return {"status": "success", "message": "Sửa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def CapBac():
    try:

        CapBac = CapBacModel.CapBacModel.objects.filter(TinhTrang=True)


        data = list(CapBac.values("id", "TenCapBac"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThemCBHSQ(TenCapBac):
    try:

        cap_bac = CBHaSiQuanModel.CBHaSiQuanModel(
            TenCapBac=TenCapBac
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        cap_bac.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def XoaCBHSQ(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        CapBac = CBHaSiQuanModel.CBHaSiQuanModel.objects.get(pk=id)
        CapBac.TinhTrang=False
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CapBac.save()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}


def SuaCBHSQ(id,TenCapBac):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        CapBac = CBHaSiQuanModel.CBHaSiQuanModel.objects.get(pk=id)
        CapBac.TenCapBac = TenCapBac
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        CapBac.save()

        return {"status": "success", "message": "Sửa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def CapBacHSQ():
    try:

        CapBac = CBHaSiQuanModel.CBHaSiQuanModel.objects.filter(TinhTrang=True)


        data = list(CapBac.values("id", "TenCapBac"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}