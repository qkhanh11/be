from model import LoaiKhachModel, KhachModel, TheKhachModel,KhachSiQuanModel,KhachQNCNModel,KhachVienChucModel, KhachHocVienModel
from .NVSiQuan import LaySQTuMa
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta


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
    # Lọc các bản ghi có ThoiGianKetThuc là null và sử dụng select_related để lấy thông tin từ các mô hình liên quan
    khach_si_quan_list = KhachSiQuanModel.KhachSiQuanModel.objects.filter(ThoiGianKetThuc__isnull=True).select_related('SiQuan', 'TheKhach', 'Khach')

    # Chuyển QuerySet thành danh sách các dictionary chứa các trường cần thiết
    data = []
    for ksq in khach_si_quan_list:
        data.append({
            'id': ksq.id,
            'SiQuan__HoTen': ksq.SiQuan.HoTen,
            'TheKhach__SoThe': ksq.TheKhach.SoThe,
            'Khach__HoTenKhach': ksq.Khach.HoTenKhach,
            'ThoiGianBatDau': ksq.ThoiGianBatDau.strftime('%H:%M %d-%m-%Y'),  # Định dạng ngày giờ
            'GhiChu': ksq.GhiChu,
        })

    # Trả về JsonResponse
    return {"status": "success", "data": data}


