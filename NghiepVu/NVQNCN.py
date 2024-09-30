from model import SiQuanModel, DonViModel, CVSiQuanModel, CapBacModel, NhomSQModel,SQ_DVModel,SQ_CVModel, KhachSiQuanModel, LSRaVaoSQModel, QNCNModel, CVQNCNModel, NhomQNCNModel, QNCN_CVModel, QNCN_DVModel, KhachQNCNModel, LSRaVaoQNCNModel
from django.db import transaction
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from be.settings import SoDoiTuongMoiTrang
from datetime import datetime, timedelta



def them_qncn_dv(id_QNCN, id_DonVi):
    try:
        # Lấy ngày hiện tại
        today = timezone.now().date()

        # Bắt đầu transaction để đảm bảo tính nhất quán dữ liệu
        with transaction.atomic():
            # Tìm bản ghi có SQ = id_SQ và DenNgay là null
            existing_record = QNCN_DVModel.QNCN_DVModel.objects.filter(QNCN_id=id_QNCN, DenNgay__isnull=True).first()
            
            # Nếu đã tồn tại bản ghi, cập nhật DenNgay là hôm nay
            if existing_record:
                existing_record.DenNgay = today
                existing_record.save()

            # Thêm bản ghi mới với SQ = id_SQ, DonVi = id_DonVi và TuNgay là hôm nay
            new_record = QNCN_DVModel.QNCN_DVModel(QNCN_id=id_QNCN, DV_id=id_DonVi, TuNgay=today)
            new_record.save()

            return new_record
    except Exception as e:
        # Xử lý lỗi nếu có
        print(f"Lỗi xảy ra: {e}")
        return None


def them_qncn_cv(id_QNCN, id_CV):
    try:
        # Lấy ngày hiện tại
        today = timezone.now().date()

        # Bắt đầu transaction để đảm bảo tính nhất quán dữ liệu
        with transaction.atomic():
            # Tìm bản ghi có SQ = id_SQ và DenNgay là null
            existing_record = QNCN_CVModel.QNCN_CVModel.objects.filter(QNCN_id=id_QNCN, DenNgay__isnull=True).first()
            
            # Nếu đã tồn tại bản ghi, cập nhật DenNgay là hôm nay
            if existing_record:
                existing_record.DenNgay = today
                existing_record.save()

            # Thêm bản ghi mới với SQ = id_SQ, CV = id_CV và TuNgay là hôm nay
            new_record = QNCN_CVModel.QNCN_CVModel(QNCN_id=id_QNCN, CV_id=id_CV, TuNgay=today)
            new_record.save()

            return new_record
    except Exception as e:
        # Xử lý lỗi nếu có
        print(f"Lỗi xảy ra: {e}")
        return None


