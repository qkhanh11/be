from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVQNCN


@api_view(['POST'])
def ThemQNCN(request):
    HoTen = request.data.get('HoTen')
    NgaySinh = request.data.get('NgaySinh')
    MaQuanNhan = request.data.get('MaQuanNhan')
    DonVi_id = request.data.get('DonVi_id')
    ChucVu_id = request.data.get('ChucVu_id')
    CapBac_id = request.data.get('CapBac_id')
    NhomSQ_id = request.data.get('NhomSQ_id')
    NgayNhapNgu = request.data.get('NgayNhapNgu')
    SoCanCuoc = request.data.get('SoCanCuoc')
    QueQuan = request.data.get('QueQuan')
    NoiO = request.data.get('NoiO')
    result = NVQNCN.ThemQNCN(HoTen, NgaySinh, MaQuanNhan, DonVi_id, ChucVu_id, CapBac_id, NhomSQ_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO)
    print(HoTen, NgaySinh, MaQuanNhan, DonVi_id, ChucVu_id, CapBac_id, NhomSQ_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaQNCN(request,id):
    HoTen = request.data.get('HoTen')
    NgaySinh = request.data.get('NgaySinh')
    MaQuanNhan = request.data.get('MaQuanNhan')
    DonVi_id = request.data.get('DonVi_id')
    ChucVu_id = request.data.get('ChucVu_id')
    CapBac_id = request.data.get('CapBac_id')
    NhomSQ_id = request.data.get('NhomSQ_id')
    NgayNhapNgu = request.data.get('NgayNhapNgu')
    SoCanCuoc = request.data.get('SoCanCuoc')
    QueQuan = request.data.get('QueQuan')
    NoiO = request.data.get('NoiO')
    result = NVQNCN.SuaQNCN(id, HoTen, NgaySinh, MaQuanNhan, DonVi_id, ChucVu_id, CapBac_id, NhomSQ_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaQNCN(request,id):
    result = NVQNCN.XoaQNCN(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def TimQNCN(request):
    TimKiem = request.GET.get('TimKiem')
    TenDV = request.GET.get('TenDV')
    page = request.GET.get('page')
    result = NVQNCN.TimQNCN(TimKiem,TenDV,page)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def LSDV(request,id):
    result = NVQNCN.XemLichSuDonVi(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def LSCV(request,id):
    result = NVQNCN.XemLichSuChucVu(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ThongTinChiTiet(request,id):
    result = NVQNCN.ThongTinChiTiet(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def  LayTenQNCNTuMa(request):
    MaSQ = request.GET.get('MaSQ')
    result = NVQNCN.LayTenQNCNTuMa(MaSQ)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET'])
def DSTiepKhachQNCN(request,id):
    NgayBD = request.GET.get('NgayBD')
    NgayKT = request.GET.get('NgayKT')
    result = NVQNCN.DSTiepKhachSQ(id, NgayBD, NgayKT)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
