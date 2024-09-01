from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVDonVi


@api_view(['POST'])
def Them(request):
    TenDonVi = request.data.get('TenDonVi')
    DiaDiem = request.data.get('DiaDiem')
    MaDonVi = request.data.get('MaDonVi')
    id_DonViCapTren = request.data.get('id_DonViCapTren')
    SoDienThoai = request.data.get('SoDienThoai')
    CapNhomDonVi = request.data.get('CapNhomDonVi')
    result = NVDonVi.ThemDonVi(TenDonVi, DiaDiem, MaDonVi, id_DonViCapTren, SoDienThoai, CapNhomDonVi)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ThongTin(request,id):
    result = NVDonVi.ThongTinDonVi(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def Sua(request,id):
    TenDonVi = request.data.get('TenDonVi')
    DiaDiem = request.data.get('DiaDiem')
    MaDonVi = request.data.get('MaDonVi')
    id_DonViCapTren = request.data.get('id_DonViCapTren')
    SoDienThoai = request.data.get('SoDienThoai')
    CapNhomDonVi = request.data.get('CapNhomDonVi')
    result = NVDonVi.SuaDonVi(id,TenDonVi, DiaDiem, MaDonVi, id_DonViCapTren, SoDienThoai, CapNhomDonVi)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaDonVi(request,id):
    try:
        # Lấy dữ liệu từ yêu cầu
        result = NVDonVi.XoaDonVi(id)
        if result["status"] == "success":
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def TimKiemDonVi(request):
    TimKiem = request.query_params.get('TimKiem')
    result = NVDonVi.TimDonVi(TimKiem)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['GET'])
def DropDownDV(request):
    id_CapDonVi = request.query_params.get('id_CapDonVi')
    result = NVDonVi.DropDownDV(id_CapDonVi)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def DonViCon(request):
    id_CapDonVi = request.query_params.get('id_CapDonVi')
    result = NVDonVi.DonViCon(id_CapDonVi)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def DonViChaTheoNhom(request):
    id_nhom = request.query_params.get('id_nhom')
    result = NVDonVi.DonViChaTheoNhom(id_nhom)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def TimDonVi(request):
    Nhom = request.query_params.get('Nhom')
    print(Nhom)
    TimKiem = request.query_params.get('TimKiem')
    result = NVDonVi.TimDonVi(Nhom, TimKiem)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_404_NOT_FOUND)