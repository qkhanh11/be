from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVChienSi

@api_view(['POST'])
def ThemChienSi(request):
    HoTen = request.data.get('HoTen')
    Ma = request.data.get('Ma')
    NgaySinh = request.data.get('NgaySinh')
    DonVi = request.data.get('DonVi')
    CapBac = request.data.get('CapBac')
    NgayNhapNgu = request.data.get('NgayNhapNgu')
    SoCanCuoc = request.data.get('SoCanCuoc')
    QueQuan = request.data.get('QueQuan')
    NoiO = request.data.get('NoiO')

    result = NVChienSi.ThemChienSi(HoTen,Ma,NgaySinh,DonVi,CapBac,NgayNhapNgu,SoCanCuoc,QueQuan,NoiO)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PUT'])
def SuaChienSi(request,id):
    HoTen = request.data.get('HoTen')
    Ma = request.data.get('Ma')
    NgaySinh = request.data.get('NgaySinh')
    DonVi = request.data.get('DonVi')
    CapBac = request.data.get('CapBac')
    NgayNhapNgu = request.data.get('NgayNhapNgu')
    SoCanCuoc = request.data.get('SoCanCuoc')
    QueQuan = request.data.get('QueQuan')
    NoiO = request.data.get('NoiO')

    result = NVChienSi.SuaChienSi(id,HoTen,Ma,NgaySinh,DonVi,CapBac,NgayNhapNgu,SoCanCuoc,QueQuan,NoiO)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaChienSi(request,id):
    result = NVChienSi.XoaChienSi(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def TatCaChienSi(request):
    result = NVChienSi.TatCaChienSi()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def ChiTietChienSi(request,id):
    result = NVChienSi.TatCaChienSi(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
