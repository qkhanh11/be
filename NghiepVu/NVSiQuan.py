from model import SiQuanModel, DonViModel, CVSiQuanModel, CapBacModel, NhomSQModel,SQ_DVModel,SQ_CVModel
from django.db import transaction
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from be.settings import SoDoiTuongMoiTrang



def them_sq_dv(id_SQ, id_DonVi):
    try:
        # Lấy ngày hiện tại
        today = timezone.now().date()

        # Bắt đầu transaction để đảm bảo tính nhất quán dữ liệu
        with transaction.atomic():
            # Tìm bản ghi có SQ = id_SQ và DenNgay là null
            existing_record = SQ_DVModel.SQ_DVModel.objects.filter(SQ_id=id_SQ, DenNgay__isnull=True).first()
            
            # Nếu đã tồn tại bản ghi, cập nhật DenNgay là hôm nay
            if existing_record:
                existing_record.DenNgay = today
                existing_record.save()

            # Thêm bản ghi mới với SQ = id_SQ, DonVi = id_DonVi và TuNgay là hôm nay
            new_record = SQ_DVModel.SQ_DVModel(SQ_id=id_SQ, DV_id=id_DonVi, TuNgay=today)
            new_record.save()

            return new_record
    except Exception as e:
        # Xử lý lỗi nếu có
        print(f"Lỗi xảy ra: {e}")
        return None


def them_sq_cv(id_SQ, id_CV):
    try:
        # Lấy ngày hiện tại
        today = timezone.now().date()

        # Bắt đầu transaction để đảm bảo tính nhất quán dữ liệu
        with transaction.atomic():
            # Tìm bản ghi có SQ = id_SQ và DenNgay là null
            existing_record = SQ_CVModel.SQ_CVModel.objects.filter(SQ_id=id_SQ, DenNgay__isnull=True).first()
            
            # Nếu đã tồn tại bản ghi, cập nhật DenNgay là hôm nay
            if existing_record:
                existing_record.DenNgay = today
                existing_record.save()

            # Thêm bản ghi mới với SQ = id_SQ, CV = id_CV và TuNgay là hôm nay
            new_record = SQ_CVModel.SQ_CVModel(SQ_id=id_SQ, CV_id=id_CV, TuNgay=today)
            new_record.save()

            return new_record
    except Exception as e:
        # Xử lý lỗi nếu có
        print(f"Lỗi xảy ra: {e}")
        return None


