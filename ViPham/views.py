from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVViPham



@api_view(['GET'])
def TatCaLoiViPham(request):
    result = NVViPham.TatCaLoiViPham()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def ThemLoiViPham(request):
    TenLoi = request.data.get('TenLoi')
    GiaiThich = request.data.get('GiaiThich')
    result = NVViPham.ThemLoiViPham(TenLoi,GiaiThich)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaLoiViPham(request,id):
    TenLoi = request.data.get('TenLoi')
    GiaiThich = request.data.get('GiaiThich')
    result = NVViPham.SuaLoiViPham(id, TenLoi, GiaiThich)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaLoiViPham(request,id):
    result = NVViPham.XoaLoiViPham(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


