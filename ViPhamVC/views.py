from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVViPhamVC


@api_view(['POST'])
def ThemViPhamVC(request):
    SoCanCuoc = request.data.get('SoCanCuoc')
    LoiViPham = request.data.get('LoiViPham')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    cong = request.data.get('cong')
    ghichu = request.data.get('ghichu')
    result = NVViPhamVC.ThemViPhamVC(SoCanCuoc, LoiViPham, ngay, gio, cong, ghichu)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaViPhamVC(request,id):
    SoCanCuoc = request.data.get('SoCanCuoc')
    LoiViPham = request.data.get('LoiViPham')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    cong = request.data.get('cong')
    ghichu = request.data.get('ghichu')
    result = NVViPhamVC.SuaViPhamVC(id, SoCanCuoc, LoiViPham, ngay, gio, cong, ghichu)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaViPhamVC(request,id):
    result = NVViPhamVC.XoaViPhamVC(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ChiTietViPhamVC(request,id):
    result = NVViPhamVC.ChiTietViPhamVC(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def TatCaViPhamVC(request):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVViPhamVC.TatCaViPhamVC(NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ViPhamVC(request,id):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVViPhamVC.ViPhamVC(id,NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
