from model import QuyenModel,ThoiGianQuyenModel,NhomSQModel,QuyenNhomSQModel, NhomQNCNModel,QuyenNhomQNCNModel, QuyenNhomVCModel, NhomVCQPModel
from .NVTheRaVao import The_NhomSQ, The_NhomQNCN, The_NhomVC
from datetime import date
from django.db.models import Min, Max
from datetime import datetime


def ThemQuyen(TenQuyen,GiaiThich):
    try:
        quyen = QuyenModel.QuyenModel.objects.create(
        TenQuyen=TenQuyen,
        GiaiThich=GiaiThich
    )
        quyen.save()
        return {"status": "success", "data": 'Thêm thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaQuyen(id,TenQuyen,GiaiThich):
    try:
        quyen = QuyenModel.QuyenModel.objects.get(pk=id)
        quyen.TenQuyen=TenQuyen
        quyen.GiaiThich=GiaiThich
    
        quyen.save()
        return {"status": "success", "data": 'Sửa thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def XoaQuyen(id):
    try:
        quyen = QuyenModel.QuyenModel.objects.get(pk=id)
        quyen.TinhTrang = False
        quyen.save()
        return {"status": "success", "data": 'Xóa thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def TatCaQuyen():
    try:
        # Lấy tất cả các quyền từ QuyenModel
        quyen_list = QuyenModel.QuyenModel.objects.filter(TinhTrang=True).values("id", "TenQuyen","GiaiThich")

        # Chuyển đổi dữ liệu thành dạng danh sách
        data = list(quyen_list)

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def ThemThoiGianQuyen(quyen_id, thu, tg_ra, tg_vao):
    try:
        # Tìm đối tượng QuyenModel theo id
        quyen = QuyenModel.QuyenModel.objects.get(id=quyen_id)

        # Tạo đối tượng ThoiGianQuyenModel mới
        thoi_gian_quyen = ThoiGianQuyenModel.ThoiGianQuyenModel(
            Quyen=quyen,
            Thu=thu,
            TGRa=tg_ra,
            TGVao=tg_vao
        )
        thoi_gian_quyen.save()
        # Trả về thông tin của đối tượng vừa thêm
        return {
            "status": "success",
            "data": "Thêm thành công"
        }

    except QuyenModel.QuyenModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy quyền với id này."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def XemChiTietQuyen(id):
    try:
        # Tìm đối tượng QuyenModel theo id
        quyen = QuyenModel.QuyenModel.objects.get(id=id)

        # Tạo đối tượng ThoiGianQuyenModel mới
        thoi_gian_quyen = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.filter(Quyen=quyen).order_by('Thu')
        
        # Chuẩn bị dữ liệu để trả về
        data = {
            'TenQuyen': quyen.TenQuyen,
            'GiaiThich': quyen.GiaiThich,
            'ThoiGianQuyen': []
        }
        
        for tgq in thoi_gian_quyen:
            data['ThoiGianQuyen'].append({
                'id': tgq.id,
                'Thu': tgq.get_Thu_display(),
                'TGRa': tgq.TGRa.strftime('%H:%M'),
                'TGVao': tgq.TGVao.strftime('%H:%M'),
                'Thu_':tgq.Thu
            })
        return {
            "status": "success",
            "data": data
        }
    except QuyenModel.QuyenModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy quyền với id này."}
    except Exception as e:
        return {"status": "error", "message": str(e)}



def SuaThoiGianQuyen(id, thu, tg_ra, tg_vao):
    try:
        # Tìm đối tượng QuyenModel theo id
        quyen = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.get(id=id)

        quyen.Thu = thu
        quyen.TGRa = tg_ra
        quyen.TGVao = tg_vao
        # Tạo đối tượng ThoiGianQuyenModel mới
        
        quyen.save()
        # Trả về thông tin của đối tượng vừa thêm
        return {
            "status": "success",
            "data": "Sửa thành công"
        }

    except QuyenModel.QuyenModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy thời gian này của quyền."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def XoaThoiGianQuyen(id):
    try:
        # Tìm đối tượng QuyenModel theo id
        quyen = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.get(id=id)

        # Tạo đối tượng ThoiGianQuyenModel mới
        
        quyen.delete()
        # Trả về thông tin của đối tượng vừa thêm
        return {
            "status": "success",
            "data": "Xóa thành công"
        }

    except QuyenModel.QuyenModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy thời gian này của quyền."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def ChiTietThoiGianQuyen(id):
    try:
        # Lấy bản ghi chi tiết theo id
        chitiet = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.get(id=id)

        # Tạo dictionary chứa thông tin chi tiết
        data = {
            'id': chitiet.id,
            'Quyen': chitiet.Quyen.TenQuyen,  # Giả sử có trường 'ten_quyen' trong QuyenModel
            'TenThu': dict(ThoiGianQuyenModel.ThoiGianQuyenModel.NGAY_CHOICES).get(chitiet.Thu),
            'Thu': chitiet.Thu,  # Lấy tên thứ từ choices
            'TGRa': chitiet.TGRa.strftime('%H:%M'),  # Định dạng thời gian ra
            'TGVao': chitiet.TGVao.strftime('%H:%M'),  # Định dạng thời gian vào
        }

        return {"status": "success", "data": data}
    
    except ThoiGianQuyenModel.ThoiGianQuyenModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy thời gian quyền."}
    except Exception as e:
        return {"status": "error", "message": str(e)}




def ThoiGianTrongNgay_NhomSQ(ngay,sothe):
    try:
        # Lấy nhóm sĩ quan dựa trên số thẻ
        nhom_sq_response = The_NhomSQ(sothe)
        try:
            if nhom_sq_response['status'] == 'error':
                return nhom_sq_response  # Trả về thông báo lỗi nếu không tìm thấy nhóm sĩ quan
        except: pass

        nhom_sq = NhomSQModel.NhomSQModel.objects.get(pk=nhom_sq_response)  # Lấy đối tượng NhomSQ
        quyen_nhom_qncn_list = QuyenNhomSQModel.QuyenNhomSQModel.objects.filter(NhomSQ=nhom_sq)
        if not quyen_nhom_qncn_list.exists():
            return {"status": "error", "message": "Không tìm thấy quyền cho nhóm sĩ quan này."}

        ngay = datetime.strptime(ngay, "%Y-%m-%d")

        # Lấy thứ bằng phương thức strftime
        today = ngay.weekday()

        tg_ra_va_tg_vao = []
        # Duyệt qua tất cả các quyền của nhóm quân nhân chuyên nghiệp
        for quyen_nhom_qncn in quyen_nhom_qncn_list:
            quyen = quyen_nhom_qncn.Quyen
            # Lọc các bản ghi của ngày hôm nay và quyền cụ thể
            cac_ban_ghi_hom_nay = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.filter(
                Quyen=quyen,
                Thu=today
            )
            # Thêm thời gian ra và vào của các bản ghi vào danh sách
            tg_ra_va_tg_vao.extend(cac_ban_ghi_hom_nay.values_list('TGRa', 'TGVao'))

        return tg_ra_va_tg_vao

    except Exception as e:
        print(str(e))
        return {"status": "error", "message": str(e)}


def ThoiGianTrongNgay_NhomQNCN(ngay, sothe):
    try:

        # Lấy nhóm sĩ quan dựa trên số thẻ
        nhom_qncn_response = The_NhomQNCN(sothe)
        try:
            if nhom_qncn_response['status'] == 'error':
                return nhom_qncn_response  # Trả về thông báo lỗi nếu không tìm thấy nhóm sĩ quan
        except: pass

        nhom_qncn = NhomQNCNModel.NhomQNCNModel.objects.get(pk=nhom_qncn_response)  # Lấy đối tượng NhomSQ
        quyen_nhom_qncn_list = QuyenNhomQNCNModel.QuyenNhomQNCNModel.objects.filter(NhomQNCN=nhom_qncn)
        if not quyen_nhom_qncn_list.exists():
            return {"status": "error", "message": "Không tìm thấy quyền cho nhóm quân nhân chuyên nghiệp này."}

        ngay = datetime.strptime(ngay, "%Y-%m-%d")

        # Lấy thứ bằng phương thức strftime
        today = ngay.weekday()

        tg_ra_va_tg_vao = []
        # Duyệt qua tất cả các quyền của nhóm quân nhân chuyên nghiệp
        for quyen_nhom_qncn in quyen_nhom_qncn_list:
            quyen = quyen_nhom_qncn.Quyen
            # Lọc các bản ghi của ngày hôm nay và quyền cụ thể
            cac_ban_ghi_hom_nay = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.filter(
                Quyen=quyen,
                Thu=today
            )
            # Thêm thời gian ra và vào của các bản ghi vào danh sách
            tg_ra_va_tg_vao.extend(cac_ban_ghi_hom_nay.values_list('TGRa', 'TGVao'))

        return tg_ra_va_tg_vao

    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def ThoiGianTrongNgay_NhomVC(ngay, sothe):
    try:
        # Lấy nhóm sĩ quan dựa trên số thẻ
        nhom_qncn_response = The_NhomVC(sothe)
        try:
            if nhom_qncn_response['status'] == 'error':
                return nhom_qncn_response  # Trả về thông báo lỗi nếu không tìm thấy nhóm sĩ quan
        except:
            pass

        nhom_qncn = NhomVCQPModel.NhomVCQPModel.objects.get(pk=nhom_qncn_response)
        
        # Lấy tất cả các quyền liên quan đến nhóm quân nhân chuyên nghiệp
        quyen_nhom_qncn_list = QuyenNhomVCModel.QuyenNhomVCModel.objects.filter(NhomVC=nhom_qncn)

        if not quyen_nhom_qncn_list.exists():
            return {"status": "error", "message": "Không tìm thấy quyền cho nhóm viên chức này."}

        ngay = datetime.strptime(ngay, "%Y-%m-%d")

        # Lấy thứ bằng phương thức strftime
        today = ngay.weekday()

        tg_ra_va_tg_vao = []
        # Duyệt qua tất cả các quyền của nhóm quân nhân chuyên nghiệp
        for quyen_nhom_qncn in quyen_nhom_qncn_list:
            quyen = quyen_nhom_qncn.Quyen
            # Lọc các bản ghi của ngày hôm nay và quyền cụ thể
            cac_ban_ghi_hom_nay = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.filter(
                Quyen=quyen,
                Thu=today
            )
            # Thêm thời gian ra và vào của các bản ghi vào danh sách
            tg_ra_va_tg_vao.extend(cac_ban_ghi_hom_nay.values_list('TGRa', 'TGVao'))

        return tg_ra_va_tg_vao

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def QuyenNhomSQ(id):
    try:
        # Lấy danh sách các quyền của NhomSQ dựa trên id
        nhom_sq = NhomSQModel.NhomSQModel.objects.get( id=id)
        quyen_nhom_sq_queryset = QuyenNhomSQModel.QuyenNhomSQModel.objects.filter(NhomSQ=nhom_sq)

        # Tạo danh sách kết quả
        quyen_list = []
        for quyen_nhom_sq in quyen_nhom_sq_queryset:
            quyen_list.append({
                "id": quyen_nhom_sq.id,
                "id_quyen":quyen_nhom_sq.Quyen.id,
                "TenQuyen": quyen_nhom_sq.Quyen.TenQuyen,
                "GiaiThich": quyen_nhom_sq.Quyen.GiaiThich,
                "id_nhomsq":quyen_nhom_sq.NhomSQ.id
            })

        # Trả về kết quả
        return {
            "status": "success",
            "data": quyen_list
        }
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def ThemQuyenNhomSQ(id_nhomsq,id_quyen):
    try:
        # Lấy đối tượng NhomSQ và Quyen dựa trên id
        nhom_sq = NhomSQModel.NhomSQModel.objects.get(pk=id_nhomsq)
        quyen = QuyenModel.QuyenModel.objects.get(pk=id_quyen)

        # Kiểm tra xem quyền đã được thêm vào nhóm sĩ quan chưa
        if QuyenNhomSQModel.QuyenNhomSQModel.objects.filter(NhomSQ=nhom_sq, Quyen=quyen).exists():
            return {
                "status": "error",
                "message": "Quyền này đã tồn tại trong nhóm sĩ quan"
            }

        # Tạo đối tượng QuyenNhomSQ mới
        quyen_nhom_sq = QuyenNhomSQModel.QuyenNhomSQModel(NhomSQ=nhom_sq, Quyen=quyen)
        quyen_nhom_sq.save()

        return {
            "status": "success",
            "message": "Đã thêm quyền cho nhóm sĩ quan thành công"
        }
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaQuyenNhomSQ(id,id_quyen):
    try:
        # Lấy đối tượng NhomSQ và Quyen dựa trên id
        quyen_nhom = QuyenNhomSQModel.QuyenNhomSQModel.objects.get(pk=id)
        quyen = QuyenModel.QuyenModel.objects.get(pk=id_quyen)
        # Kiểm tra xem quyền đã được thêm vào nhóm sĩ quan chưa
        if QuyenNhomSQModel.QuyenNhomSQModel.objects.filter(NhomSQ=quyen_nhom.NhomSQ, Quyen=quyen).exists():
            return {
                "status": "error",
                "message": "Quyền này đã tồn tại trong nhóm sĩ quan."
            }

        # Cập nhật quyền cho nhóm sĩ quan
        quyen_nhom.Quyen = quyen
        quyen_nhom.save()

        return {
            "status": "success",
            "message": "Đã cập nhật quyền cho nhóm sĩ quan thành công"
        }
    except Exception as e:
        # Xử lý các lỗi khác
        return {"status": "error", "message": str(e)}
    

def XoaQuyenNhomSQ(id):
    try:
        # Lấy đối tượng NhomSQ và Quyen dựa trên id
        quyen_nhom = QuyenNhomSQModel.QuyenNhomSQModel.objects.get(pk=id)

        
        quyen_nhom.delete()

        return {
            "status": "success",
            "message": "Xóa quyền cho nhóm sĩ quan thành công"
        }
    except Exception as e:
        # Xử lý các lỗi khác
        print(str(e))
        return {"status": "error", "message": str(e)}
    


##### quyền nhóm qncn
def QuyenNhomQNCN(id):
    try:
        # Lấy danh sách các quyền của NhomSQ dựa trên id
        nhom_sq = NhomQNCNModel.NhomQNCNModel.objects.get( id=id)
        quyen_nhom_sq_queryset = QuyenNhomQNCNModel.QuyenNhomQNCNModel.objects.filter(NhomQNCN=nhom_sq)

        # Tạo danh sách kết quả
        quyen_list = []
        for quyen_nhom_sq in quyen_nhom_sq_queryset:
            quyen_list.append({
                "id": quyen_nhom_sq.id,
                "id_quyen":quyen_nhom_sq.Quyen.id,
                "TenQuyen": quyen_nhom_sq.Quyen.TenQuyen,
                "GiaiThich": quyen_nhom_sq.Quyen.GiaiThich,
                "id_nhomQNCN":quyen_nhom_sq.NhomQNCN.id
            })

        # Trả về kết quả
        return {
            "status": "success",
            "data": quyen_list
        }
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def ThemQuyenNhomQNCN(id_nhomQNCN,id_quyen):
    try:
        # Lấy đối tượng NhomSQ và Quyen dựa trên id
        nhom_sq = NhomQNCNModel.NhomQNCNModel.objects.get(pk=id_nhomQNCN)
        quyen = QuyenModel.QuyenModel.objects.get(pk=id_quyen)

        # Kiểm tra xem quyền đã được thêm vào nhóm sĩ quan chưa
        if QuyenNhomQNCNModel.QuyenNhomQNCNModel.objects.filter(NhomQNCN=nhom_sq, Quyen=quyen).exists():
            return {
                "status": "error",
                "message": "Quyền này đã tồn tại trong nhóm QNCN"
            }

        # Tạo đối tượng QuyenNhomSQ mới
        quyen_nhom_sq = QuyenNhomSQModel.QuyenNhomSQModel(NhomQNCN=nhom_sq, Quyen=quyen)
        quyen_nhom_sq.save()

        return {
            "status": "success",
            "message": "Đã thêm quyền cho nhóm QNCN thành công"
        }
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaQuyenNhomQNCN(id,id_quyen):
    try:
        # Lấy đối tượng NhomSQ và Quyen dựa trên id
        quyen_nhom = QuyenNhomQNCNModel.QuyenNhomQNCNModel.objects.get(pk=id)
        quyen = QuyenModel.QuyenModel.objects.get(pk=id_quyen)
        # Kiểm tra xem quyền đã được thêm vào nhóm sĩ quan chưa
        if QuyenNhomSQModel.QuyenNhomSQModel.objects.filter(NhomSQ=quyen_nhom.NhomQNCN, Quyen=quyen).exists():
            return {
                "status": "error",
                "message": "Quyền này đã tồn tại trong nhóm QNCN."
            }

        # Cập nhật quyền cho nhóm sĩ quan
        quyen_nhom.Quyen = quyen
        quyen_nhom.save()

        return {
            "status": "success",
            "message": "Đã cập nhật quyền cho nhóm QNCN thành công"
        }
    except Exception as e:
        # Xử lý các lỗi khác
        print(str(e))
        return {"status": "error", "message": str(e)}
    

def XoaQuyenNhomQNCN(id):
    try:
        # Lấy đối tượng NhomSQ và Quyen dựa trên id
        quyen_nhom = QuyenNhomQNCNModel.QuyenNhomQNCNModel.objects.get(pk=id)

        
        quyen_nhom.delete()

        return {
            "status": "success",
            "message": "Xóa quyền cho nhóm QNCN thành công"
        }
    except Exception as e:
        # Xử lý các lỗi khác
        print(str(e))
        return {"status": "error", "message": str(e)}



###Quyền nhóm vc


def QuyenNhomVC(id):
    try:
        # Lấy danh sách các quyền của NhomSQ dựa trên id
        nhom_sq = NhomVCQPModel.NhomVCQPModel.objects.get( id=id)
        quyen_nhom_sq_queryset = QuyenNhomVCModel.QuyenNhomVCModel.objects.filter(NhomVC=nhom_sq)

        # Tạo danh sách kết quả
        quyen_list = []
        for quyen_nhom_sq in quyen_nhom_sq_queryset:
            print()
            quyen_list.append({
                "id": quyen_nhom_sq.id,
                "id_quyen":quyen_nhom_sq.Quyen.id,
                "TenQuyen": quyen_nhom_sq.Quyen.TenQuyen,
                "GiaiThich": quyen_nhom_sq.Quyen.GiaiThich,
                "id_nhomVC":quyen_nhom_sq.NhomVC.id
            })

        # Trả về kết quả
        return {
            "status": "success",
            "data": quyen_list
        }
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def ThemQuyenNhomVC(id_nhomVC,id_quyen):
    try:
        # Lấy đối tượng NhomSQ và Quyen dựa trên id
        nhom_sq = NhomVCQPModel.NhomVCQPModel.objects.get(pk=id_nhomVC)
        quyen = QuyenModel.QuyenModel.objects.get(pk=id_quyen)

        # Kiểm tra xem quyền đã được thêm vào nhóm sĩ quan chưa
        if QuyenNhomVCModel.QuyenNhomVCModel.objects.filter(NhomVC=nhom_sq, Quyen=quyen).exists():
            return {
                "status": "error",
                "message": "Quyền này đã tồn tại trong nhóm viên chức"
            }

        # Tạo đối tượng QuyenNhomSQ mới
        quyen_nhom_sq = QuyenNhomVCModel.QuyenNhomVCModel(NhomVC=nhom_sq, Quyen=quyen)
        quyen_nhom_sq.save()

        return {
            "status": "success",
            "message": "Đã thêm quyền cho nhóm viên chức thành công"
        }
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaQuyenNhomVC(id,id_quyen):
    print(id_quyen)
    try:
        # Lấy đối tượng NhomSQ và Quyen dựa trên id
        quyen_nhom = QuyenNhomVCModel.QuyenNhomVCModel.objects.get(pk=id)
        quyen = QuyenModel.QuyenModel.objects.get(pk=id_quyen)
        print(id_quyen)
        # Kiểm tra xem quyền đã được thêm vào nhóm sĩ quan chưa
        if QuyenNhomVCModel.QuyenNhomVCModel.objects.filter(NhomSQ=quyen_nhom.NhomVC, Quyen=quyen).exists():
            return {
                "status": "error",
                "message": "Quyền này đã tồn tại trong nhóm viên chức."
            }

        # Cập nhật quyền cho nhóm sĩ quan
        quyen_nhom.Quyen = quyen
        quyen_nhom.save()

        return {
            "status": "success",
            "message": "Đã cập nhật quyền cho nhóm viên chức thành công"
        }
    except Exception as e:
        # Xử lý các lỗi khác
        print(str(e))
        return {"status": "error", "message": str(e)}
    

def XoaQuyenNhomVC(id):
    try:
        # Lấy đối tượng NhomSQ và Quyen dựa trên id
        quyen_nhom = QuyenNhomVCModel.QuyenNhomVCModel.objects.get(pk=id)

        
        quyen_nhom.delete()

        return {
            "status": "success",
            "message": "Xóa quyền cho nhóm viên chức thành công"
        }
    except Exception as e:
        # Xử lý các lỗi khác
        print(str(e))
        return {"status": "error", "message": str(e)}