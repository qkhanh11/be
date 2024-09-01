from model import QuyenModel,ThoiGianQuyenModel,NhomSQModel
from .NVTheRaVao import The_NhomSQ
from datetime import date
from django.db.models import Min, Max


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
    

def ThemQuyen(id):
    try:
        quyen = QuyenModel.QuyenModel.objects.get(pk=id)
        quyen.delete()
        return {"status": "success", "data": 'Xóa thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def TatCaQuyen():
    try:
        # Lấy tất cả các quyền từ QuyenModel
        quyen_list = QuyenModel.QuyenModel.objects.all().values("id", "TenQuyen")

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
    
def ThoiGianTrongNgay_NhomSQ(sothe):
    try:
        # Lấy nhóm sĩ quan dựa trên số thẻ
        nhom_sq_response = The_NhomSQ(sothe)
        
        if nhom_sq_response['status'] == 'error':
            return nhom_sq_response  # Trả về thông báo lỗi nếu không tìm thấy nhóm sĩ quan

        nhom_sq = nhom_sq_response  # Lấy đối tượng NhomSQ
        
        today = date.today()

        # Lọc các bản ghi của ngày hôm nay và nhóm sĩ quan cụ thể
        cac_ban_ghi_hom_nay = ThoiGianQuyenModel.ThoiGianQuyenModel.objects.filter(
            Quyen__nhomsqmodel__NhomSQ=nhom_sq,
            Thu=today.weekday()
        )

        # Tìm thời gian ra sớm nhất và thời gian vào muộn nhất
        tg_ra_va_tg_vao = cac_ban_ghi_hom_nay.values_list('TGRa', 'TGVao')

        return tg_ra_va_tg_vao

    except Exception as e:
        return {"status": "error", "message": str(e)}
