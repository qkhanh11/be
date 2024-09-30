from model import HocVienModel,DonViModel,CBHaSiQuanModel
from be.settings import SoDoiTuongMoiTrang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def ThemHocVien(HoTen,NgaySinh,MaQuanNhan,DonVi,CapBac,NgayNhapNgu,SoCanCuoc,QueQuan,NoiO):
    try:
        don_vi = DonViModel.DonViModel.objects.get(pk=DonVi)
        cap_bac = CBHaSiQuanModel.CBHaSiQuanModel.objects.get(pk=CapBac)
        hoc_vien = HocVienModel.HocVienModel.objects.create(
            HoTen=HoTen,
            NgaySinh=NgaySinh,
            MaQuanNhan=MaQuanNhan,
            DonVi=don_vi,
            CapBac=cap_bac,
            NgayNhapNgu=NgayNhapNgu,
            SoCanCuoc=SoCanCuoc,
            QueQuan=QueQuan,
            NoiO=NoiO
        )
        return {"status": "success", "data": 'Thêm thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def SuaHocVien(id,HoTen,NgaySinh,MaQuanNhan,DonVi,CapBac,NgayNhapNgu,SoCanCuoc,QueQuan,NoiO):
    try:
        don_vi = DonViModel.DonViModel.objects.get(pk=DonVi)
        cap_bac = CBHaSiQuanModel.CBHaSiQuanModel.objects.get(pk=CapBac)
        hoc_vien = HocVienModel.HocVienModel.objects.get(pk=id)
        hoc_vien.HoTen=HoTen
        hoc_vien.NgaySinh=NgaySinh
        hoc_vien.MaQuanNhan=MaQuanNhan
        hoc_vien.DonVi=don_vi
        hoc_vien.CapBac=cap_bac
        hoc_vien.NgayNhapNgu=NgayNhapNgu
        hoc_vien.SoCanCuoc=SoCanCuoc
        hoc_vien.QueQuan=QueQuan
        hoc_vien.NoiO=NoiO
        

        hoc_vien.save()
        return {"status": "success", "data": 'Sửa thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def XoaHocVien(id):
    try:
        hoc_vien = HocVienModel.HocVienModel.objects.get(pk=id)
        hoc_vien.TinhTrang = False
        hoc_vien.save()
        return {"status": "success", "data": 'Xóa thành công'}

    except Exception as e:
        # Trả về thông báo lỗi nếu có lỗi xảy ra
        return {"status": "error", "message": str(e)}
    

def TatCaHocVien(page=1):
    try:
        # Truy vấn tất cả các chiến sĩ
        chien_si_list = HocVienModel.HocVienModel.objects.filter(TinhTrang=True)
        
        # Tạo danh sách dữ liệu để trả về
        data = []
        for chien_si in chien_si_list:
            data.append({
                "id": chien_si.id,
                "HoTen": chien_si.HoTen,
                "Ma": chien_si.MaQuanNhan,
                "CapBac": chien_si.CapBac.TenCapBac,
                "TenDonVi": chien_si.DonVi.TenDonVi,
                "QueQuan": chien_si.QueQuan
            })

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}


def TimKiemHocVien(keyword,DonVi,page=1):
    try:
        # Bắt đầu với toàn bộ danh sách học viên
        hoc_vien_queryset = HocVienModel.HocVienModel.objects.all()

        # Tìm kiếm theo tên đơn vị nếu có
        if DonVi:
            hoc_vien_queryset = hoc_vien_queryset.filter(
                Q(DonVi__TenDonVi__icontains=DonVi)|
                Q(DonVi__MaDonVi__icontains=DonVi)
                )

        # Tìm kiếm theo tên hoặc mã quân nhân nếu có
        if keyword:
            hoc_vien_queryset = hoc_vien_queryset.filter(
                Q(HoTen__icontains=keyword) | 
                Q(MaQuanNhan__icontains=keyword)
            ).distinct()

        # Phân trang
        paginator = Paginator(hoc_vien_queryset, SoDoiTuongMoiTrang)  # Tạo đối tượng Paginator
        trang_hien_tai = paginator.get_page(page)  # Lấy trang hiện tại

        # Tạo danh sách các kết quả
        results = []
        for hoc_vien in trang_hien_tai:
            results.append({
                "id": hoc_vien.id,
                "HoTen": hoc_vien.HoTen,
                "MaQuanNhan": hoc_vien.MaQuanNhan,
                "CapBac__TenCapBac": hoc_vien.CapBac.TenCapBac,
                "NgaySinh": hoc_vien.NgaySinh,
                "DonVi__TenDonVi": hoc_vien.DonVi.TenDonVi
                
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
    


def TimHVTrongDonVi(keyword,DonVi,page=1):
    try:
        # Bắt đầu với toàn bộ danh sách học viên
        donvi = DonViModel.DonViModel.objects.get(pk=DonVi)
        hoc_vien_queryset = HocVienModel.HocVienModel.objects.filter(DonVi=donvi)

        # Tìm kiếm theo tên đơn vị nếu có
        # Tìm kiếm theo tên hoặc mã quân nhân nếu có
        if keyword:
            hoc_vien_queryset = hoc_vien_queryset.filter(
                Q(HoTen__icontains=keyword) | 
                Q(MaQuanNhan__icontains=keyword)
            ).distinct()

        # Phân trang
        paginator = Paginator(hoc_vien_queryset, SoDoiTuongMoiTrang)  # Tạo đối tượng Paginator
        trang_hien_tai = paginator.get_page(page)  # Lấy trang hiện tại

        # Tạo danh sách các kết quả
        results = []
        for hoc_vien in trang_hien_tai:
            results.append({
                "id": hoc_vien.id,
                "HoTen": hoc_vien.HoTen,
                "MaQuanNhan": hoc_vien.MaQuanNhan,
                "CapBac__TenCapBac": hoc_vien.CapBac.TenCapBac,
                "NgaySinh": hoc_vien.NgaySinh,
                "DonVi__TenDonVi": hoc_vien.DonVi.TenDonVi
                
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
    

def ChiTietHocVien(id):
    try:
        # Lấy đối tượng chiến sĩ theo ID
        chien_si = HocVienModel.HocVienModel.objects.select_related('DonVi', 'CapBac').get(pk=id)
        
        # Tạo dữ liệu chi tiết của chiến sĩ
        data = {
            "id": chien_si.id,
            "HoTen": chien_si.HoTen,
            "Ma": chien_si.MaQuanNhan,
            "NgaySinh": chien_si.NgaySinh,
            "DonVi": chien_si.DonVi.TenDonVi,
            "CapBac": chien_si.CapBac.TenCapBac,
            "NgayNhapNgu": chien_si.NgayNhapNgu,
            "SoCanCuoc": chien_si.SoCanCuoc,
            "QueQuan": chien_si.QueQuan,
            "NoiO": chien_si.NoiO,
            "IDDonVi": chien_si.DonVi.id,
            "IDCapBac": chien_si.CapBac.id

        }

        return {"status": "success", "data": data}

    except Exception as e:
        return {"status": "error", "message": str(e)}