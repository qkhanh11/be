from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVCapBac,NVChucVu


@api_view(['POST'])
def ThemCapBac(request):
    TenCapBac = request.data.get('TenCapBac')
    result = NVCapBac.Them(TenCapBac)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PUT'])
def SuaCapBac(request,id):
    TenCapBac = request.data.get('TenCapBac')
    result = NVCapBac.Sua(id,TenCapBac)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def XoaCapBac(request,id):
    result = NVCapBac.Xoa(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def CapBac(request):
    result = NVCapBac.CapBac()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def ThemCapBacHSQ(request):
    TenCapBac = request.data.get('TenCapBac')
    result = NVCapBac.ThemCBHSQ(TenCapBac)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PUT'])
def SuaCapBacHSQ(request,id):
    TenCapBac = request.data.get('TenCapBac')
    result = NVCapBac.SuaCBHSQ(id,TenCapBac)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def XoaCBHSQ(request,id):
    result = NVCapBac.XoaCBHSQ(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def CapBacHSQ(request):
    result = NVCapBac.CapBacHSQ()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def ThemCVSQ(request):
    TenChucVu = request.data.get('TenChucVu')
    id_CapNhomDonVi = request.data.get('id_CapNhomDonVi')
    result = NVChucVu.ThemCVSQ(TenChucVu,id_CapNhomDonVi)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def ThemCVQNCN(request):
    TenChucVu = request.data.get('TenChucVu')
    id_CapNhomDonVi = request.data.get('id_CapNhomDonVi')
    result = NVChucVu.ThemCVQNCN(TenChucVu,id_CapNhomDonVi)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaCVSQ(request,id):
    TenChucVu = request.data.get('TenChucVu')
    id_CapNhomDonVi = request.data.get('id_CapNhomDonVi')
    result = NVChucVu.SuaCVSQ(id,TenChucVu,id_CapNhomDonVi)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaCVQNCN(request,id):
    TenChucVu = request.data.get('TenChucVu')
    id_CapNhomDonVi = request.data.get('id_CapNhomDonVi')
    result = NVChucVu.SuaCVQNVN(id,TenChucVu,id_CapNhomDonVi)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaCVSQ(request,id):
    result = NVChucVu.XoaCVSQ(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaCVQNCN(request,id):
    result = NVChucVu.XoaCVQNCN(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def CVSQ(request):
    id_CapNhomDonVi = request.query_params.get('id_CapNhomDonVi')
    result = NVChucVu.CVSQ(id_CapNhomDonVi)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def CVQNCN(request):
    id_CapNhomDonVi = request.query_params.get('id_CapNhomDonVi')
    result = NVChucVu.CVQNCN(id_CapNhomDonVi)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def CVSQTrongDonVi(request,id):
    result = NVChucVu.XemCVSQTrongDV(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)