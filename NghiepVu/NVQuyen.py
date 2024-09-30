from model import QuyenModel,ThoiGianQuyenModel,NhomSQModel,QuyenNhomSQModel, NhomQNCNModel,QuyenNhomQNCNModel
from .NVTheRaVao import The_NhomSQ, The_NhomQNCN
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
        print(ngay)
        # Lấy nhóm sĩ quan dựa trên số thẻ
        nhom_sq_response = The_NhomSQ(sothe)
        try:
            if nhom_sq_response['status'] == 'error':
                return nhom_sq_response  # Trả về thông báo lỗi nếu không tìm thấy nhóm sĩ quan
        except: pass

        nhom_sq = NhomSQModel.NhomSQModel.objects.get(pk=nhom_sq_response)  # Lấy đối tượng NhomSQ
        quyen_nhom_sq = QuyenNhomSQModel.QuyenNhomSQModel.objects.filter(NhomSQ=nhom_sq).first()
        if not quyen_nhom_sq:
            return {"status": "error", "message": "Không tìm thấy quyền cho nhóm sĩ quan này."}

        quyen = quyen_nhom_sq.Quyen  # Giả sử QuyenNhomSQModel có một trường ForeignKey hoặc OneToOneField tên là 'Quyen'
        # print(quyen.TenQuyen)
        ngay = datetime.strptime(ngay, "%Y-%m-%d")

# Lấy thứ bằng phương thức strftime
        today = ngay.weekday()
        print(today)
        # today = date.today()
        # Lọc các bản ghi của ngày hôm nay và nhóm sĩ quan cụ thể
    
        cac_ban_ghi_hom_nay = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.filter(
            Quyen=quyen,
            Thu=today
        )
        for i in cac_ban_ghi_hom_nay:
            print(i.id)
        # Tìm thời gian ra sớm nhất và thời gian vào muộn nhất
        tg_ra_va_tg_vao = cac_ban_ghi_hom_nay.values_list('TGRa', 'TGVao')
        print(tg_ra_va_tg_vao)
        return tg_ra_va_tg_vao

    except Exception as e:
        print(str(e))
        return {"status": "error", "message": str(e)}


def ThoiGianTrongNgay_NhomQNCN(sothe):
    try:

        # Lấy nhóm sĩ quan dựa trên số thẻ
        nhom_qncn_response = The_NhomQNCN(sothe)
        try:
            if nhom_qncn_response['status'] == 'error':
                return nhom_qncn_response  # Trả về thông báo lỗi nếu không tìm thấy nhóm sĩ quan
        except: pass

        nhom_qncn = NhomQNCNModel.NhomQNCNModel.objects.get(pk=nhom_qncn_response)  # Lấy đối tượng NhomSQ
        quyen_nhom_qncn = QuyenNhomQNCNModel.QuyenNhomQNCNModel.objects.filter(NhomQNCN=nhom_qncn).first()
        if not quyen_nhom_qncn:
            return {"status": "error", "message": "Không tìm thấy quyền cho nhóm quân nhân chuyên nghiệp này."}

        quyen = quyen_nhom_qncn.Quyen  # Giả sử QuyenNhomSQModel có một trường ForeignKey hoặc OneToOneField tên là 'Quyen'
        print(quyen.TenQuyen)
        today = date.today()
        # Lọc các bản ghi của ngày hôm nay và nhóm sĩ quan cụ thể
    
        cac_ban_ghi_hom_nay = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.filter(
            Quyen=quyen,
            Thu=today.weekday()
        )
        for i in cac_ban_ghi_hom_nay:
            print(i.id)
        # Tìm thời gian ra sớm nhất và thời gian vào muộn nhất
        tg_ra_va_tg_vao = cac_ban_ghi_hom_nay.values_list('TGRa', 'TGVao')
        print(tg_ra_va_tg_vao)
        return tg_ra_va_tg_vao

    except Exception as e:
        return {"status": "error", "message": str(e)}