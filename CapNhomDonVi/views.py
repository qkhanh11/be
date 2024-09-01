from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVCapNhomDonVi


@api_view(['POST'])
def Them(request):
    NhomDonVi = request.data.get('NhomDonVi')
    CapTren = request.data.get('CapTren')
    Ten = request.data.get('Ten')
    result = NVCapNhomDonVi.ThemCapNhomDonVi(NhomDonVi,Ten,CapTren)
    if result["status"] == "success":
        return Response(data={"status": "success", "message": "Thêm thành công."},status=status.HTTP_200_OK)
    else:
        return Response(data={"status": "error", "message": 'Có lỗi xảy ra'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def Sua(request,id):
    NhomDonVi = request.data.get('NhomDonVi')
    Cap = request.data.get('Cap')
    Ten = request.data.get('Ten')
    result = NVCapNhomDonVi.SuaCapNhomDonVi(id,NhomDonVi,Ten,Cap)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
def Xoa(request,id):
    result = NVCapNhomDonVi.XoaCapNhomDonVi(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def TimKiemTheoNhom(request,id):
    result = NVCapNhomDonVi.TimKiemTheoNhom(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ThongTin(request,id):
    result = NVCapNhomDonVi.ThongTin(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    


    

