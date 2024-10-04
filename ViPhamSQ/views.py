from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVViPham


@api_view(['POST'])
def ThemViPhamSQ(request):
    masq = request.data.get('masq')
    LoiViPham = request.data.get('LoiViPham')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    cong = request.data.get('cong')
    ghichu = request.data.get('ghichu')
    result = NVViPham.ThemViPhamSQ(masq, LoiViPham, ngay, gio, cong, ghichu)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaViPhamSQ(request,id):
    masq = request.data.get('masq')
    LoiViPham = request.data.get('LoiViPham')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    cong = request.data.get('cong')
    ghichu = request.data.get('ghichu')
    result = NVViPham.SuaViPhamSQ(id, masq, LoiViPham, ngay, gio, cong, ghichu)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaViPhamSQ(request,id):
    result = NVViPham.XoaViPhamSQ(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ChiTietViPhamSQ(request,id):
    result = NVViPham.ChiTietViPhamSQ(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def TatCaViPhamSQ(request):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVViPham.TatCaViPhamSQ(NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ViPhamSQ(request,id):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVViPham.ViPhamSQ(id,NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)

    


