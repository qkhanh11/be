from model import LoaiKhachModel, KhachModel, TheKhachModel,KhachSiQuanModel
from .NVSiQuan import LaySQTuMa
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator


def kiem_tra_the_co_hieu_luc(sothe):
    return TheKhachModel.TheKhachModel.objects.filter(SoThe=sothe, TrangThai=True).exists()


def ThemTheKhach(sothe):
    try:
        kiemtra = kiem_tra_the_co_hieu_luc(sothe)
        if kiemtra:
            return {"status": "error", "message": "Đã tồn tại thẻ này"}
        the = TheKhachModel.TheKhachModel.objects.create(
            SoThe = sothe
        )
        return {"status": "success", "data": 'Thêm thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def HuyThe(id):
    try:
        the = TheKhachModel.TheKhachModel.objects.get(pk = id)
        the.TrangThai = False
        the.save()
        return {"status": "success", "data": 'Hủy thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}


def lay_the_khach_hieu_luc():
    the_khach_list = TheKhachModel.TheKhachModel.objects.filter(TrangThai=True, DangSuDung=False).values('id', 'SoThe')
    data = list(the_khach_list)  # Chuyển QuerySet thành danh sách các dictionary chứa id và SoThe

    return {"status": "success", "data": data}
    


def ThemLoaiKhach(TenLoaiKhach):
    try:
        loai = LoaiKhachModel.LoaiKhachModel.objects.create(
        TenLoaiKhach=TenLoaiKhach
    )

        return {"status": "success", "data": [{
            "id": loai.id,
            "TenLoaiKhach": loai.TenLoaiKhach
        }]}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaLoaiKhach(id,TenLoaiKhach):
    try:
        loai = LoaiKhachModel.LoaiKhachModel.objects.get(pk=id)
        loai.TenLoaiKhach=TenLoaiKhach
    
        loai.save()
        return {"status": "success", "data": 'Sửa thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    


def XoaLoaiKhach(id):
    try:
        loai = LoaiKhachModel.LoaiKhachModel.objects.get(pk=id)
        loai.TrangThai=False
        loai.save()
        return {"status": "success", "data": 'Xóa thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def ThemKhach(HoTenKhach,SoDinhDanh,Loai):
    try:
        loai = LoaiKhachModel.LoaiKhachModel.objects.get(pk=Loai)
        khach,created = KhachModel.KhachModel.objects.get_or_create(
            HoTenKhach=HoTenKhach,
            SoDinhDanh=SoDinhDanh,
            Loai = loai
        )
        return khach
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
    

def TiepKhachSQ(SiQuan,HoTenKhach,SoDinhDanh,Loai,TheKhach,GhiChu):
    try:
        khach = ThemKhach(HoTenKhach, SoDinhDanh, Loai)
        SQ = LaySQTuMa(SiQuan)
        if not SQ:
            return {"status": "error", "message": "Không tồn tại mã quân nhân"}
        thekhach = TheKhachModel.TheKhachModel.objects.get(pk=TheKhach)

        # Cộng thêm 7 giờ
        thoigian = timezone.now() + timedelta(hours=7)
        tiepkhach = KhachSiQuanModel.KhachSiQuanModel.objects.create(
            SiQuan=SQ,
            TheKhach=thekhach,
            Khach=khach,
            ThoiGianBatDau=thoigian,
            GhiChu=GhiChu
        )
        thekhach.DangSuDung = True
        thekhach.save()
        return {"status": "success", "data": 'Thêm thành công'}
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
    

def DangTiepKhachSQ():
    # Lọc các bản ghi có ThoiGianKetThuc là null và sử dụng select_related để lấy thông tin từ các mô hình liên quan
    khach_si_quan_list = KhachSiQuanModel.KhachSiQuanModel.objects.filter(ThoiGianKetThuc__isnull=True).select_related('SiQuan', 'TheKhach', 'Khach')

    # Chuyển QuerySet thành danh sách các dictionary chứa các trường cần thiết
    data = list(khach_si_quan_list.values(
        'id',
        'SiQuan__HoTen',  # Tên sĩ quan
        'TheKhach__SoThe',  # Số thẻ khách
        'Khach__HoTenKhach',  # Tên khách
        'ThoiGianBatDau',
        'GhiChu'
    ))

    # Trả về JsonResponse
    return {"status": "success", "data": data}


def TraKhachSQ(id):
    try:
        # Lấy bản ghi KhachSiQuanModel dựa trên id
        khach_si_quan = KhachSiQuanModel.KhachSiQuanModel.objects.get(id=id)
        
        # Cập nhật ThoiGianKetThuc với thời gian hiện tại
        khach_si_quan.ThoiGianKetThuc = timezone.now() + timedelta(hours=7)
        khach_si_quan.save()
        the_khach = khach_si_quan.TheKhach
        the_khach.DangSuDung = False
        the_khach.save()
        # Trả về phản hồi JSON xác nhận thành công
        return {"status": "success", "message": "Trả khách thành công"}
    
    except KhachSiQuanModel.KhachSiQuanModel.DoesNotExist:
        # Nếu không tìm thấy bản ghi với id cho trước
        return {"status": "error", "message": "Khách không tồn tại"}
    

def LayLoaiKhach():
    loaikhach = LoaiKhachModel.LoaiKhachModel.objects.filter(TrangThai=True).values('id', 'TenLoaiKhach')
    data = list(loaikhach)  # Chuyển QuerySet thành danh sách các dictionary chứa id và SoThe

    return {"status": "success", "data": data}


def DanhSachTiepKhachSiQuan():
    try:
        khach_si_quan_list = KhachSiQuanModel.KhachSiQuanModel.objects.values(
            'id',
            'SiQuan__id',  # ID của sĩ quan
            'SiQuan__HoTen',  # Tên của sĩ quan
            'TheKhach__SoThe',  # Số thẻ khách
            'Khach__id',  # ID của khách
            'Khach__HoTenKhach',  # Tên của khách
            'ThoiGianBatDau',  # Thời gian bắt đầu tiếp khách
            'ThoiGianKetThuc',  # Thời gian kết thúc tiếp khách
            'GhiChu'  # Ghi chú
        )
        
        # Chuyển đổi kết quả thành danh sách các dictionary
        data = list(khach_si_quan_list)

        # Trả về JsonResponse với kết quả
        return {"status": "success", "data": data}

    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
    

def danh_sach_the_khach(page=1):
    # Lấy tất cả các thẻ khách
    danh_sach_the = TheKhachModel.TheKhachModel.objects.all()
    
    # Phân trang
    paginator = Paginator(danh_sach_the, 50)  # Số lượng thẻ trên mỗi trang  # Số trang hiện tại, mặc định là 1
    page_obj = paginator.get_page(page)
    
    # Chuẩn bị dữ liệu để trả về dưới dạng JSON
    data = {
        'the_khach': list(page_obj.object_list.values()),
        'page_number': page_obj.number,
        'num_pages': paginator.num_pages,
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous(),
    }
    
    return {"status": "success", "data": data}