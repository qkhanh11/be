from model import NhomQNCNModel,NhomSQModel,NhomVCQPModel

def ThemNhomSQ(TenNhom):
    try:
  
        Nhom = NhomSQModel.NhomSQModel(
            TenNhom=TenNhom
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        Nhom.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def ThemNhomQNCN(TenNhom):
    try:
  
        Nhom = NhomQNCNModel.NhomQNCNModel(
            TenNhom=TenNhom
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        Nhom.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def ThemNhomVC(TenNhom):
    try:
  
        Nhom = NhomVCQPModel.NhomVCQPModel(
            TenNhom=TenNhom
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        Nhom.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Thêm thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaNhomSQ(id,TenNhom):
    try:
  
        Nhom = NhomSQModel.NhomSQModel.objects.get(pk=id)
        Nhom.TenNhom=TenNhom
        

        # Lưu đối tượng vào cơ sở dữ liệu
        Nhom.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Sửa thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaNhomQNCN(id,TenNhom):
    try:
  
        Nhom = NhomQNCNModel.NhomQNCNModel.objects.get(pk=id)
        Nhom.TenNhom=TenNhom
        

        # Lưu đối tượng vào cơ sở dữ liệu
        Nhom.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Sửa thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    


def SuaNhomVC(id,TenNhom):
    try:
  
        Nhom = NhomVCQPModel.NhomVCQPModel.objects.get(pk=id)
        Nhom.TenNhom=TenNhom
        

        # Lưu đối tượng vào cơ sở dữ liệu
        Nhom.save()

        # Trả về thông báo thành công và dữ liệu của đơn vị mới
        return {"status": "success", "data": "Sửa thành công"}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def XoaNhomSQ(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        Nhom = NhomSQModel.NhomSQModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        Nhom.delete()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaNhomQNCN(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        Nhom = NhomQNCNModel.NhomQNCNModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        Nhom.delete()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def XoaNhomVC(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        Nhom = NhomVCQPModel.NhomVCQPModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        Nhom.delete()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}


def NhomSQ():
    try:

        Nhom = NhomSQModel.NhomSQModel.objects.all()


        data = list(Nhom.values("id", "TenNhom"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def NhomQNCN():
    try:

        Nhom = NhomQNCNModel.NhomQNCNModel.objects.all()


        data = list(Nhom.values("id", "TenNhom"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def NhomVC():
    try:

        Nhom = NhomVCQPModel.NhomVCQPModel.objects.all()


        data = list(Nhom.values("id", "TenNhom"))

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}