def TraKhachSQ(id):
    try:
        # Lấy bản ghi KhachSiQuanModel dựa trên id
        khach_si_quan = KhachSiQuanModel.KhachSiQuanModel.objects.get(id=id)
        
        # Cập nhật ThoiGianKetThuc với thời gian hiện tại
        khach_si_quan.ThoiGianKetThuc = timezone.now() + timedelta(hours=7)
        khach_si_quan.TraTheKhach = True
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
        khach_si_quan_list = KhachSiQuanModel.KhachSiQuanModel.objects.all().values(
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
    

def danh_sach_the_khach():
    # Lấy tất cả các thẻ khách
    try:
        # Lấy tất cả các thẻ khách
        danh_sach_the = TheKhachModel.TheKhachModel.objects.all().order_by("-TrangThai")

        # Chuyển đổi QuerySet thành danh sách với các trạng thái được cập nhật
        data = []
        for the in danh_sach_the:
            trang_thai = 'Chưa sử dụng' if not the.DangSuDung else  'Đang sử dụng'
            trang_thai_dang_su_dung = 'Đã hủy' if not the.TrangThai else 'Có thể sử dụng'
            
            data.append({
                'id': the.id,
                'SoThe': the.SoThe,
                'TrangThai': trang_thai_dang_su_dung,
                'DangSuDung': trang_thai
            })

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def SuaTheKhach(id,SoThe):
    try:
        KTthekhach = TheKhachModel.TheKhachModel.objects.filter(SoThe=SoThe,TrangThai=True).exists()
        if KTthekhach:
            return {"status": "error", "message": "Số thẻ khách đã tồn tại."}
        thekhach = TheKhachModel.TheKhachModel.objects.get(pk=id)
        thekhach.SoThe=SoThe
        thekhach.save()
        return {"status": "success", "message": "Thành công."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    


def TraTheKhach(id):
    thekhach = TheKhachModel.TheKhachModel.objects.get(pk=id)
    thekhach.DangSuDung=False
    thekhach.save()
    

def ThongKeKhachTrongNgay():
    today = (timezone.now() + timedelta(hours=7)).date()
    start_of_day = timezone.make_aware(timezone.datetime.combine(today, timezone.datetime.min.time()))
    end_of_day = timezone.make_aware(timezone.datetime.combine(today, timezone.datetime.max.time()))
    
    sq = KhachSiQuanModel.KhachSiQuanModel.objects.filter(
        ThoiGianBatDau__gte=start_of_day,
        ThoiGianBatDau__lte=end_of_day
    ).aggregate(total_khach=Count('id'))["total_khach"]


    qncn = KhachQNCNModel.KhachQNCNModel.objects.filter(
        ThoiGianBatDau__gte=start_of_day,
        ThoiGianBatDau__lte=end_of_day
    ).aggregate(total_khach=Count('id'))["total_khach"]


    vc = KhachVienChucModel.KhachVienChucModel.objects.filter(
        ThoiGianBatDau__gte=start_of_day,
        ThoiGianBatDau__lte=end_of_day
    ).aggregate(total_khach=Count('id'))["total_khach"]


    hv = KhachHocVienModel.KhachHocVienModel.objects.filter(
        ThoiGianBatDau__gte=start_of_day,
        ThoiGianBatDau__lte=end_of_day
    ).aggregate(total_khach=Count('id'))["total_khach"]


    tong = sq + qncn + vc + hv

    data ={
        'KhachSQ': sq,
        'KhachQNCN': qncn,
        'KhachVC': vc,
        'KhachHV': hv,
        'Tong': tong
    }
    return {"status": "success", "data": data}


def ThongKeTrongThang():
    now = (timezone.now() + timedelta(hours=7))
    start_of_month = now.replace(day=1)

    # Lấy ngày đầu của tháng tiếp theo, rồi trừ đi một giây để có ngày cuối tháng hiện tại
    if now.month == 12:
        end_of_month = now.replace(year=now.year + 1, month=1, day=1) - timedelta(seconds=1)
    else:
        end_of_month = now.replace(month=now.month + 1, day=1) - timedelta(seconds=1)

    sq = KhachSiQuanModel.KhachSiQuanModel.objects.filter(
        ThoiGianBatDau__gte=start_of_month,
        ThoiGianBatDau__lte=end_of_month
    ).aggregate(total_khach=Count('id'))["total_khach"]

    qncn = KhachQNCNModel.KhachQNCNModel.objects.filter(
        ThoiGianBatDau__gte=start_of_month,
        ThoiGianBatDau__lte=end_of_month
    ).aggregate(total_khach=Count('id'))["total_khach"]

    vc = KhachVienChucModel.KhachVienChucModel.objects.filter(
        ThoiGianBatDau__gte=start_of_month,
        ThoiGianBatDau__lte=end_of_month
    ).aggregate(total_khach=Count('id'))["total_khach"]

    hv = KhachHocVienModel.KhachHocVienModel.objects.filter(
        ThoiGianBatDau__gte=start_of_month,
        ThoiGianBatDau__lte=end_of_month
    ).aggregate(total_khach=Count('id'))["total_khach"]

    tong = sq + qncn + vc + hv

    data ={
        'KhachSQ': sq,
        'KhachQNCN': qncn,
        'KhachVC': vc,
        'KhachHV': hv,
        'Tong': tong
    }
    return {"status": "success", "data": data}



def ThongKeTheoNam(nam):
    current_year  = nam


    thong_ke_theo_thang_sq = KhachSiQuanModel.KhachSiQuanModel.objects.filter(
        ThoiGianBatDau__year=current_year
    ).annotate(
        thang=TruncMonth('ThoiGianBatDau')
    ).values(
        'thang'
    ).annotate(
        total_khach=Count('id')
    ).order_by('thang')


    thong_ke_theo_thang_qncn = KhachQNCNModel.KhachQNCNModel.objects.filter(
        ThoiGianBatDau__year=current_year
    ).annotate(
        thang=TruncMonth('ThoiGianBatDau')
    ).values(
        'thang'
    ).annotate(
        total_khach=Count('id')
    ).order_by('thang')


    thong_ke_theo_thang_vc = KhachVienChucModel.KhachVienChucModel.objects.filter(
        ThoiGianBatDau__year=current_year
    ).annotate(
        thang=TruncMonth('ThoiGianBatDau')
    ).values(
        'thang'
    ).annotate(
        total_khach=Count('id')
    ).order_by('thang')


    thong_ke_theo_thang_hv = KhachHocVienModel.KhachHocVienModel.objects.filter(
        ThoiGianBatDau__year=current_year
    ).annotate(
        thang=TruncMonth('ThoiGianBatDau')
    ).values(
        'thang'
    ).annotate(
        total_khach=Count('id')
    ).order_by('thang')

    # Tạo từ điển với tất cả các tháng từ thang1 đến thang12 có giá trị mặc định là 0
    ket_qua = {f'thang{i}': 0 for i in range(1, 13)}

    # Duyệt qua kết quả truy vấn và cập nhật số lượng khách vào từ điển
    ket_qua = {f'thang{i}': 0 for i in range(1, 13)}

    # Hàm hỗ trợ cập nhật số lượng khách cho từ điển kết quả
    def cap_nhat_ket_qua(thong_ke_theo_thang):
        for item in thong_ke_theo_thang:
            thang_so = item['thang'].month  # Lấy số tháng từ đối tượng 'thang'
            ket_qua[f'thang{thang_so}'] += item['total_khach']  # Cộng dồn số khách

    # Cập nhật kết quả từ các truy vấn
    cap_nhat_ket_qua(thong_ke_theo_thang_sq)
    cap_nhat_ket_qua(thong_ke_theo_thang_qncn)
    cap_nhat_ket_qua(thong_ke_theo_thang_vc)
    cap_nhat_ket_qua(thong_ke_theo_thang_hv)

    return {"status": "success", "data": ket_qua}


def SuaTiepKhachSQ(id,SiQuan,HoTenKhach,SoDinhDanh,Loai,TheKhach,NgayBD, GioBD,NgayKT,GioKT,GhiChu,TraThe):
    try:
        tiepkhach = KhachSiQuanModel.KhachSiQuanModel.objects.get(pk=id)
        if tiepkhach.Khach.SoDinhDanh == SoDinhDanh and tiepkhach.Khach.Loai.id == Loai:
            tiepkhach.Khach.HoTenKhach = HoTenKhach
            tiepkhach.Khach.save()
            khach = tiepkhach.Khach
        else:
            khach = ThemKhach(HoTenKhach, SoDinhDanh, Loai)
        SQ = LaySQTuMa(SiQuan)
        if not SQ:
            return {"status": "error", "message": "Không tồn tại mã quân nhân"}

        # Lấy thông tin thẻ khách
        thekhach = TheKhachModel.TheKhachModel.objects.get(pk=TheKhach)
        tiepkhach.TheKhach.DangSuDung=False
        tiepkhach.TheKhach.save()
        # Cộng thêm 7 giờ vào giờ bắt đầu và giờ kết thúc nếu cần
        # Chuyển đổi NgayBD, GioBD, NgayKT, GioKT thành datetime object
        TGBD = datetime.strptime(f"{NgayBD} {GioBD}", '%Y-%m-%d %H:%M') 
        TGKT = datetime.strptime(f"{NgayKT} {GioKT}", '%Y-%m-%d %H:%M') if NgayKT and GioKT else None

        # Cập nhật thông tin của tiepkhach
        tiepkhach.SiQuan = SQ
        tiepkhach.TheKhach = thekhach
        tiepkhach.Khach = khach
        tiepkhach.ThoiGianBatDau = TGBD
        tiepkhach.ThoiGianKetThuc = TGKT
        tiepkhach.GhiChu = GhiChu
        tiepkhach.TraTheKhach = TraThe
        tiepkhach.save()
        
        # Cập nhật trạng thái thẻ khách
        thekhach.DangSuDung = not TraThe
        thekhach.save()

        return {"status": "success", "data": "Cập nhật thành công"}
    except KhachSiQuanModel.KhachSiQuanModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy bản ghi."}
    except TheKhachModel.TheKhachModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy thẻ khách."}
    except Exception as e:
        # Xử lý lỗi khác nếu có
        return {"status": "error", "message": str(e)}
    

def ThemLSTiepKhachSQ(SiQuan,HoTenKhach,SoDinhDanh,Loai,TheKhach,NgayBD, GioBD,NgayKT,GioKT,GhiChu,TraThe):
    try:
        # Lấy sĩ quan theo mã
        SQ = LaySQTuMa(SiQuan)
        if not SQ:
            return {"status": "error", "message": "Không tồn tại mã quân nhân"}

        # Kiểm tra xem khách đã tồn tại chưa
        khach = ThemKhach(HoTenKhach, SoDinhDanh, Loai)
        
        # Lấy thông tin thẻ khách
        thekhach = TheKhachModel.TheKhachModel.objects.get(pk=TheKhach)

        # Xử lý thời gian bắt đầu và kết thúc
        TGBD = datetime.strptime(f"{NgayBD} {GioBD}", '%Y-%m-%d %H:%M')
        TGKT = datetime.strptime(f"{NgayKT} {GioKT}", '%Y-%m-%d %H:%M') if NgayKT and GioKT else None

        # Tạo bản ghi KhachSiQuanModel mới
        tiepkhach = KhachSiQuanModel.KhachSiQuanModel.objects.create(
            SiQuan=SQ,
            TheKhach=thekhach,
            Khach=khach,
            ThoiGianBatDau=TGBD,
            ThoiGianKetThuc=TGKT,
            GhiChu=GhiChu,
            TraTheKhach=TraThe
        )

        # Cập nhật trạng thái của thẻ khách
        thekhach.DangSuDung = not TraThe
        thekhach.save()

        return {"status": "success", "message": "Thêm lịch sử tiếp khách thành công."}
    
    except TheKhachModel.TheKhachModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy thẻ khách."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TraTheKhachSQ(id):
    try:
        # Lấy bản ghi lịch sử tiếp khách dựa trên id
        tiepkhach = KhachSiQuanModel.KhachSiQuanModel.objects.get(pk=id)

        # Kiểm tra nếu thẻ đã được trả chưa
        if tiepkhach.TraTheKhach:
            return {"status": "error", "message": "Thẻ khách đã được trả trước đó."}

        # Cập nhật trạng thái thẻ khách
        tiepkhach.TraTheKhach = True
        tiepkhach.ThoiGianKetThuc = timezone.now()  # Cập nhật thời gian trả thẻ
        tiepkhach.save()

        # Cập nhật trạng thái của thẻ khách
        thekhach = tiepkhach.TheKhach
        thekhach.DangSuDung = False  # Thẻ khách không còn sử dụng
        thekhach.save()

        return {"status": "success", "message": "Trả thẻ khách thành công."}
    
    except KhachSiQuanModel.KhachSiQuanModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy lịch sử tiếp khách."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def DaTraKhachSQ():
    khach_si_quan_list = KhachSiQuanModel.KhachSiQuanModel.objects.filter(ThoiGianKetThuc__isnull=False).select_related('SiQuan', 'TheKhach', 'Khach').order_by("-ThoiGianKetThuc")

    # Chuyển QuerySet thành danh sách các dictionary chứa các trường cần thiết
    data = []
    for ksq in khach_si_quan_list:
        data.append({
            'id': ksq.id,
            'SiQuan__HoTen': ksq.SiQuan.HoTen,
            'TheKhach__SoThe': ksq.TheKhach.SoThe,
            'Khach__HoTenKhach': ksq.Khach.HoTenKhach,
            'ThoiGianBatDau': ksq.ThoiGianBatDau.strftime('%H:%M %d-%m-%Y'),  # Định dạng ngày giờ
            'ThoiGianKetThuc': ksq.ThoiGianKetThuc.strftime('%H:%M %d-%m-%Y'),
            'GhiChu': ksq.GhiChu,
            'DaTraThe': ksq.TraTheKhach
        })

    # Trả về JsonResponse
    return {"status": "success", "data": data}


def ChiTietTiepKhachSQ(id):
    try:
        # Lấy bản ghi lịch sử tiếp khách dựa trên id
        tiepkhach = KhachSiQuanModel.KhachSiQuanModel.objects.select_related('SiQuan', 'Khach', 'TheKhach').get(pk=id)

        # Tạo dictionary chứa thông tin chi tiết
        data = {
            'id': tiepkhach.id,
            'SiQuan': tiepkhach.SiQuan.MaQuanNhan,
            'HoTenSQ': tiepkhach.SiQuan.HoTen,
            'HoTenKhach': tiepkhach.Khach.HoTenKhach,
            'SoDinhDanh': tiepkhach.Khach.SoDinhDanh,
            'Loai': tiepkhach.Khach.Loai.id,
            'TenLoai': tiepkhach.Khach.Loai.TenLoaiKhach,
            'SoTheKhach': tiepkhach.TheKhach.SoThe,
            'TheKhach': tiepkhach.TheKhach.id,  # Số thẻ khách
            'NgayBD': tiepkhach.ThoiGianBatDau.date(),
            'GioBD': f"{tiepkhach.ThoiGianBatDau.time().hour}:{tiepkhach.ThoiGianBatDau.time().minute}",
            'NgayKT': tiepkhach.ThoiGianKetThuc.date() if tiepkhach.ThoiGianKetThuc else None,
            'GioKT': f"{tiepkhach.ThoiGianKetThuc.time().hour}:{tiepkhach.ThoiGianKetThuc.time().minute}" if tiepkhach.ThoiGianKetThuc else None,
            'GhiChu': tiepkhach.GhiChu,
            'TraTheKhach': tiepkhach.TraTheKhach
        }

        return {"status": "success", "data": data}
    
    except KhachSiQuanModel.KhachSiQuanModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy lịch sử tiếp khách."}
    except Exception as e:
        return {"status": "error", "message": str(e)}