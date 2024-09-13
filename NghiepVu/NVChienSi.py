from model import ChienSiModel, DonViModel, CBHaSiQuanModel
from django.core.exceptions import ObjectDoesNotExist



def LayChienSiTuMa(Ma):
    try:
        chiensi = ChienSiModel.ChienSiModel.objects.get(Ma=Ma)
        return chiensi
    except:
        return None
    

def ThemChienSi(HoTen,Ma,NgaySinh,DonVi,CapBac,NgayNhapNgu,SoCanCuoc,QueQuan,NoiO):
    try:
        # Xác thực mã đơn vị
        try:
            don_vi = DonViModel.DonViModel.objects.get(pk=DonVi)
        except ObjectDoesNotExist:
            return {"status": "error", "message": "Đơn vị không tồn tại."}
        
        MaCS = ChienSiModel.ChienSiModel.objects.filter(Ma=Ma, TinhTrang=True)
        if MaCS.exists():
            return {"status": "error", "message": "Mã chiến sĩ đã tồn tại."}
        # Xác thực cấp bậc
        try:
            cap_bac = CBHaSiQuanModel.CBHaSiQuanModel.objects.get(pk=CapBac)
        except ObjectDoesNotExist:
            return {"status": "error", "message": "Cấp bậc không tồn tại."}
        
        # Tạo đối tượng chiến sĩ
        chien_si = ChienSiModel.ChienSiModel(
            HoTen=HoTen,
            Ma=Ma,
            NgaySinh=NgaySinh,
            DonVi=don_vi,
            CapBac=cap_bac,
            NgayNhapNgu=NgayNhapNgu,
            SoCanCuoc=SoCanCuoc,
            QueQuan=QueQuan,
            NoiO=NoiO
        )
        
        # Lưu đối tượng vào cơ sở dữ liệu
        chien_si.save()
        
        return {"status": "success", "message": "Thêm chiến sĩ thành công."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def SuaChienSi(id,HoTen,Ma,NgaySinh,DonVi,CapBac,NgayNhapNgu,SoCanCuoc,QueQuan,NoiO):
    try:
        # Lấy đối tượng chiến sĩ theo ID
        try:
            chien_si = ChienSiModel.ChienSiModel.objects.get(pk=id)
        except ObjectDoesNotExist:
            return {"status": "error", "message": "Chiến sĩ không tồn tại."}
        
        # Xác thực và cập nhật các trường thông tin
        try:
            don_vi = DonViModel.DonViModel.objects.get(pk=DonVi)
            chien_si.DonVi = don_vi
        except ObjectDoesNotExist:
            return {"status": "error", "message": "Đơn vị không tồn tại."}

        try:
            cap_bac = CBHaSiQuanModel.CBHaSiQuanModel.objects.get(pk=CapBac)
            chien_si.CapBac = cap_bac
        except ObjectDoesNotExist:
            return {"status": "error", "message": "Cấp bậc không tồn tại."}

        chien_si.HoTen = HoTen
        chien_si.Ma = Ma
        chien_si.NgaySinh = NgaySinh
        chien_si.NgayNhapNgu = NgayNhapNgu
        chien_si.SoCanCuoc = SoCanCuoc
        chien_si.QueQuan = QueQuan
        chien_si.NoiO = NoiO
        
        # Lưu đối tượng vào cơ sở dữ liệu
        chien_si.save()
        
        return {"status": "success", "message": "Cập nhật chiến sĩ thành công."}

    except Exception as e:
        return {"status": "error", "message": str(e)}



def XoaChienSi(id):
    try:
        # Lấy đối tượng chiến sĩ theo ID
        try:
            chien_si = ChienSiModel.ChienSiModel.objects.get(pk=id)
        except ObjectDoesNotExist:
            return {"status": "error", "message": "Chiến sĩ không tồn tại."}
        
        # Xóa đối tượng chiến sĩ
        chien_si.TinhTrang=False
        chien_si.save()
        
        return {"status": "success", "message": "Xóa chiến sĩ thành công."}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TatCaChienSi():
    try:
        # Truy vấn tất cả các chiến sĩ
        chien_si_list = ChienSiModel.ChienSiModel.objects.select_related('DonVi', 'CapBac').filter(TinhTrang=True)
        
        # Tạo danh sách dữ liệu để trả về
        data = []
        for chien_si in chien_si_list:
            data.append({
                "id": chien_si.id,
                "HoTen": chien_si.HoTen,
                "Ma": chien_si.Ma,
                "CapBac": chien_si.CapBac.TenCapBac,
                "TenDonVi": chien_si.DonVi.TenDonVi,
                "QueQuan": chien_si.QueQuan
            })

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ChiTietChienSi(id):
    try:
        # Lấy đối tượng chiến sĩ theo ID
        chien_si = ChienSiModel.ChienSiModel.objects.select_related('DonVi', 'CapBac').get(pk=id)
        
        # Tạo dữ liệu chi tiết của chiến sĩ
        data = {
            "id": chien_si.id,
            "HoTen": chien_si.HoTen,
            "Ma": chien_si.Ma,
            "NgaySinh": chien_si.NgaySinh,
            "DonVi": chien_si.DonVi.TenDonVi,
            "CapBac": chien_si.CapBac.TenCapBac,
            "NgayNhapNgu": chien_si.NgayNhapNgu,
            "SoCanCuoc": chien_si.SoCanCuoc,
            "QueQuan": chien_si.QueQuan,
            "NoiO": chien_si.NoiO
        }

        return {"status": "success", "data": data}

    except ObjectDoesNotExist:
        return {"status": "error", "message": "Chiến sĩ không tồn tại."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def LayTenCSTuMa(MaCS):
    try:
        CS = ChienSiModel.ChienSiModel.objects.get(Ma=MaCS,TinhTrang=True)
        return {"status": "success", "HoTen": CS.HoTen}
    # except Exception as e:
    #     return {"status": "error", "message": str(e)}
    except:
        return {"status": "success", "HoTen": ""}