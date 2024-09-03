from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVSiQuan


@api_view(['POST'])
def ThemSiQuan(request):
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
    result = NVSiQuan.ThemSiQuan(HoTen, NgaySinh, MaQuanNhan, DonVi_id, ChucVu_id, CapBac_id, NhomSQ_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaSiQuan(request,id):
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
    result = NVSiQuan.SuaSiQuan(id, HoTen, NgaySinh, MaQuanNhan, DonVi_id, ChucVu_id, CapBac_id, NhomSQ_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaSiQuan(request,id):
    result = NVSiQuan.XoaSiQuan(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def TimSiQuan(request):
    TimKiem = request.GET.get('TimKiem')
    TenDV = request.GET.get('TenDV')
    page = request.GET.get('page')
    result = NVSiQuan.TimSiQuan(TimKiem,TenDV,page)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def LSDV(request,id):
    result = NVSiQuan.XemLichSuDonVi(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def LSCV(request,id):
    result = NVSiQuan.XemLichSuChucVu(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ThongTinChiTiet(request,id):
    result = NVSiQuan.ThongTinChiTiet(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def LayTenSQTuMa(request,id):
    result = NVSiQuan.LayTenSQTuMa(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    


