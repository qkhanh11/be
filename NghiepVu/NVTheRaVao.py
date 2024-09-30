from model import TheSiQuanModel,TheQNCNModel,TheSiQuanNamModel,TheQNCNNamModel,TheVienChucModel,TheVienChucNamModel, SiQuanModel,QNCNModel,VienChucQPModel,NhomSQModel,NhomQNCNModel


def ThemTheSQ(SoThe, SiQuan):
    try:

        # Kiểm tra xem SiQuan có tồn tại không
        si_quan = SiQuanModel.SiQuanModel.objects.get(id=SiQuan)
        
        # Tạo và lưu bản ghi mới trong TheSiQuanModel
        the_siquan = TheSiQuanModel.TheSiQuanModel(SoThe=SoThe, SiQuan=si_quan)
        the_siquan.save()
        
        return {"status": "success", "message": "Thẻ sĩ quan đã được thêm thành công"}
    
    except SiQuanModel.SiQuanModel.DoesNotExist:
        return {"status": "error", "message": "Sĩ quan với id này không tồn tại"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThemTheQNCN(SoThe, QNCN):
    try:
        # Kiểm tra xem SiQuan có tồn tại không
        qncn = QNCNModel.QNCNModel.objects.get(id=QNCN)
        
        # Tạo và lưu bản ghi mới trong TheSiQuanModel
        the_qncn = TheQNCNModel.TheQNCNModel(SoThe=SoThe, QNCN=qncn)
        the_qncn.save()
        
        return {"status": "success", "message": "Thêm thành công"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThemTheVC(SoThe, VC):
    try:
        # Kiểm tra xem SiQuan có tồn tại không
        vien_chuc = VienChucQPModel.VienChucQPModel.objects.get(id=VC)
        
        # Tạo và lưu bản ghi mới trong TheSiQuanModel
        the_vc = TheVienChucModel.TheVienChucModel(SoThe=SoThe, VienChuc=vien_chuc)
        the_vc.save()
        
        return {"status": "success", "message": "Thẻ sĩ quan đã được thêm thành công"}
    
    except SiQuanModel.SiQuanModel.DoesNotExist:
        return {"status": "error", "message": "Sĩ quan với id này không tồn tại"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def KTTheSQ(siquan_id):
    try:
        # Lấy đối tượng sĩ quan với id cụ thể
        si_quan = SiQuanModel.SiQuanModel.objects.get(id=siquan_id)
        
        # Tìm kiếm thẻ sĩ quan kích hoạt
        the_siquan = TheSiQuanModel.TheSiQuanModel.objects.filter(SiQuan=si_quan, TrangThai=True).first()
        
        # Nếu tìm thấy thẻ, trả về thông tin thẻ
        if the_siquan:
            return {
                "id": the_siquan.id,
                "SoThe": the_siquan.SoThe
            }
        # Nếu không tìm thấy thẻ, trả về False
        else:
            return False
    
    except SiQuanModel.SiQuanModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy sĩ quan với id này."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def KTTheQNCN(qncn_id):
    try:
        qncn = QNCNModel.QNCNModel.objects.get(id=qncn_id)
        
        # Kiểm tra xem sĩ quan đã có thẻ kích hoạt hay chưa
        has_active_card = TheQNCNModel.TheQNCNModel.objects.filter(QNCN=qncn, TrangThai=True).exists()
        
        return has_active_card
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def KTTheVC(vc_id):
    try:
        vien_chuc = VienChucQPModel.VienChucQPModel.objects.get(id=vc_id)
        
        # Kiểm tra xem sĩ quan đã có thẻ kích hoạt hay chưa
        has_active_card = TheVienChucModel.TheVienChucModel.objects.filter(VienChuc=vien_chuc, TrangThai=True).exists()
        
        return has_active_card
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def HuyTheSQ(id):
    try:
        # Kiểm tra xem SiQuan có tồn tại không
        the = TheSiQuanModel.TheSiQuanModel.objects.get(id=id)
        
        the.delete()
        
        return {"status": "success", "message": "Xóa thành công"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def HuyTheQNCN(id):
    try:
        # Kiểm tra xem SiQuan có tồn tại không
        the = TheQNCNModel.TheQNCNModel.objects.get(id=id)
        
        the.delete()
        
        return {"status": "success", "message": "Xóa thành công"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def HuyThevc(id):
    try:
        # Kiểm tra xem SiQuan có tồn tại không
        the = TheVienChucModel.TheVienChucModel.objects.get(id=id)
        
        the.delete()
        
        return {"status": "success", "message": "Xóa thành công"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}


def ThemNamTheQNCN(the_id, nam):
    try:
        # Lấy đối tượng TheSiQuanModel bằng ID
        the= TheQNCNModel.TheQNCNModel.objects.get(id=the_id)
        
        # Tạo hoặc lưu thông tin năm cho thẻ sĩ quan
        # Kiểm tra xem đã có bản ghi với cùng năm chưa
        the_nam, created = TheQNCNNamModel.TheQNCNNamModel.objects.get_or_create(
            The=the,
            Nam=nam
        )
        
        if created:
            return {"status": "success", "message": "Thông tin năm thẻ đã được thêm thành công."}
        else:
            return {"status": "info", "message": "Thông tin năm thẻ sĩ quan đã tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThemNamTheVC(the_id, nam):
    try:
        # Lấy đối tượng TheSiQuanModel bằng ID
        the_siquan = TheVienChucModel.TheVienChucModel.objects.get(id=the_id)
        
        # Tạo hoặc lưu thông tin năm cho thẻ sĩ quan
        # Kiểm tra xem đã có bản ghi với cùng năm chưa
        the_siquan_nam, created = TheVienChucNamModel.TheVienChucNamModel.objects.get_or_create(
            The=the_siquan,
            Nam=nam
        )
        
        if created:
            return {"status": "success", "message": "Thông tin năm thẻ đã được thêm thành công."}
        else:
            return {"status": "info", "message": "Thông tin năm thẻ sĩ quan đã tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThemNamTheSQ(the_id, nam):
    try:
        # Lấy đối tượng TheSiQuanModel bằng ID
        the_siquan = TheSiQuanModel.TheSiQuanModel.objects.get(id=the_id)
        
        # Tạo hoặc lưu thông tin năm cho thẻ sĩ quan
        # Kiểm tra xem đã có bản ghi với cùng năm chưa
        the_siquan_nam, created = TheSiQuanNamModel.TheSiQuanNamModel.objects.get_or_create(
            The=the_siquan,
            Nam=nam
        )
        
        if created:
            return {"status": "success", "message": "Thông tin năm thẻ sĩ quan đã được thêm thành công."}
        else:
            return {"status": "success", "message": "Thông tin năm thẻ sĩ quan đã tồn tại."}

    except Exception as e:
        return {"status": "error", "message": str(e)}



def The_NhomSQ(sothe):
    try:
        # Tìm thẻ sĩ quan với số thẻ đã cho
        the = TheSiQuanModel.TheSiQuanModel.objects.filter(SoThe=sothe,TrangThai=True).first()

        # Kiểm tra xem thẻ có tồn tại không
        if not the:
            return {"status": "error", "message": "Không tìm thấy thẻ với số thẻ này."}
 
        # Lấy thông tin sĩ quan liên kết với thẻ
        si_quan = the.SiQuan

        # Lấy thông tin NhomSQ của sĩ quan
        nhom_sq = NhomSQModel.NhomSQModel.objects.get(pk=si_quan.NhomSQ.id)
        return int(nhom_sq.id)

    except AttributeError:
        return {"status": "error", "message": "Không tìm thấy thông tin nhóm sĩ quan."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def TenSQTuThe(sothe):
    try:
        thesq=TheSiQuanModel.TheSiQuanModel.objects.get(SoThe=sothe,TrangThai=True)
        SQ=thesq.SiQuan
        return {"status": "success", "message": SQ.HoTen}
    except:
        return {"status": "success", "message": ""}


def The_NhomQNCN(sothe):
    try:
        # Tìm thẻ sĩ quan với số thẻ đã cho
        the = TheQNCNModel.TheQNCNModel.objects.filter(SoThe=sothe,TrangThai=True).first()

        # Kiểm tra xem thẻ có tồn tại không
        if not the:
            return {"status": "error", "message": "Không tìm thấy thẻ với số thẻ này."}
 
        # Lấy thông tin sĩ quan liên kết với thẻ
        qncn = the.QNCN

        # Lấy thông tin NhomSQ của sĩ quan
        nhom_sq = NhomQNCNModel.NhomQNCNModel.objects.get(pk=qncn.NhomQNCN.id)
        return int(nhom_sq.id)

    except AttributeError:
        return {"status": "error", "message": "Không tìm thấy thông tin nhóm sĩ quan."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def TenQNCNTuThe(sothe):
    try:
        thesq=TheQNCNModel.TheQNCNModel.objects.get(SoThe=sothe,TrangThai=True)
        QNCN=thesq.QNCN
        return {"status": "success", "message": QNCN.HoTen}
    except:
        return {"status": "success", "message": ""}
