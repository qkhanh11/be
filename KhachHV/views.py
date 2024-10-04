from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVKhachHV


@api_view(['POST'])
def TiepKhachHV(request):
    HV = request.data.get('HV')
    HoTenKhach = request.data.get('HoTenKhach')
    SoDinhDanh = request.data.get('SoDinhDanh')
    NgayBD = request.data.get('NgayBD')
    GioBD = request.data.get('GioBD')
    NgayKT = request.data.get('NgayKT')
    GioKT = request.data.get('GioKT')
    GhiChu = request.data.get('GhiChu')
    result = NVKhachHV.TiepKhachHV(HV,HoTenKhach,SoDinhDanh,NgayBD, GioBD,NgayKT,GioKT,GhiChu)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PUT'])
def SuaTiepKhachHV(request,id):
    HV = request.data.get('HV')
    HoTenKhach = request.data.get('HoTenKhach')
    SoDinhDanh = request.data.get('SoDinhDanh')
    NgayBD = request.data.get('NgayBD')
    GioBD = request.data.get('GioBD')
    NgayKT = request.data.get('NgayKT')
    GioKT = request.data.get('GioKT')
    GhiChu = request.data.get('GhiChu')
    result = NVKhachHV.SuaTiepKhachHV(id,HV,HoTenKhach,SoDinhDanh,NgayBD, GioBD,NgayKT,GioKT,GhiChu)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def TraKhach(request,id):
    result = NVKhachHV.TraKhach(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def XoaTiepKhachHV(request,id):
    result = NVKhachHV.XoaTiepKhachHV(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def DangTiepKhach(request):
    result = NVKhachHV.DangTiepKhach()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def DanhSachTiepKhach(request):
    result = NVKhachHV.DanhSachTiepKhach()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
   