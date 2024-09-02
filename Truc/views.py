from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVTruc



@api_view(['POST'])
def ThemTrucBan(request):
    ngay = request.data.get('ngay')
    TBTruong = request.data.get('TBTruong')
    TBPho = request.data.get('TBPho')
    result = NVTruc.ThemTrucBan(ngay,TBTruong,TBPho)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PUT'])
def SuaTrucBan(request,id):
    ngay = request.data.get('ngay')
    TBTruong = request.data.get('TBTruong')
    TBPho = request.data.get('TBPho')
    result = NVTruc.SuaTrucBan(id, ngay,TBTruong,TBPho)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaTrucBan(request,id):
    result = NVTruc.XoaTrucBan(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def XemTatCaTrucBan(request):
    result = NVTruc.XemTatCaTrucBan()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def XemChiTietTrucBan(request,id):
    result = NVTruc.XemChiTietTrucBan(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


