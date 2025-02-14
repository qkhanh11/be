from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVViPhamHV


@api_view(['POST'])
def ThemViPhamHV(request):
    mahv = request.data.get('maHV')
    LoiViPham = request.data.get('LoiViPham')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    cong = request.data.get('cong')
    ghichu = request.data.get('ghichu')
    result = NVViPhamHV.ThemViPhamHV(mahv, LoiViPham, ngay, gio, cong, ghichu)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaViPhamHV(request,id):
    mahv = request.data.get('maHV')
    LoiViPham = request.data.get('LoiViPham')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    cong = request.data.get('cong')
    ghichu = request.data.get('ghichu')
    result = NVViPhamHV.SuaViPhamHV(id, mahv, LoiViPham, ngay, gio, cong, ghichu)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaViPhamHV(request,id):
    result = NVViPhamHV.XoaViPhamHV(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ChiTietViPhamHV(request,id):
    result = NVViPhamHV.ChiTietViPhamHV(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def TatCaViPhamHV(request):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVViPhamHV.TatCaViPhamHV(NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ViPhamHV(request,id):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVViPhamHV.ViPhamHV(id,NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
