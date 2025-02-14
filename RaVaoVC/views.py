from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVRaVaoVC

@api_view(['POST'])
def RaVaoVC(request):
    sothe = request.data.get('sothe')
    trangthai = request.data.get('trangthai')
    cong = request.data.get('cong')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    result = NVRaVaoVC.RaVaoVC(sothe,trangthai,cong,ngay,gio)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def RaVaoVCDacBiet(request):
    sothe = request.data.get('sothe')
    trangthai = request.data.get('trangthai')
    cong = request.data.get('cong')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    result = NVRaVaoVC.RaVaoVCDacBiet(sothe,trangthai,cong, ngay, gio)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def lay_lich_su_ra_vao(request):
    result = NVRaVaoVC.lay_lich_su_ra_vao()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def LSRaVaoVC(request,id):
    NgayBD = request.GET.get("NgayBD")
    NgayKT = request.GET.get("NgayKT")
    result = NVRaVaoVC.LSRaVaoVC(id,NgayBD,NgayKT)
    if result["status"] == "success" or result["status"] == "success1":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ChiTiet(request,id):
    result = NVRaVaoVC.ChiTiet(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaRaVaoVC(request,id):
    sothe = request.data.get('sothe')
    trangthai = request.data.get('trangthai')
    cong = request.data.get('cong')
    ngay = request.data.get('ngay')
    gio = request.data.get('gio')
    print(id, sothe, trangthai,cong, ngay, gio)
    result = NVRaVaoVC.SuaRaVaoVC(id, sothe, trangthai,cong, ngay, gio)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        print(result)
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaRaVaoVC(request,id):
    result = NVRaVaoVC.XoaRaVaoVC(id)
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
    result = NVRaVaoVC.ThemBanGhi( sothe, trangthai,cong, ngay, gio)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)