def ThemSiQuan(HoTen, NgaySinh, MaQuanNhan, DonVi_id, ChucVu_id, CapBac_id, NhomSQ_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO):
    try:
        # Lấy các đối tượng liên quan dựa trên ID
        DonVi = DonViModel.DonViModel.objects.get(pk=DonVi_id)
        ChucVu = CVSiQuanModel.CVSiQuanModel.objects.get(pk=ChucVu_id)
        CapBac = CapBacModel.CapBacModel.objects.get(pk=CapBac_id)
        NhomSQ = NhomSQModel.NhomSQModel.objects.get(pk=NhomSQ_id)
        if SiQuanModel.SiQuanModel.objects.filter(MaQuanNhan=MaQuanNhan).exists():
            return {"status": "error", "message": "Mã quân nhân đã tồn tại"}


        # Tạo đối tượng SiQuanModel mới
        si_quan = SiQuanModel.SiQuanModel(
            HoTen=HoTen,
            NgaySinh=NgaySinh,
            MaQuanNhan=MaQuanNhan,
            DonVi=DonVi,
            ChucVu=ChucVu,
            CapBac=CapBac,
            NhomSQ=NhomSQ,
            NgayNhapNgu=NgayNhapNgu,
            SoCanCuoc=SoCanCuoc,
            QueQuan=QueQuan,
            NoiO=NoiO
        )

        # Lưu đối tượng vào cơ sở dữ liệu
        si_quan.save()

        them_sq_dv(si_quan.id, DonVi.id)

        # Gọi hàm để thêm bản ghi vào SQ_CVModel
        them_sq_cv(si_quan.id, ChucVu.id)
        # Trả về thông báo thành công và dữ liệu của sĩ quan mới
        return {"status": "success", "data": 'Thêm thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaSiQuan(id, HoTen, NgaySinh, MaQuanNhan, DonVi_id, ChucVu_id, CapBac_id, NhomSQ_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO):
    try:
        # Lấy các đối tượng liên quan dựa trên ID
        DonVi = DonViModel.DonViModel.objects.get(pk=DonVi_id)
        ChucVu = CVSiQuanModel.CVSiQuanModel.objects.get(pk=ChucVu_id)
        CapBac = CapBacModel.CapBacModel.objects.get(pk=CapBac_id)
        NhomSQ = NhomSQModel.NhomSQModel.objects.get(pk=NhomSQ_id)

        if SiQuanModel.SiQuanModel.objects.exclude(pk=id).filter(MaQuanNhan=MaQuanNhan).exists():
            return {"status": "error", "message": "Mã quân nhân đã tồn tại"}
        # Lấy đối tượng SiQuanModel hiện tại
        si_quan = SiQuanModel.SiQuanModel.objects.get(pk=id)

        # Lưu lại giá trị cũ của Đơn vị và Chức vụ
        don_vi_cu = si_quan.DonVi
        chuc_vu_cu = si_quan.ChucVu

        # Cập nhật thông tin sĩ quan
        si_quan.HoTen = HoTen
        si_quan.NgaySinh = NgaySinh
        si_quan.MaQuanNhan = MaQuanNhan
        si_quan.DonVi = DonVi
        si_quan.ChucVu = ChucVu
        si_quan.CapBac = CapBac
        si_quan.NhomSQ = NhomSQ
        si_quan.NgayNhapNgu = NgayNhapNgu
        si_quan.SoCanCuoc = SoCanCuoc
        si_quan.QueQuan = QueQuan
        si_quan.NoiO = NoiO

        # Lưu đối tượng vào cơ sở dữ liệu
        si_quan.save()

        # Gọi hàm them_sq_dv nếu đơn vị mới khác đơn vị cũ
        if don_vi_cu != DonVi:
            them_sq_dv(si_quan.id, DonVi.id)

        # Gọi hàm them_sq_cv nếu chức vụ mới khác chức vụ cũ
        if chuc_vu_cu != ChucVu:
            them_sq_cv(si_quan.id, ChucVu.id)

        # Trả về thông báo thành công
        return {"status": "success", "data": 'Sửa thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    


def XoaSiQuan(id):
    try:
        # Lấy đối tượng dựa trên khóa chính (id)
        SQ = SiQuanModel.SiQuanModel.objects.get(pk=id)
        
        # Xóa đối tượng khỏi cơ sở dữ liệu
        SQ.delete()

        return {"status": "success", "message": "Xóa thành công."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def TimSiQuan(TimKiem, TenDV, trang=1):
    try:
        # Xử lý tìm kiếm theo tên, mã quân nhân, và tên đơn vị
        si_quan_queryset = SiQuanModel.SiQuanModel.objects.all()

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
        for si_quan in trang_hien_tai:
            results.append({
                "id": si_quan.id,
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
        

def SiQuanTrongDonVi(id_DonVi,trang=1):
    try:
        # Lấy tất cả các sĩ quan thuộc đơn vị với id_DonVi
        si_quan_queryset = SiQuanModel.SiQuanModel.objects.filter(DonVi_id=id_DonVi)

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
        lich_su_queryset = SQ_CVModel.SQ_CVModel.objects.filter(SQ_id=id).order_by('TuNgay')

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
        lich_su_queryset = SQ_DVModel.SQ_DVModel.objects.filter(SQ_id=id).order_by('TuNgay')

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
        si_quan = SiQuanModel.SiQuanModel.objects.get(id=id)

        # Chuyển đổi thông tin thành dạng có thể trả về
        data = {
            "HoTen": si_quan.HoTen,
            "NgaySinh": si_quan.NgaySinh,
            "MaQuanNhan": si_quan.MaQuanNhan,
            "DonVi": si_quan.DonVi.TenDonVi,
            "ChucVu": si_quan.ChucVu.TenChucVu,
            "CapBac": si_quan.CapBac.TenCapBac,
            "NhomSQ": si_quan.NhomSQ.TenNhom,  
            "NgayNhapNgu": si_quan.NgayNhapNgu,
            "SoCanCuoc": si_quan.SoCanCuoc,
            "QueQuan": si_quan.QueQuan,
            "NoiO": si_quan.NoiO
        }

        return {"status": "success", "data": data}

    except SiQuanModel.SiQuanModel.DoesNotExist:
        return {"status": "error", "message": "Không tìm thấy sĩ quan với ID đã cho."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def LaySQTuMa(MaSQ):
    try:
        si_quan = SiQuanModel.SiQuanModel.objects.get(MaQuanNhan=MaSQ)
        return si_quan
    except SiQuanModel.SiQuanModel.DoesNotExist:
        print(f"Không tìm thấy mã quân nhân: {MaSQ}")
        return None
    except SiQuanModel.SiQuanModel.MultipleObjectsReturned:
        print(f"Nhiều quân nhân có cùng mã: {MaSQ}")
        return None
    except Exception as e:
        print(f"Lỗi khác: {str(e)}")
        return None