def ThemQNCN(HoTen, NgaySinh, MaQuanNhan, DonVi_id, ChucVu_id, CapBac_id, NhomSQ_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO):
    try:
        # Lấy các đối tượng liên quan dựa trên ID
        DonVi = DonViModel.DonViModel.objects.get(pk=DonVi_id)
        ChucVu = CVQNCNModel.CVQNCNModel.objects.get(pk=ChucVu_id)
        CapBac = CapBacModel.CapBacModel.objects.get(pk=CapBac_id)
        NhomQNCN = NhomQNCNModel.NhomQNCNModel.objects.get(pk=NhomSQ_id)
        if SiQuanModel.SiQuanModel.objects.filter(MaQuanNhan=MaQuanNhan).exists():
            return {"status": "error", "message": "Mã quân nhân đã tồn tại"}


        # Tạo đối tượng SiQuanModel mới
        QNCN = QNCNModel.QNCNModel(
            HoTen=HoTen,
            NgaySinh=NgaySinh,
            MaQuanNhan=MaQuanNhan,
            DonVi=DonVi,
            ChucVu=ChucVu,
            CapBac=CapBac,
            NhomQNCN=NhomQNCN,
            NgayNhapNgu=NgayNhapNgu,
            SoCanCuoc=SoCanCuoc,
            QueQuan=QueQuan,
            NoiO=NoiO
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        QNCN.save()

        them_qncn_dv(QNCN.id, DonVi.id)

        # Gọi hàm để thêm bản ghi vào SQ_CVModel
        them_qncn_cv(QNCN.id, ChucVu.id)
        # Trả về thông báo thành công và dữ liệu của sĩ quan mới
        return {"status": "success", "data": 'Thêm thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        print(str(e))
        return {"status": "error", "message": str(e)}
    

def SuaQNCN(id, HoTen, NgaySinh, MaQuanNhan, DonVi_id, ChucVu_id, CapBac_id, NhomSQ_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO):
    try:
        # Lấy các đối tượng liên quan dựa trên ID
        DonVi = DonViModel.DonViModel.objects.get(pk=DonVi_id)
        ChucVu = CVQNCNModel.CVQNCNModel.objects.get(pk=ChucVu_id)
        CapBac = CapBacModel.CapBacModel.objects.get(pk=CapBac_id)
        NhomQNCN = NhomQNCNModel.NhomQNCNModel.objects.get(pk=NhomSQ_id)

        if QNCNModel.QNCNModel.objects.exclude(pk=id).filter(MaQuanNhan=MaQuanNhan).exists():
            return {"status": "error", "message": "Mã quân nhân đã tồn tại"}
        # Lấy đối tượng SiQuanModel hiện tại
        QNCN = QNCNModel.QNCNModel.objects.get(pk=id)

        # Lưu lại giá trị cũ của Đơn vị và Chức vụ
        don_vi_cu = QNCN.DonVi
        chuc_vu_cu = QNCN.ChucVu

        # Cập nhật thông tin sĩ quan
        QNCN.HoTen = HoTen
        QNCN.NgaySinh = NgaySinh
        QNCN.MaQuanNhan = MaQuanNhan
        QNCN.DonVi = DonVi
        QNCN.ChucVu = ChucVu
        QNCN.CapBac = CapBac
        QNCN.NhomQNCN = NhomQNCN
        QNCN.NgayNhapNgu = NgayNhapNgu
        QNCN.SoCanCuoc = SoCanCuoc
        QNCN.QueQuan = QueQuan
        QNCN.NoiO = NoiO

        # Lưu đối tượng vào cơ sở dữ liệu
        QNCN.save()

        # Gọi hàm them_sq_dv nếu đơn vị mới khác đơn vị cũ
        if don_vi_cu != DonVi:
            them_qncn_dv(QNCN.id, DonVi.id)

        # Gọi hàm them_sq_cv nếu chức vụ mới khác chức vụ cũ
        if chuc_vu_cu != ChucVu:
            them_qncn_cv(QNCN.id, ChucVu.id)

        # Trả về thông báo thành công
        return {"status": "success", "data": 'Sửa thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    


def XoaQNCN(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        QNCN = SiQuanModel.SiQuanModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        QNCN.TrangThai=False
        QNCN.save()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TimQNCN(TimKiem, TenDV, trang=1):
    try:
        # Xử lý tìm kiếm theo tên, mã quân nhân, và tên đơn vị
        si_quan_queryset = QNCNModel.QNCNModel.objects.filter(TrangThai=True)

        # Tìm kiếm theo tên đơn vị nếu có
        if TenDV:
            si_quan_queryset = si_quan_queryset.filter(DonVi__TenDonVi__icontains=TenDV)

        # Tìm kiếm theo tên hoặc mã quân nhân nếu có
        if TimKiem:
            si_quan_queryset = si_quan_queryset.filter(
                Q(HoTen__icontains=TimKiem) | 
                Q(MaQuanNhan__icontains=TimKiem)
            ).distinct()

        # Phân trang
        paginator = Paginator(si_quan_queryset, SoDoiTuongMoiTrang)  # Tạo đối tượng Paginator
        trang_hien_tai = paginator.get_page(trang)  # Lấy trang hiện tại

        # Tạo danh sách các kết quả
        results = []
        for si_quan in si_quan_queryset:
            results.append({
                "id": si_quan.id,
                "HoTen": si_quan.HoTen,
                "NhomSQ": si_quan.NhomQNCN.TenNhom,
                "MaQuanNhan": si_quan.MaQuanNhan,
                "TenDonVi": si_quan.DonVi.TenDonVi,
                "TenCapBac": si_quan.CapBac.TenCapBac 

            })

        return {
            "status": "success",
            "data": results,
            "total_pages": paginator.num_pages,
            "current_page": trang_hien_tai.number,
            "has_next": trang_hien_tai.has_next(),
            "has_previous": trang_hien_tai.has_previous()
        }
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
        

def SiQuanTrongDonVi(id_DonVi,trang=1):
    try:
        # Lấy tất cả các sĩ quan thuộc đơn vị với id_DonVi
        si_quan_queryset = SiQuanModel.SiQuanModel.objects.filter(DonVi_id=id_DonVi,TrangThai=True)

        # Phân trang
        paginator = Paginator(si_quan_queryset, SoDoiTuongMoiTrang)  # Tạo đối tượng Paginator
        trang_hien_tai = paginator.get_page(trang)  # Lấy trang hiện tại

        # Tạo danh sách các kết quả
        results = []
        for si_quan in trang_hien_tai:
            results.append({
                "HoTen": si_quan.HoTen,
                "MaQuanNhan": si_quan.MaQuanNhan,
                "TenDonVi": si_quan.DonVi.TenDonVi, 
                "TenCapBac": si_quan.CapBac.TenCapBac
            })

        return {
            "status": "success",
            "data": results,
            "total_pages": paginator.num_pages,
            "current_page": trang_hien_tai.number,
            "has_next": trang_hien_tai.has_next(),
            "has_previous": trang_hien_tai.has_previous()
        }
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def XemLichSuChucVu(id):
    try:
        # Lấy tất cả các lịch sử chức vụ của sĩ quan với id
        lich_su_queryset = QNCN_CVModel.QNCN_CVModel.objects.filter(QNCN_id=id).order_by('-id')

        # Tạo danh sách các kết quả
        results = []
        for lich_su in lich_su_queryset:
            results.append({
                "ChucVu": lich_su.CV.TenChucVu,  # Giả sử CVSiQuanModel có trường TenChucVu
                "TuNgay": lich_su.TuNgay,
                "DenNgay": lich_su.DenNgay
            })

        return {"status": "success", "data": results}
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def XemLichSuDonVi(id):
    try:
        # Lấy tất cả các lịch sử đơn vị của sĩ quan với id
        lich_su_queryset = QNCN_DVModel.QNCN_DVModel.objects.filter(QNCN_id=id).order_by('-id')

        # Tạo danh sách các kết quả
        results = []
        for lich_su in lich_su_queryset:
            results.append({
                "TenDonVi": lich_su.DV.TenDonVi,  # Giả sử DonViModel có trường TenDonVi
                "TuNgay": lich_su.TuNgay,
                "DenNgay": lich_su.DenNgay
            })

        return {"status": "success", "data": results}
    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def ThongTinChiTiet(id):
    try:
        # Lấy thông tin chi tiết của sĩ quan dựa trên id
        si_quan = QNCNModel.QNCNModel.objects.get(id=id)

        # Chuyển đổi thông tin thành dạng có thể trả về
        data = {
            "HoTen": si_quan.HoTen,
            "NgaySinh": si_quan.NgaySinh,
            "MaQuanNhan": si_quan.MaQuanNhan,
            "DonVi": si_quan.DonVi.TenDonVi,
            "ChucVu": si_quan.ChucVu.TenChucVu,
            "CapBac": si_quan.CapBac.TenCapBac,
            "NhomSQ": si_quan.NhomQNCN.TenNhom,  
            "NgayNhapNgu": si_quan.NgayNhapNgu,
            "SoCanCuoc": si_quan.SoCanCuoc,
            "QueQuan": si_quan.QueQuan,
            "NoiO": si_quan.NoiO,
            "IDDonVi": si_quan.DonVi.id,
            "IDChucVu": si_quan.ChucVu.id,
            "IDCapBac": si_quan.CapBac.id,
            "IDNhomSQ": si_quan.NhomQNCN.id,
        }

        return {"status": "success", "data": data}

    except SiQuanModel.SiQuanModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy sĩ quan với ID đã cho."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def LayQNCNTuMa(MaQNCN):
    try:
        si_quan = QNCNModel.QNCNModel.objects.get(MaQuanNhan=MaQNCN,TrangThai=True)
        return si_quan
    except SiQuanModel.SiQuanModel.DoesNotExist:
        print(f"Không tìm thấy mã quân nhân: {MaQNCN}")
        return None
    except SiQuanModel.SiQuanModel.MultipleObjectsReturned:
        print(f"Nhiều quân nhân có cùng mã: {MaQNCN}")
        return None
    except Exception as e:
        print(f"Lỗi khác: {str(e)}")
        return None
    

def LayTenQNCNTuMa(MaQNCN):
    try:
        si_quan = QNCNModel.QNCNModel.objects.get(MaQuanNhan=MaQNCN,TrangThai=True)
        return {"status": "success", "HoTen": si_quan.HoTen}
    except:
        return {"status": "success", "HoTen": ""}
    

def DSTiepKhachSQ(id, NgayBD=None, NgayKT=None):
    try:
        if NgayBD:
            NgayBD = datetime.strptime(NgayBD, '%Y-%m-%d').date()
        if NgayKT:
            NgayKT = datetime.strptime(NgayKT, '%Y-%m-%d').date()
        # Truy vấn cơ bản theo id của sĩ quan
        ds_khach = KhachQNCNModel.KhachQNCNModel.objects.filter(QNCN_id=id)
        
        # Nếu NgayBD không None, lọc các khách từ NgayBD trở đi
        if NgayBD:
            NgayBD_start = datetime.combine(NgayBD, datetime.min.time())  # Bắt đầu từ 00:00:00 của ngày đó
            ds_khach = ds_khach.filter(ThoiGianBatDau__gte=NgayBD_start)
        
        # Nếu NgayKT không None, lọc các khách có ThoiGianKetThuc đến hết ngày NgayKT
        if NgayKT:
            NgayKT_end = datetime.combine(NgayKT, datetime.max.time())  # Kết thúc ở 23:59:59 của ngày đó
            ds_khach = ds_khach.filter(ThoiGianKetThuc__lte=NgayKT_end)
        
        # Chuẩn bị dữ liệu trả về
        result = []
        for khach in ds_khach:
            result.append({
                'Khach': khach.Khach.HoTenKhach,  # Tên khách
                'LoaiKhach': khach.Khach.Loai.TenLoaiKhach,
                'SoThe': khach.TheKhach.SoThe,  # Số thẻ khách
                'NgayBatDau': khach.ThoiGianBatDau.date().strftime('%d/%m/%Y'),  # Ngày tháng năm bắt đầu
                'GioBatDau': khach.ThoiGianBatDau.time().strftime('%H:%M'),  # Giờ phút bắt đầu
                'NgayKetThuc': khach.ThoiGianKetThuc.date().strftime('%d/%m/%Y') if khach.ThoiGianKetThuc else None,  # Ngày tháng năm kết thúc
                'GioKetThuc': khach.ThoiGianKetThuc.time().strftime('%H:%M') if khach.ThoiGianKetThuc else None,  # Giờ phút kết thúc
                'GhiChu': khach.GhiChu  # Ghi chú
            })
        
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

    