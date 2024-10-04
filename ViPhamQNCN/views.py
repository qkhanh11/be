from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVViPhamQNCN


@api_view(['POST'])
def ThemViPhamQNCN(request):
    maqncn = request.data.get('maQNCN')
    LoiViPham = request.data.get('LoiViPham')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    cong = request.data.get('cong')
    ghichu = request.data.get('ghichu')
    result = NVViPhamQNCN.ThemViPhamQNCN(maqncn, LoiViPham, ngay, gio, cong, ghichu)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaViPhamQNCN(request,id):
    maqncn = request.data.get('maQNCN')
    LoiViPham = request.data.get('LoiViPham')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    cong = request.data.get('cong')
    ghichu = request.data.get('ghichu')
    result = NVViPhamQNCN.SuaViPhamQNCN(id, maqncn, LoiViPham, ngay, gio, cong, ghichu)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaViPhamQNCN(request,id):
    result = NVViPhamQNCN.XoaViPhamQNCN(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ChiTietViPhamQNCN(request,id):
    result = NVViPhamQNCN.ChiTietViPhamQNCN(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def TatCaViPhamQNCN(request):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVViPhamQNCN.TatCaViPhamQNCN(NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ViPhamQNCN(request,id):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVViPhamQNCN.ViPhamQNCN(id,NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
