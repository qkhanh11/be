from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVRaVaoQNCN

@api_view(['POST'])
def RaVaoSQ(request):
    sothe = request.data.get('sothe')
    trangthai = request.data.get('trangthai')
    cong = request.data.get('cong')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    result = NVRaVaoQNCN.RaVaoQNCN(sothe,trangthai,cong,ngay,gio)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def RaVaoSQDacBiet(request):
    sothe = request.data.get('sothe')
    trangthai = request.data.get('trangthai')
    cong = request.data.get('cong')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    result = NVRaVaoQNCN.RaVaoQNCNDacBiet(sothe,trangthai,cong, ngay, gio)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def lay_lich_su_ra_vao(request):
    result = NVRaVaoQNCN.lay_lich_su_ra_vao()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def LSRaVaoSQ(request,id):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVRaVaoQNCN.LSRaVaoQNCN(id,NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ChiTiet(request,id):
    result = NVRaVaoQNCN.ChiTiet(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaRaVaoSQ(request,id):
    sothe = request.data.get('sothe')
    trangthai = request.data.get('trangthai')
    cong = request.data.get('cong')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    print(id, sothe, trangthai,cong, ngay, gio)
    result = NVRaVaoSQ.SuaRaVaoSQ(id, sothe, trangthai,cong, ngay, gio)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        print(result)
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaRaVaoSQ(request,id):
    result = NVRaVaoSQ.XoaRaVaoSQ(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def ThemBanGhi(request):
    sothe = request.data.get('sothe')
    trangthai = request.data.get('trangthai')
    cong = request.data.get('cong')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    result = NVRaVaoSQ.ThemBanGhi( sothe, trangthai,cong, ngay, gio)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)