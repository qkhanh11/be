from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVVC


@api_view(['POST'])
def ThemVC(request):
    HoTen = request.data.get('HoTen')
    NgaySinh = request.data.get('NgaySinh')
    DonVi_id = request.data.get('DonVi_id')
    NhomVC_id = request.data.get('NhomVC_id')
    NgayNhapNgu = request.data.get('NgayBDLamViec')
    SoCanCuoc = request.data.get('SoCanCuoc')
    QueQuan = request.data.get('QueQuan')
    NoiO = request.data.get('NoiO')
    result = NVVC.ThemVC(HoTen, NgaySinh,  DonVi_id, NhomVC_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaVC(request,id):
    HoTen = request.data.get('HoTen')
    NgaySinh = request.data.get('NgaySinh')
    DonVi_id = request.data.get('DonVi_id')
    NhomVC_id = request.data.get('NhomVC_id')
    NgayNhapNgu = request.data.get('NgayBDLamViec')
    SoCanCuoc = request.data.get('SoCanCuoc')
    QueQuan = request.data.get('QueQuan')
    NoiO = request.data.get('NoiO')
    result = NVVC.SuaVC(id, HoTen, NgaySinh,  DonVi_id, NhomVC_id, NgayNhapNgu, SoCanCuoc, QueQuan, NoiO)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaVC(request,id):
    result = NVVC.XoaVC(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def TimVC(request):
    TimKiem = request.GET.get('TimKiem')
    TenDV = request.GET.get('TenDV')
    page = request.GET.get('page')
    result = NVVC.TimVC(TimKiem,TenDV,page)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def LSDV(request,id):
    result = NVVC.XemLichSuDonVi(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ThongTinChiTiet(request,id):
    result = NVVC.ThongTinChiTiet(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def LayVCTuMa(request):
    MaSQ = request.GET.get('SoCanCuoc')
    result = NVVC.LayTenVCTuCC(MaSQ)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET'])
def DSTiepKhachVC(request,id):
    NgayBD = request.GET.get('NgayBD')
    NgayKT = request.GET.get('NgayKT')
    result = NVVC.DSTiepKhachVC(id, NgayBD, NgayKT)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
