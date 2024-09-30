from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVHocVien


@api_view(['POST'])
def ThemHocVien(request):
    HoTen = request.data.get('HoTen')
    NgaySinh = request.data.get('NgaySinh')
    MaQuanNhan = request.data.get('MaQuanNhan')
    DonVi = request.data.get('DonVi')
    CapBac = request.data.get('CapBac')
    NgayNhapNgu = request.data.get('NgayNhapNgu')
    SoCanCuoc = request.data.get('SoCanCuoc')
    QueQuan = request.data.get('QueQuan')
    NoiO = request.data.get('NoiO')
    result = NVHocVien.ThemHocVien(HoTen,NgaySinh,MaQuanNhan,DonVi,CapBac,NgayNhapNgu,SoCanCuoc,QueQuan,NoiO)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PUT'])
def SuaHocVien(request,id):
    HoTen = request.data.get('HoTen')
    NgaySinh = request.data.get('NgaySinh')
    MaQuanNhan = request.data.get('MaQuanNhan')
    DonVi = request.data.get('DonVi')
    CapBac = request.data.get('CapBac')
    NgayNhapNgu = request.data.get('NgayNhapNgu')
    SoCanCuoc = request.data.get('SoCanCuoc')
    QueQuan = request.data.get('QueQuan')
    NoiO = request.data.get('NoiO')
    print(id,HoTen,NgaySinh,MaQuanNhan,DonVi,CapBac,NgayNhapNgu,SoCanCuoc,QueQuan,NoiO)
    result = NVHocVien.SuaHocVien(id,HoTen,NgaySinh,MaQuanNhan,DonVi,CapBac,NgayNhapNgu,SoCanCuoc,QueQuan,NoiO)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaHocVien(request,id):
    result = NVHocVien.XoaHocVien(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def TatCaHocVien(request):
    result = NVHocVien.TatCaHocVien()
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def TimHocVien(request):
    keyword = request.GET.get('keyword')
    DonVi = request.GET.get('DonVi')
    page = request.GET.get('page')
    result = NVHocVien.TimKiemHocVien(keyword,DonVi,page)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def TimHVTrongDonVi(request):
    keyword = request.GET.get('keyword')
    DonVi = request.GET.get('DonVi')
    page = request.GET.get('page')
    result = NVHocVien.TimHVTrongDonVi(keyword,DonVi,page)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ChiTietHocVien(request,id):
    result = NVHocVien.ChiTietHocVien(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)